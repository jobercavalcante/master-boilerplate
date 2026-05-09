---
name: roadmap-detailed
description: Mantém o ROADMAP.md sempre rico, extremamente detalhado e preserva todo o histórico de tarefas já concluídas.
---

# Detalhamento do ROADMAP.md

Ao trabalhar com o `ROADMAP.md` (seja criando um novo plano, adicionando tarefas ou concluindo marcos no framework GSD), você DEVE seguir as seguintes regras de detalhamento extremo:

1. **Nunca resuma tarefas importantes**: O ROADMAP.md não é apenas uma lista de checkboxes simples de uma linha. Ele é o diário de bordo arquitetural do projeto.
2. **Contexto Arquitetural Completo**: Para cada tarefa ou fase, explique:
   - **O que** foi feito (a regra de negócio).
   - **Quais** padrões técnicos e ferramentas foram usados (ex: Thin Controllers, Inertia, React, Spatie Roles).
   - **Onde** o impacto ocorreu (quais models, tabelas ou telas específicas).
3. **Mantenha o Histórico Vivo**: NUNCA apague o histórico de tarefas já concluídas sob a premissa de "limpar o arquivo" ou "enxugar o log". O usuário exige que a listagem de tudo que já foi construído permaneça intacta e visível no arquivo, independentemente do tamanho que o documento atinja.
4. **Formatação Rica**: Utilize descrições com múltiplas linhas e tópicos aninhados sob cada item de checkbox (ex: `- [x] Tarefa 1`). Inclua o Status, a Descrição e os critérios de "Pronto quando".

**Gatilho**: Sempre que você (ou o GSD) for atualizar, modificar ou mesclar informações no `.planning/ROADMAP.md`, ative esta skill para garantir que a atualização expanda a informação em vez de comprimi-la.
