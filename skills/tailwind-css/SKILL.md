---
name: tailwind-css
description: Disciplina de Tailwind para interfaces utilitárias React/Inertia. Use quando o usuário pedir ajuste visual, layout, responsividade, componentes, tabelas ou formulários com Tailwind no projeto `projeto-moderno`.
---

# Tailwind CSS

Use este skill para escrever Tailwind com clareza, consistência e sem excesso de truques.

## Diretrizes

1. Reuse a linguagem visual já presente no projeto.
2. Prefira classes utilitárias diretas e legíveis.
3. Mantenha responsividade explícita.
4. Evite composição de classes dinâmica quando um mapa simples resolver.
5. Preserve alinhamento, espaçamento e largura dos controles em mobile e desktop.
6. Use estados `hover`, `focus`, `disabled` e `dark` apenas quando o projeto realmente os suporta.

## Para Este Projeto

- O repo usa Tailwind 3, então siga o padrão existente de `tailwind.config.js` e `resources/css/app.css`.
- Não assuma sintaxe de Tailwind 4 sem checar a base instalada.
- Evite mexer na configuração global se um ajuste local resolve.
- Para formulários e tabelas, prefira classes estáveis e previsíveis.
- Garanta que textos e ações caibam sem quebrar o layout.

## Revisão Rápida

- Evite utilitários repetidos sem necessidade.
- Verifique se spacing, borders e radius são consistentes.
- Confirme se a tela continua agradável em 1280px e em mobile estreito.
