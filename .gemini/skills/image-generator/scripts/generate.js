import { GoogleGenAI } from '@google/genai';
import fs from 'fs';
import path from 'path';

// Lấy tham số từ command line
const prompt = process.argv[2];
const outputFile = process.argv[3] || 'generated_image.jpg';

if (!prompt) {
  console.error('Lỗi: Bạn phải cung cấp câu lệnh (prompt) để tạo ảnh.');
  console.error('Cách sử dụng: node generate.js "<prompt>" [tên_file_đầu_ra.jpg]');
  process.exit(1);
}

// Kiểm tra API Key
const apiKey = process.env.GEMINI_API_IMG;
if (!apiKey) {
  console.error('Lỗi: Không tìm thấy biến môi trường GEMINI_API_IMG.');
  console.error('Vui lòng thiết lập bằng lệnh: export GEMINI_API_IMG="your_api_key_here"');
  process.exit(1);
}

const ai = new GoogleGenAI({ apiKey });

async function generateImage() {
  console.log(`Đang tạo ảnh với câu lệnh: "${prompt}"...`);
  try {
    const response = await ai.models.generateImages({
      model: 'imagen-4.0-generate-001',
      prompt: prompt,
      config: {
        numberOfImages: 1,
        aspectRatio: '1:1', // Có thể điều chỉnh: '1:1', '3:4', '4:3', '9:16', '16:9'
        outputMimeType: 'image/jpeg'
      }
    });

    const generatedImage = response.generatedImages[0];
    
    if (generatedImage) {
      const buffer = Buffer.from(generatedImage.image.imageBytes, 'base64');
      const outputPath = path.resolve(process.cwd(), outputFile);
      fs.writeFileSync(outputPath, buffer);
      console.log(`✅ Thành công! Ảnh đã được lưu tại: ${outputPath}`);
    } else {
      console.error('Lỗi: Không có ảnh nào được trả về từ API.');
    }
  } catch (error) {
    console.error('❌ Lỗi khi gọi API tạo ảnh:');
    console.error(error.message);
  }
}

generateImage();