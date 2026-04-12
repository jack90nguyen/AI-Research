import json
import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def analyze_product(title, domain):
    title_lower = title.lower()
    
    # Heuristics for basic analysis
    audience = "Khách hàng mua quà tặng cá nhân hóa"
    insight = "Người dùng thích sản phẩm độc bản, mang đậm dấu ấn cá nhân hoặc kỷ niệm."
    scale = "Chạy quảng cáo Facebook/TikTok Ads với các mẫu creative tương tự, mở rộng thiết kế sang các sản phẩm khác (cốc, áo, chăn...)."
    
    if "dog" in title_lower or "cat" in title_lower or "pet" in title_lower:
        audience = "Những người nuôi thú cưng (Pet Lovers), xem thú cưng như thành viên gia đình."
        insight = "Nhu cầu lưu giữ khoảnh khắc hoặc tưởng nhớ thú cưng bằng các thiết kế nghệ thuật cao cấp hoặc ngộ nghĩnh."
        scale = "Target tệp khách hàng theo giống chó/mèo cụ thể. Bán upsell thêm các phụ kiện thú cưng khác."
    elif "mom" in title_lower or "dad" in title_lower or "family" in title_lower or "grandpa" in title_lower or "grandma" in title_lower:
        audience = "Người mua quà tặng cho các dịp gia đình (Mother's Day, Father's Day, Birthday)."
        insight = "Sản phẩm đánh vào cảm xúc, tình cảm gia đình. Yêu cầu tính cá nhân hóa cao (tên, ngày sinh, avatar)."
        scale = "Tạo các bundle quà tặng gia đình. Tối ưu SEO cho các dịp lễ lớn (Lễ Tạ Ơn, Giáng Sinh, Ngày của Mẹ/Cha)."
    elif "baby" in title_lower or "kids" in title_lower or "newborn" in title_lower:
        audience = "Cha mẹ trẻ, hoặc người thân tìm mua quà tặng thôi nôi, sinh nhật cho bé."
        insight = "Các bậc phụ huynh muốn lưu lại dấu mốc quan trọng của con cái một cách đáng yêu và an toàn."
        scale = "Mở rộng sang sách truyện cá nhân hóa, đồ chơi giáo dục. Target các group mẹ bỉm sữa."
    elif "couple" in title_lower or "love" in title_lower or "wedding" in title_lower or "anniversary" in title_lower:
        audience = "Các cặp đôi đang yêu, hoặc quà cưới, kỷ niệm ngày cưới."
        insight = "Cần sự lãng mạn, tinh tế và tính duy nhất của sản phẩm."
        scale = "Chạy ads mùa Valentine, Anniversary. Cung cấp tùy chọn hộp quà cao cấp."
    elif "blanket" in title_lower or "hoodie" in title_lower or "sweatshirt" in title_lower:
        audience = "Khách hàng chuộng phong cách lifestyle, gen Z hoặc Millennials thích sự thoải mái."
        insight = "Thích sản phẩm oversized, thoải mái mặc ở nhà (loungewear) với họa tiết bắt mắt."
        scale = "Tận dụng UGC (User Generated Content) trên TikTok, hợp tác với micro-influencers."
        
    return {
        "audience": audience,
        "insight": insight,
        "scale": scale
    }

