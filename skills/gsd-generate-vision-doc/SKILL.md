---
name: gsd-generate-vision-doc
description: "Gerar documentação técnica de viabilidade e arquitetura (Vision Document) em arquivo HTML único com injeção de mockups em base64"
---

<objective>
Guia o sistema a explorar, arquitetar e gerar uma documentação técnica de viabilidade de alto nível (Vision Document) para novos produtos ou módulos complexos. O resultado final deve ser um arquivo HTML único, esteticamente polido e portável, enriquecido com diagramas e mockups de interface gerados por IA, codificados em Base64 diretamente no código.
</objective>

<process>
1. **Coleta de Requisitos e Arquitetura:**
   - Explore com o usuário os domínios, fluxos e restrições operacionais do sistema.
   - Analise a aderência tecnológica com a stack atual (ex: Laravel, Inertia, React) e identifique como contornar gargalos (ex: TEF, Offline-first, Multi-tenant).

2. **Criação do Documento Base (HTML):**
   - Crie o arquivo base (ex: `documentacao_viabilidade.html`) contendo CSS moderno embutido (ex: tipografia limpa, caixas de alerta, tabelas padronizadas).
   - Estruture o documento por módulos, explicando a estratégia de engenharia, arquitetura de banco de dados (ACID, Locks, Transactions), WebSocket, filas e rotinas assíncronas.

3. **Enriquecimento Visual com Mockups (IA):**
   - Sempre que descrever uma interface crítica ou fluxo complexo, gere um mockup de interface usando a ferramenta `generate_image`.
   - Crie prompts detalhados e precisos (ex: "high-fidelity modern UI dashboard, glassmorphism, dark mode").

4. **Injeção Automática via Python (Base64):**
   - Para manter o HTML como um arquivo único e portátil, **NÃO** referencie caminhos locais nas tags `<img>`.
   - Crie um script Python temporário para ler o arquivo da imagem gerada pela IA, converter para string Base64 e injetar a tag `<img src="data:image/png;base64,...">` diretamente no arquivo HTML.
   - Execute o script Python usando a ferramenta `run_command` e notifique o usuário sobre o sucesso da injeção.

5. **Iteração Contínua:**
   - Aceite feedback do usuário sobre novas regras de negócios (ex: integrações fiscais, fidelização).
   - Siga gerando imagens, criando scripts de injeção em Python para os novos blocos e atualizando o HTML contornando limites de tokens (usando scripts Python para substituição e concatenação em arquivos muito grandes).
</process>
