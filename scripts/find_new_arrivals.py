import urllib.request
import urllib.parse
from html.parser import HTMLParser
import json
import os
from concurrent.futures import ThreadPoolExecutor

class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    # filter out javascript:, mailto:, etc.
                    if value and not value.startswith(('javascript:', 'mailto:', 'tel:')):
                        full_url = urllib.parse.urljoin(self.base_url, value)
                        if self.base_url in full_url: # only keep same-domain links
                            self.links.add(full_url)

domains = [
    "wanderprints.com", "gossby.com", "pawfecthouse.com", "crownandpaw.com",
    "westandwillow.com", "personalizationmall.com", "shutterfly.com",
    "markandgraham.com", "wonderbly.com", "bluecrate.com", "theoodie.com",
    "macorner.co", "gearbunch.com", "uncommongoods.com", "meowingtons.com",
    "pupsentials.com", "ilikemaps.com", "wrappiness.co", "minted.com",
    "sunflowerly.com"
]

def check_domain(domain):
    url = f"https://{domain}"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    })
    
    result = {"domain": domain, "new_links": [], "error": None}
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            parser = LinkParser(url)
            parser.feed(html)
            
            # Find links that might indicate "new arrivals" or "new products"
            keywords = ['new-arrival', '/new', '/collections/new', 'latest', 'recent']
            
            likely_links = set()
            for link in parser.links:
                link_lower = link.lower()
                path = urllib.parse.urlparse(link_lower).path
                parts = path.split('/')
                
                # Check if 'new' or related keywords are present as standalone path parts or exact matches
                if any(kw in path for kw in keywords) or 'new' in parts or 'new-arrivals' in parts:
                    likely_links.add(link)
                     
            likely_links = list(likely_links)
            
            if likely_links:
                # Lấy 3 link đầu tiên có vẻ liên quan nhất
                result['new_links'] = sorted(likely_links, key=len)[:3]
            else:
                # Provide educated guesses
                result['new_links'] = [f"{url}/collections/new-arrivals", f"{url}/new"]
                result['error'] = "Không tìm thấy link 'mới' cụ thể trên trang chủ, đây là các link dự đoán."
                
    except Exception as e:
        result['error'] = f"Lỗi truy cập trang chủ: {str(e)}"
        # Fallback educated guesses
        result['new_links'] = [f"{url}/collections/new-arrivals", f"{url}/new"]
        
    return result

def main():
    results = []
    print("Đang quét tìm link danh sách sản phẩm mới cho 20 website...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        for res in executor.map(check_domain, domains):
            results.append(res)
            print(f"Đã xử lý: {res['domain']}")
            
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    json_path = os.path.join(reports_dir, 'new_arrival_links.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
        
    md_path = os.path.join(reports_dir, 'new_arrival_links.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Danh Sách Link Sản Phẩm Mới (New Arrivals) Của 20 Website Bán Lẻ POD\n\n")
        f.write("Dưới đây là danh sách các link sản phẩm mới nhất được trích xuất tự động từ trang chủ của 20 website thương hiệu:\n\n")
        
        for r in results:
            f.write(f"### {r['domain']}\n")
            if r['error']:
                f.write(f"> **Lưu ý:** {r['error']}\n\n")
            for link in r['new_links']:
                f.write(f"- [{link}]({link})\n")
            f.write("\n")
            
    print(f"Thành công! Báo cáo đã được lưu vào: \n- {json_path}\n- {md_path}")

if __name__ == '__main__':
    main()
