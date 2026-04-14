import json
from camoufox import Camoufox

def main():
    url = "https://wanderprints.com/collections/new-arrival"
    with Camoufox(headless=True) as browser:
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        
        # Execute Javascript directly in browser to get image URLs and alts
        products = page.evaluate('''() => {
            const images = [];
            document.querySelectorAll('img').forEach(img => {
                let src = img.getAttribute('src') || img.getAttribute('data-src') || img.getAttribute('data-srcset') || '';
                let alt = img.getAttribute('alt') || '';
                
                if (src.startsWith('//')) {
                    src = 'https:' + src;
                }
                
                if (src && alt) {
                    if (src.includes('{width}')) {
                        src = src.replace('{width}', '800');
                    }
                    images.push({title: alt.trim(), image: src});
                }
            });
            return images;
        }''')
            
    with open("reports/real_images.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()