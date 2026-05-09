import re
import base64
import urllib.request

def fetch_svg_base64(diagram_text):
    encoded = base64.b64encode(diagram_text.encode('utf-8')).decode('utf-8')
    url = "https://mermaid.ink/svg/" + encoded
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            svg_data = response.read()
            b64 = base64.b64encode(svg_data).decode('utf-8')
            return f"data:image/svg+xml;base64,{b64}"
    except Exception as e:
        print(f"Error fetching SVG: {e}")
        return None

def process_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all <div class="mermaid">...</div>
    pattern = re.compile(r'<div class="mermaid">(.*?)</div>', re.DOTALL)
    
    def replacer(match):
        diagram_text = match.group(1).strip()
        print("Generating graph for block...")
        b64_uri = fetch_svg_base64(diagram_text)
        if b64_uri:
            return f'<div class="mermaid-img" style="text-align: center; margin: 1.5rem 0;"><img src="{b64_uri}" alt="Diagrama Mermaid" style="max-width: 100%; height: auto; border: 1px solid #e2e8f0; border-radius: 4px; padding: 1rem; background: #fff;"></div>'
        else:
            return match.group(0)

    new_content = pattern.sub(replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done processing HTML!")

process_html('documentacao_pdv.html')
