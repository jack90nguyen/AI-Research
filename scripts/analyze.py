import json

with open('products_scraped.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for i, p in enumerate(products[:20]):
    print(f"{i+1}. {p['title']} - https://macorner.co/products/{p['handle']}")
    
    # Try to extract the first image
    image = ""
    if 'images' in p and len(p['images']) > 0:
        image = p['images'][0]['src']
    
    # Try to extract price from variants
    price = ""
    if 'variants' in p and len(p['variants']) > 0:
        price = p['variants'][0]['price']
        
    print(f"   Price: ${price} | Img: {image}\n")
