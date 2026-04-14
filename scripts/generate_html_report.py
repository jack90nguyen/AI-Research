import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_html():
    try:
        analysis_data = load_json('reports/top10_analysis.json')
        products_data = load_json('reports/products_scraped.json')
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    html_content = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Top 10 Sản Phẩm Mới Tiềm Năng - Macorner</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; padding: 20px; background-color: #f5f7fa; }
            h1 { text-align: center; color: #2c3e50; margin-bottom: 30px; font-size: 2.5em; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
            .product-card { background: #fff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 30px; overflow: hidden; display: flex; flex-wrap: wrap; }
            .product-image { flex: 1 1 300px; max-width: 400px; padding: 20px; text-align: center; border-right: 1px solid #eee; }
            .product-image img { max-width: 100%; border-radius: 4px; }
            .product-info { flex: 2 1 500px; padding: 20px 30px; }
            .product-title { margin-top: 0; color: #2c3e50; font-size: 1.5em; }
            .product-title a { color: #3498db; text-decoration: none; }
            .product-title a:hover { text-decoration: underline; }
            .price { font-size: 1.2em; font-weight: bold; color: #e74c3c; margin: 10px 0; }
            .product-type { display: inline-block; background: #ecf0f1; padding: 4px 10px; border-radius: 4px; font-size: 0.9em; margin-bottom: 15px; color: #7f8c8d; }
            .scores { display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }
            .score-badge { background: #3498db; color: white; padding: 8px 12px; border-radius: 6px; font-weight: bold; text-align: center; flex: 1; min-width: 100px; }
            .score-badge.avg { background: #27ae60; font-size: 1.1em; }
            .analysis { background: #f9f9f9; padding: 15px; border-left: 4px solid #3498db; border-radius: 4px; }
            .analysis h4 { margin-top: 0; color: #2c3e50; }
            @media (max-width: 768px) {
                .product-image { border-right: none; border-bottom: 1px solid #eee; max-width: 100%; }
            }
        </style>
    </head>
    <body>
        <h1>Top 10 Sản Phẩm Mới Tiềm Năng - Macorner</h1>
    """

    for item in analysis_data:
        idx = item['id']
        product = products_data[idx] if idx < len(products_data) else {}
        
        title = item.get('title', product.get('title', 'Unknown Title'))
        product_type = item.get('product_type', product.get('product_type', 'Unknown Type'))
        
        # Get link
        handle = product.get('handle', '')
        link = f"https://macorner.co/products/{handle}" if handle else "#"
        
        # Get image
        image_url = ""
        if 'images' in product and len(product['images']) > 0:
            image_url = product['images'][0].get('src', '')
        
        # Get price
        price = "N/A"
        if 'variants' in product and len(product['variants']) > 0:
            price = f"${product['variants'][0].get('price', 'N/A')}"
            
        scores = item.get('scores', {})
        avg_score = scores.get('average', 0)
        demand = scores.get('demand', 0)
        creativity = scores.get('creativity', 0)
        novelty = scores.get('novelty', 0)
        willingness = scores.get('willingness_to_pay', 0)
        
        analysis_text = item.get('analysis', '')
        
        html_content += f"""
        <div class="product-card">
            <div class="product-image">
                <img src="{image_url}" alt="{title}">
            </div>
            <div class="product-info">
                <h2 class="product-title"><a href="{link}" target="_blank">{title}</a></h2>
                <div class="product-type">{product_type}</div>
                <div class="price">{price}</div>
                
                <div class="scores">
                    <div class="score-badge avg">
                        <div>Điểm TB</div>
                        <div>{avg_score}/10</div>
                    </div>
                    <div class="score-badge">
                        <div>Demand</div>
                        <div>{demand}/10</div>
                    </div>
                    <div class="score-badge">
                        <div>Sáng tạo</div>
                        <div>{creativity}/10</div>
                    </div>
                    <div class="score-badge">
                        <div>Mới lạ</div>
                        <div>{novelty}/10</div>
                    </div>
                    <div class="score-badge">
                        <div>Sẵn sàng chi</div>
                        <div>{willingness}/10</div>
                    </div>
                </div>
                
                <div class="analysis">
                    <h4>Phân tích chi tiết:</h4>
                    <p>{analysis_text.replace(chr(10), '<br>')}</p>
                </div>
            </div>
        </div>
        """

    html_content += """
    </body>
    </html>
    """

    with open('reports/top10_potential_products.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Successfully generated reports/top10_potential_products.html")

if __name__ == "__main__":
    generate_html()
