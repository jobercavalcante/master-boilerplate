---
name: verification-before-completion
description: Exija verificação objetiva antes de dizer que terminou. Use antes de encerrar qualquer tarefa, correção, commit ou resposta de conclusão, especialmente quando houver testes, build, migrations, rotas, Inertia ou alterações em múltiplas camadas.
---

# Verification Before Completion

Use este skill como a última porta antes de declarar sucesso.

## Gate

Antes de afirmar que a tarefa está pronta:

1. Identifique o que mudou.
2. Rode o check mais próximo do risco.
3. Leia o resultado completo.
4. Verifique o que o resultado realmente prova.
5. Só então declare concluído.

## Regras

- Não reutilize um resultado antigo como prova nova.
- Se houver testes, rode pelo menos um teste focado e um check mais amplo quando fizer sentido.
- Se houver frontend, valide build.
- Se houver migrations, valide status ou aplicação local.
- Se houver Inertia, confira props e navegação.

## Para Este Projeto

- Combine bem com `reversa-reconstructor`: não marque uma tarefa como feita sem executar a validação mínima.
- Quando a mudança tocar PHP e React, rode `composer test` e `npm run build` antes de fechar.
