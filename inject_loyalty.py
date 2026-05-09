import base64

image_path = r"C:\Users\jober\.gemini\antigravity\brain\54ab1f02-806a-43ea-b707-611dc72d3c86\loyalty_program_mockup_1778271551861.png"
html_path = r"e:\projetos\master-boilerplate\documentacao_pdv.html"

def img_to_b64(path):
    with open(path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode('utf-8')
        return f'<div style="text-align: center; margin: 2rem 0;"><img src="data:image/png;base64,{b64_string}" alt="Customer Loyalty App Mockup Gerado por IA" style="max-width: 100%; max-height: 500px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);"></div>\n'

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

target_content = """    <!-- PARTE 2 -->
    <h2>12. Análise de Viabilidade: Stack Master Boilerplate</h2>"""

new_section = """    <!-- NOVA SEÇÃO -->
    <h2>12. Promoções e Programa de Fidelização (Opt-in)</h2>
""" + img_to_b64(image_path) + """
    <p>A captação e retenção de clientes por meio de promoções e um programa de fidelização (Loyalty) são diferenciais massivos para o crescimento recorrente do restaurante. Como essa é uma funcionalidade opcional (<em>Opt-in</em>), sua arquitetura deve ser altamente modular e desacoplada do fluxo essencial de transações do caixa (PDV).</p>

    <h3>1. Gestão de Pontos e Carteira Digital (Ledger)</h3>
    <ul>
        <li><strong>Identificação do Cliente:</strong> O cliente se identifica no QR Code do Autoatendimento (via telefone ou CPF). O sistema vincula sua sessão efêmera a um perfil de <code>Customer</code> global (ou focado no Tenant).</li>
        <li><strong>Ledger de Fidelidade Imutável:</strong> Cada cliente possui uma <code>LoyaltyWallet</code>. O acúmulo ou resgate de pontos deve seguir um padrão de <em>Append-Only Ledger</em> ou <em>Event-Sourcing</em> (ex: <code>PointsAwardedEvent</code>). Isso impede que inconsistências no banco de dados destruam o saldo do cliente e fornece um histórico perfeito para auditoria.</li>
        <li><strong>Motor de Regras Dinâmico:</strong> A conversão de R$ em Pontos é governada por políticas configuráveis pelo SuperAdmin ou Gerente (ex: <em>"Dobro de pontos nas terças-feiras"</em> ou <em>"Itens da categoria Bebidas não pontuam"</em>).</li>
    </ul>

    <h3>2. Disparadores Promocionais e Marketing Ativo</h3>
    <ul>
        <li><strong>Cupons de Desconto (Promo Codes):</strong> Criação de cupons geridos por uma tabela <code>promocodes</code> com travas rígidas de elegibilidade (limite de usos, data de validade, valor mínimo do pedido, restrição a um único <code>tenant_id</code>).</li>
        <li><strong>Reengajamento via Laravel Queues:</strong> Uso das filas do Laravel (RabbitMQ/Redis) integradas ao <code>Task Scheduler</code> (Cron) para processar diariamente regras de reengajamento. Exemplo: disparar automaticamente um SMS/WhatsApp com um cupom especial para clientes que não visitam o restaurante há mais de 30 dias.</li>
    </ul>

    <!-- PARTE 2 -->
    <h2>13. Análise de Viabilidade: Stack Master Boilerplate</h2>"""

content = content.replace(target_content, new_section)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Loyalty Section and Image injected successfully!")
