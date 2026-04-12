import urllib.request
import urllib.error
import json
import os
from concurrent.futures import ThreadPoolExecutor

def check_url(url):
    """
    Checks if a URL is valid (returns 200 OK).
    Returns True if valid, False otherwise.
    """
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        })
        # Use GET request as some sites might block HEAD or behave differently
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200
    except Exception as e:
        return False

def validate_domain_links(entry):
    valid_links = []
    
    # Try all links in new_links
    for link in entry.get('new_links', []):
        if check_url(link):
            valid_links.append(link)
    
    entry['valid_links'] = valid_links
    return entry

def main():
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
    json_path = os.path.join(reports_dir, 'new_arrival_links.json')
    
    if not os.path.exists(json_path):
        print(f"Không tìm thấy file {json_path}")
        return
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    print(f"Bắt đầu kiểm tra tính khả dụng của các link cho {len(data)} domain...")
    
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for res in executor.map(validate_domain_links, data):
            results.append(res)
            print(f"Đã kiểm tra domain: {res['domain']} - Tìm thấy {len(res['valid_links'])} link khả dụng.")
            
    # Ghi đè file JSON với thông tin valid_links
    out_json_path = os.path.join(reports_dir, 'valid_new_arrival_links.json')
    with open(out_json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
        
    # Tạo lại file MD chỉ chứa các link khả dụng
    out_md_path = os.path.join(reports_dir, 'valid_new_arrival_links.md')
    with open(out_md_path, 'w', encoding='utf-8') as f:
        f.write("# Danh Sách Link Sản Phẩm Mới (Đã Kiểm Tra Khả Dụng)\n\n")
        f.write("Dưới đây là các link chứa danh sách sản phẩm mới của 20 website POD đã được kiểm tra (trả về HTTP 200 OK):\n\n")
        
        for r in results:
            f.write(f"### {r['domain']}\n")
            if not r['valid_links']:
                f.write("> **Không tìm thấy link 'mới' nào khả dụng/truy cập được.**\n\n")
            else:
                for link in r['valid_links']:
                    f.write(f"- [{link}]({link})\n")
            f.write("\n")
            
    print(f"\nThành công! Đã cập nhật báo cáo các link khả dụng vào:\n- {out_json_path}\n- {out_md_path}")

if __name__ == '__main__':
    main()
