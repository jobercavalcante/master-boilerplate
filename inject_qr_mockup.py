import base64

image_path = r"C:\Users\jober\.gemini\antigravity\brain\54ab1f02-806a-43ea-b707-611dc72d3c86\customer_qr_menu_mockup_1778271305670.png"
html_path = r"e:\projetos\master-boilerplate\documentacao_pdv.html"

def img_to_b64(path):
    with open(path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode('utf-8')
        return f'<div style="text-align: center; margin: 2rem 0;"><img src="data:image/png;base64,{b64_string}" alt="Customer QR Menu App Mockup Gerado por IA" style="max-width: 100%; max-height: 500px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);"></div>\n'

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

target_tenant = "<h2>11. Autoatendimento via QR Code (Mesa/Comanda)</h2>"
content = content.replace(target_tenant, target_tenant + "\n" + img_to_b64(image_path))

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("QR Menu Image injected successfully!")
