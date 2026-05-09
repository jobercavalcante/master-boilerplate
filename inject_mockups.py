import base64
import os

images = {
    'kds': r"C:\Users\jober\.gemini\antigravity\brain\54ab1f02-806a-43ea-b707-611dc72d3c86\kds_mockup_1778270471248.png",
    'gamification': r"C:\Users\jober\.gemini\antigravity\brain\54ab1f02-806a-43ea-b707-611dc72d3c86\waiter_gamification_mockup_1778270484722.png",
    'split': r"C:\Users\jober\.gemini\antigravity\brain\54ab1f02-806a-43ea-b707-611dc72d3c86\bill_split_mockup_1778270499986.png",
}

def img_to_b64(path):
    with open(path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode('utf-8')
        return f'<div style="text-align: center; margin: 2rem 0;"><img src="data:image/png;base64,{b64_string}" alt="Mockup de Interface Gerado por IA" style="max-width: 100%; max-height: 500px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);"></div>\n'

html_path = r"e:\projetos\master-boilerplate\documentacao_pdv.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. KDS Mockup
target_kds = "Esse desenho evita o erro clássico de “pedido salvo, mas ticket perdido” ou “ticket impresso duas vezes”.</p>"
content = content.replace(target_kds, target_kds + "\n" + img_to_b64(images['kds']))

# 2. Split Mockup
target_split = "<h3>1. Engenharia de Divisão e Junção de Comandas</h3>"
content = content.replace(target_split, target_split + "\n" + img_to_b64(images['split']))

# 3. Gamification Mockup
target_gamification = "<h3>3. Painel de Controle e Gamificação (Critérios de Conquista)</h3>"
content = content.replace(target_gamification, target_gamification + "\n" + img_to_b64(images['gamification']))

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Images injected successfully!")