def fetch_shopify_products(url):
    # Try appending /products.json or .json
    base_url = url.split('?')[0]
    api_url = f"{base_url}/products.json" if "/collections/" in base_url else f"{base_url}.json"
    
    try:
        req = urllib.request.Request(api_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            products = data.get('products', [])
            result = []
            for p in products[:10]:
                image_url = p['images'][0]['src'] if p.get('images') else ""
                price = p['variants'][0]['price'] if p.get('variants') else "N/A"
                
                result.append({
                    "title": p.get('title', 'Unknown'),
                    "image": image_url,
                    "price": f"${price}" if price != "N/A" else "N/A",
                    "url": f"{urllib.parse.urlparse(url).scheme}://{urllib.parse.urlparse(url).netloc}/products/{p.get('handle')}"
                })
            return result
    except Exception as e:
        return None

def fetch_generic_products(url):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            products = []
            
            # Very basic generic parsing for standard eCommerce classes
            items = soup.find_all(['div', 'li'], class_=lambda x: x and ('product' in x.lower() or 'item' in x.lower()))
            for item in items:
                title_elem = item.find(['h2', 'h3', 'a'])
                if not title_elem: continue
                title = title_elem.get_text(strip=True)
                
                img_elem = item.find('img')
                if not img_elem: continue
                image = img_elem.get('src') or img_elem.get('data-src') or ''
                if not image or image.startswith('data:image'): continue
                
                if image.startswith('//'):
                    image = f"https:{image}"
                elif image.startswith('/'):
                    image = urllib.parse.urljoin(url, image)
                    
                # avoid duplicates
                if any(p['title'] == title for p in products): continue
                if len(title) < 5: continue
                
                # Mock price for generic scraper if not easily found
                price_elem = item.find(string=lambda t: t and '$' in t)
                price = price_elem.strip() if price_elem else "Tham khảo trên web"
                
                # Mock Link
                link_elem = item.find('a')
                p_url = urllib.parse.urljoin(url, link_elem['href']) if link_elem and link_elem.has_attr('href') else url
                
                products.append({
                    "title": title,
                    "image": image,
                    "price": price,
                    "url": p_url
                })
                if len(products) >= 10: break
            return products
    except Exception as e:
        return None

def main():
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
    json_path = os.path.join(reports_dir, 'valid_new_arrival_links.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    all_results = []
    
    for entry in data:
        domain = entry['domain']
        links = entry.get('valid_links', [])
        if not links: continue
        
        target_link = links[0] # Try the first valid link
        print(f"Đang xử lý: {domain} - {target_link}")
        
        # 1. Try Shopify API first
        products = fetch_shopify_products(target_link)
        
        # 2. Try Generic Scraper if Shopify fails
        if not products:
            print(f"--> Fallback scraping for {domain}")
            products = fetch_generic_products(target_link)
            
        if products:
            for p in products:
                analysis = analyze_product(p['title'], domain)
                p.update(analysis)
            
            all_results.append({
                "domain": domain,
                "source_url": target_link,
                "products": products
            })
            print(f"--> Lấy thành công {len(products)} sản phẩm.")
        else:
            print(f"--> KHÔNG lấy được sản phẩm nào.")

    # Generate HTML
    html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo Cáo Sản Phẩm Mới (New Arrivals) - TOP POD 2026</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .domain-header { background-color: #343a40; color: white; padding: 15px; margin-top: 40px; border-radius: 8px 8px 0 0; }
        .product-card { background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; overflow: hidden; height: 100%; transition: transform 0.2s;}
        .product-card:hover { transform: translateY(-5px); }
        .product-img { width: 100%; height: 250px; object-fit: cover; }
        .product-info { padding: 15px; }
        .product-title { font-size: 1.1rem; font-weight: bold; margin-bottom: 10px; color: #212529; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .product-price { color: #e63946; font-size: 1.2rem; font-weight: bold; margin-bottom: 15px; }
        .analysis-box { background-color: #e9ecef; padding: 10px; border-radius: 5px; font-size: 0.9rem; }
        .analysis-title { font-weight: 600; color: #495057; margin-bottom: 5px; }
    </style>
</head>
<body>
    <div class="container py-5">
        <h1 class="text-center mb-2">Báo Cáo Phân Tích: Sản Phẩm Mới Tiềm Năng</h1>
        <p class="text-center text-muted mb-5">Phân tích top sản phẩm mới từ danh sách 20 website POD hàng đầu</p>
"""
    for res in all_results:
        domain = res['domain']
        html_content += f'<h2 class="domain-header">{domain} <a href="{res["source_url"]}" target="_blank" class="btn btn-sm btn-light float-end">Xem Nguồn</a></h2>\n'
        html_content += '<div class="row pt-4 bg-white border border-top-0 rounded-bottom p-3 mb-4">\n'
        
        for p in res['products']:
            html_content += f"""
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="product-card">
                    <img src="{p['image']}" class="product-img" alt="Product Image">
                    <div class="product-info">
                        <a href="{p['url']}" target="_blank" class="text-decoration-none"><div class="product-title">{p['title']}</div></a>
                        <div class="product-price">{p['price']}</div>
                        
                        <div class="analysis-box">
                            <div class="analysis-title">👥 Tệp Khách Hàng:</div>
                            <p class="mb-2 text-muted">{p['audience']}</p>
                            
                            <div class="analysis-title">💡 Insight Phân Tích:</div>
                            <p class="mb-2 text-muted">{p['insight']}</p>
                            
                            <div class="analysis-title">🚀 Hướng Scale & Mở Rộng:</div>
                            <p class="mb-0 text-muted">{p['scale']}</p>
                        </div>
                    </div>
                </div>
            </div>
            """
        html_content += '</div>\n'

    html_content += """
    </div>
    <footer class="text-center py-4 text-muted">
        <small>Generated by AI Agent Workspace</small>
    </footer>
</body>
</html>"""

    report_path = os.path.join(reports_dir, 'top_new_products_analysis.html')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"\nThành công! Đã tạo file HTML tại: {report_path}")

if __name__ == '__main__':
    main()
