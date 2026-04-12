import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

all_products = []
for i in range(1, 6):
    url = f"https://macorner.co/collections/new-arrivals/products.json?page={i}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, context=ctx)
        data = json.loads(response.read())
        products = data.get('products', [])
        all_products.extend(products)
    except Exception as e:
        print(f"Error on page {i}: {e}")

with open('products_scraped.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, indent=2, ensure_ascii=False)
print(f"Scraped {len(all_products)} products.")