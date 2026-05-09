import base64

image_path = r"C:\Users\jober\.gemini\antigravity\brain\54ab1f02-806a-43ea-b707-611dc72d3c86\tef_nfce_mockup_1778271635837.png"
html_path = r"e:\projetos\master-boilerplate\documentacao_pdv.html"

def img_to_b64(path):
    with open(path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode('utf-8')
        return f'<div style="text-align: center; margin: 2rem 0;"><img src="data:image/png;base64,{b64_string}" alt="TEF e NFC-e Mockup Gerado por IA" style="max-width: 100%; max-height: 500px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);"></div>\n'

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

target_content = """    <!-- PARTE 2 -->
    <h2>13. Análise de Viabilidade: Stack Master Boilerplate</h2>"""

new_section = """    <!-- NOVA SEÇÃO -->
    <h2>13. Integração Fiscal e Pagamentos (NFC-e / TEF)</h2>
""" + img_to_b64(image_path) + """
    <p>Um PDV operando legalmente no Brasil exige conformidade fiscal estrita e fluidez no fluxo de pagamentos. A integração de TEF (Transferência Eletrônica de Fundos) e a emissão de NFC-e (Nota Fiscal de Consumidor Eletrônica) são gargalos críticos que não admitem latência ou falhas de comunicação com a SEFAZ.</p>

    <h3>1. TEF (Transferência Eletrônica de Fundos)</h3>
    <ul>
        <li><strong>Arquitetura Client-Server Local:</strong> O TEF exige a comunicação direta com um hardware (PinPad). O navegador web moderno (onde roda o React/Inertia) é isolado por sandbox e não consegue comunicar via porta Serial/USB diretamente com o hardware.</li>
        <li><strong>A Solução (WebSocket Local Agent):</strong> A abordagem padrão-ouro para PDVs web é criar um <em>Micro-serviço Local</em> ou "Agente" (ex: um executável leve em Node.js, Go ou C#) rodando na própria máquina do caixa local. Quando o usuário clica em "Pagar com Cartão" na interface web, o React se conecta a esse Agente Local via <code>ws://127.0.0.1:XXXX</code>. O agente local assume o controle, comunica-se via DLL/SO com a biblioteca do provedor TEF (SiTef, PayGo, etc) enviando as requisições ao PinPad e devolve a autorização assinada de volta para o navegador, que então prossegue mandando o sucesso ao backend Laravel.</li>
    </ul>

    <h3>2. Emissão de NFC-e e SEFAZ</h3>
    <ul>
        <li><strong>Autorização Síncrona vs Assíncrona:</strong> A NFC-e requer o empacotamento, assinatura digital do XML e envio para a SEFAZ. APIs modernas de mensageria fiscal (como Focus NFe, Oobj ou o próprio pacote NFePHP) podem ser acopladas no Laravel via classes abstratas de Serviço (<code>App\Services\FiscalService</code>). O processamento exige que a interface de checkout fique travada em um "loader" blindado aguardando o recibo de autorização.</li>
        <li><strong>Impressão RAW do Danfe (ESC/POS):</strong> Com o XML aprovado, a SEFAZ devolve os dados, incluindo a URL do QR Code da NFC-e. Novamente, acionamos a ponte do Agente Local (a mesma que controla o TEF), enviando uma payload JSON que será traduzida em comandos <code>ESC/POS</code> puros para que a impressora térmica não-fiscal cuspa o Danfe no mesmo milissegundo, contornando completamente a aba de impressão lenta e visual do navegador.</li>
        <li><strong>Contingência Offline (Emissão Posterior):</strong> É imprescindível lidar com interrupções do lado da SEFAZ. O sistema no Laravel deve criar contingências para emitir localmente a nota e registrar a transação, inserindo um registro pendente. Um Job assíncrono no <code>Laravel Horizon</code> ficará rodando em loop para sincronizar e enviar esses XMLs retidos assim que os serviços fiscais restabelecerem conexão.</li>
    </ul>

    <!-- PARTE 2 -->
    <h2>14. Análise de Viabilidade: Stack Master Boilerplate</h2>"""

content = content.replace(target_content, new_section)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("TEF/NFC-e Section and Image injected successfully!")
