import urllib.request
import urllib.parse
import re
import os
import time

os.makedirs('ai_mockups', exist_ok=True)

prompts = [
    "Acrylic plaque mockup, Mom's Garden, birth flowers, modern clear glass sign, soft lighting, product photography",
    "Acrylic plaque mockup, Cat Mom's Garden with cute paw prints, clear glass sign, soft lighting, product photography",
    "Throw pillow mockup on a sofa, rustic garden theme floral pattern, personalized gift, high quality interior photography",
    "Glass angel figurine mockup holding preserved flowers, memorial gift In Loving Memory, elegant soft lighting, dark background",
    "Glass angel Christmas tree ornament mockup, elegant warm holiday lighting, pine tree background, high quality",
    "Glass angel figurine mockup resting on a glowing LED wooden base, premium black gift box, luxury product photography",
    "Elegant silver friendship bracelet mockup, Soul Sisters engraving, soft minimalist background, jewelry product photography",
    "Silver matching couples bracelet mockup, custom GPS coordinates engraving, minimalist background, jewelry photography",
    "Set of three matching silver bracelets bundle mockup, Family connection jewelry, minimalist white background, high quality",
    "Wooden bookshelf decor book nook mockup, rustic wood, personalized favorite books engraving, cozy library lighting",
    "Gamer setup corner wooden plaque mockup, neon LED lighting background, cool product photography",
    "Engraved wooden bookmark mockup with a tassel, resting on an open old book, cozy aesthetic, high quality",
    "Canvas tote bag mockup with blue Toile De Jouy vintage french countryside pattern, bright outdoor lighting, fashion photography",
    "Insulated wine tumbler mockup, beautiful watercolor family portrait printed on it, white background, product photography",
    "Cozy fleece blanket mockup draped over a bed, blue Toile De Jouy vintage pattern, bright bedroom lighting",
    "Unisex t-shirt mockup, Baseball Mom graphic design, sporty aesthetic, bright studio lighting, flat lay",
    "Cozy winter hoodie sweatshirt mockup, Sports Mom graphic design, folded neatly on a wooden table, top down view",
    "Large metal sports water jug tumbler mockup, Sports Mom engraving, gym background, high quality product photography",
    "Small ceramic plant pot mockup containing a cute succulent, Crazy Plant Lady text with a cat silhouette, soft lighting",
    "Bundle of three small ceramic plant pots mockup with succulents, minimalist white background, home decor product photography",
    "Mini wooden gardening tools shovel and rake mockup, custom engraved handles, resting on potting soil, top down view",
    "Wooden graduation plaque mockup, Nurse Graduation medical theme, stethoscope and flowers, wooden desk background",
    "Insulated coffee tumbler mockup, Graduation Tears funny quote, office desk background, high quality product photography",
    "Elegant wooden custom photo frame mockup, Graduation theme, resting on a shelf, interior decor photography",
    "Elegant crystal whiskey glass mockup, Reasons Dad Drinks engraving, dark moody lighting, luxury product photography",
    "Leather wine bag mockup, Funny Teacher's Wine quote, rustic wooden table, cozy indoor lighting",
    "Set of square stone drink coasters mockup, humorous drinking quotes, minimalist coffee table, top down view",
    "Insulated wine tumbler mockup, Winter Ski Trip mountain theme, snowy background, high quality product photography",
    "Group of three matching insulated wine tumblers mockup, Cruise Squad tropical theme, beach background",
    "Travel bundle mockup, matching insulated tumbler and a canvas tote bag, Girls Trip theme, bright studio lighting"
]

urls = [f"https://image.pollinations.ai/prompt/{urllib.parse.quote(p)}?width=400&height=400&nologo=true" for p in prompts]

for i, url in enumerate(urls):
    filename = f"ai_mockups/mockup_{i+1}.jpg"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        continue
        
    retries = 3
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Đã tải ảnh {i+1}/30")
            break
        except Exception as e:
            if attempt == retries - 1:
                print(f"Lỗi tải ảnh {i+1}: {e}")
            time.sleep(2) # Sleep to avoid 429 Too Many Requests

with open("top10_products_macorner_ai.html", "r", encoding="utf-8") as f:
    html_content = f.read()

def replacer(match, idx=[0]):
    filename = f"./ai_mockups/mockup_{idx[0]+1}.jpg"
    idx[0] += 1
    return f'src="{filename}"'

html_content = re.sub(r'src="https://image\.pollinations\.ai/[^"]+"', replacer, html_content)

with open("top10_products_macorner_offline.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Hoàn tất tải ảnh và tạo file HTML offline.")
