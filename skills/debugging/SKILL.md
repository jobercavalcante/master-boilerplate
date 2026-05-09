---
name: debugging
description: Investigue falhas até achar a causa raiz com evidência concreta. Use quando houver teste quebrado, erro de build, comportamento inesperado, regressão, falha de rota, problema de validação, bug Inertia ou qualquer mudança que precise ser diagnosticada com calma.
---

# Debugging

Use este skill para sair de sintoma e chegar em causa raiz.

## Processo

1. Reproduza o problema.
2. Leia a mensagem de erro inteira.
3. Localize a linha e o arquivo que originam a falha.
4. Formule uma hipótese por vez.
5. Aplique uma mudança pequena.
6. Reexecute o teste ou build relevante.
7. Pare quando a causa estiver confirmada.

## Regras

- Não adivinhe antes de ter evidência.
- Não faça várias correções ao mesmo tempo.
- Se o erro estiver em integração, rastreie contrato entre camadas.
- Se o erro for de Laravel, revise request, controller, model, migration, route e view nessa ordem.
- Se o erro for de frontend, revise props, estado inicial, import path e build output.

## Para Este Projeto

- Considere primeiro `projeto-moderno/`, não o projeto-legado.
- Se o problema envolver Reversa, preserve `_reversa_sdd/` e a trilha de execução.
- Se o build falhar por manifest ausente, confira `resources/js/app.jsx` e o output de `npm run build`.
