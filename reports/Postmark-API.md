# Hướng dẫn tích hợp Postmark API (Chi tiết)

Tài liệu này cung cấp thông tin kỹ thuật chi tiết về các REST API của Postmark, bao gồm cấu trúc Request/Response và ví dụ mã nguồn NodeJS.

---

## 1. Xác thực (Authentication)
Mọi yêu cầu đến Postmark API đều yêu cầu Header:
*   `X-Postmark-Server-Token`: Token dành cho Server cụ thể (gửi/nhận mail).
*   `X-Postmark-Account-Token`: Token dành cho quản lý tài khoản (tên miền, server).
*   `Accept: application/json`
*   `Content-Type: application/json`

---

## 2. Chi tiết các Endpoint chính

### A. Gửi Email đơn (Single Email)
**Endpoint:** `POST https://api.postmarkapp.com/email`

**Request Body:**
```json
{
  "From": "sender@example.com",
  "To": "receiver@example.com",
  "Subject": "Tiêu đề email",
  "HtmlBody": "<html><body><strong>Nội dung HTML</strong></body></html>",
  "TextBody": "Nội dung văn bản thuần",
  "MessageStream": "outbound",
  "TrackOpens": true
}
```

**Response (200 OK):**
```json
{
  "To": "receiver@example.com",
  "SubmittedAt": "2023-10-27T07:25:01-05:00",
  "MessageID": "0a129aee-e1cd-480d-b08d-4f48548ff48d",
  "ErrorCode": 0,
  "Message": "OK"
}
```

**Ví dụ NodeJS:**
```javascript
const postmark = require("postmark");
const client = new postmark.ServerClient("your-server-token");

client.sendEmail({
  "From": "sender@yourdomain.com",
  "To": "user@example.com",
  "Subject": "Hello from Postmark",
  "HtmlBody": "<strong>Hello</strong> dear Postmark user.",
  "TextBody": "Hello dear Postmark user.",
  "MessageStream": "outbound"
}).then(response => {
  console.log("Sent ID:", response.MessageID);
});
```

---

### B. Gửi Email hàng loạt (Batch Email)
**Endpoint:** `POST https://api.postmarkapp.com/email/batch`
*Tối đa 500 tin nhắn mỗi lần gọi.*

**Request Body:** Danh sách các đối tượng email như gửi đơn.
```json
[
  { "From": "a@b.com", "To": "c@d.com", "Subject": "Mail 1", "HtmlBody": "..." },
  { "From": "a@b.com", "To": "e@f.com", "Subject": "Mail 2", "HtmlBody": "..." }
]
```

**Ví dụ NodeJS:**
```javascript
client.sendEmailBatch([
  { "From": "sender@domain.com", "To": "user1@example.com", "Subject": "Batch 1", "HtmlBody": "Hi 1" },
  { "From": "sender@domain.com", "To": "user2@example.com", "Subject": "Batch 2", "HtmlBody": "Hi 2" }
]).then(responses => {
  responses.forEach(res => console.log(res.MessageID));
});
```

---

### C. Gửi bằng Template (Email with Template)
**Endpoint:** `POST https://api.postmarkapp.com/email/withTemplate`

**Request Body:**
```json
{
  "From": "sender@example.com",
  "To": "receiver@example.com",
  "TemplateId": 12345, // Hoặc TemplateAlias
  "TemplateModel": {
    "user_name": "Jack",
    "order_id": "ORD-123"
  },
  "InlineCss": true
}
```

**Ví dụ NodeJS:**
```javascript
client.sendEmailWithTemplate({
  "From": "sender@domain.com",
  "To": "user@example.com",
  "TemplateAlias": "welcome-email",
  "TemplateModel": {
    "product_name": "Postmark Guide",
    "name": "Jack"
  }
});
```

---

### D. Quản lý lỗi (Bounces)
**Lấy danh sách lỗi:** `GET https://api.postmarkapp.com/bounces?count=50&offset=0`

**Response:**
```json
{
  "TotalCount": 1,
  "Bounces": [
    {
      "ID": 1234567,
      "Type": "HardBounce",
      "Email": "bad-email@example.com",
      "BouncedAt": "2023-10-27T07:25:01Z",
      "Description": "The server was unable to deliver your message...",
      "Inactive": true,
      "CanActivate": true
    }
  ]
}
```

**Ví dụ NodeJS:**
```javascript
client.getBounces({ count: 10, offset: 0 }).then(data => {
  console.log("Total Bounces:", data.TotalCount);
  data.Bounces.forEach(b => console.log(b.Email, b.Type));
});
```

---

### E. Theo dõi tin nhắn (Messages API)
**Chi tiết tin nhắn đã gửi:** `GET https://api.postmarkapp.com/messages/outbound/{messageid}/details`

**Response chứa thông tin sự kiện (Events):**
```json
{
  "MessageID": "...",
  "Status": "Sent",
  "MessageEvents": [
    { "Type": "Delivered", "ReceivedAt": "..." },
    { "Type": "Opened", "ReceivedAt": "..." }
  ]
}
```

**Ví dụ NodeJS (Lấy chi tiết):**
```javascript
client.getOutboundMessageDetails("message-id").then(msg => {
  console.log("Current Status:", msg.Status);
  console.log("Events:", msg.MessageEvents);
});
```

---

## 3. Webhook Dữ liệu mẫu (Inbound)
Khi nhận email, Postmark đẩy JSON về URL của bạn:
```json
{
  "From": "customer@gmail.com",
  "To": "support@yourdomain.com",
  "Subject": "Cần hỗ trợ",
  "TextBody": "Nội dung cần giải đáp...",
  "Attachments": [
    {
      "Name": "bill.pdf",
      "Content": "base64-string...",
      "ContentType": "application/pdf"
    }
  ]
}
```

---

## 4. Lưu ý quan trọng
1.  **Rate Limiting:** Postmark không có giới hạn cứng về số lượng request/giây, nhưng khuyến khích sử dụng Batch API khi gửi số lượng lớn.
2.  **Kích thước đính kèm:** Mỗi file tối đa 10MB.
3.  **Lưu trữ dữ liệu:** Postmark lưu trữ nội dung email trong 45 ngày mặc định.

---
*Tài liệu này được tổng hợp từ Postmark Developer Docs (2026).*
