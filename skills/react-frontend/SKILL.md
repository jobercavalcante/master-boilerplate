---
name: react-frontend
description: Práticas de React para componentes, estado, formulários e fluxos UI. Use quando o usuário pedir trabalho em React/Inertia, componentes reutilizáveis, estado local, formulários, renderização de listas, interação entre páginas ou correções de comportamento no frontend do projeto.
---

# React Frontend

Use este skill para implementar React com menos efeitos desnecessários e melhor fluxo de dados.

## Diretrizes

1. Comece pelos dados que a página recebe do backend.
2. Use estado local simples antes de abstrações maiores.
3. Prefira derivar valores em renderização quando o custo for baixo.
4. Use efeitos só quando houver sincronização real com o mundo externo.
5. Mantenha formulários controlados e payloads explícitos.
6. Extraia componentes quando houver repetição verdadeira.

## Para Inertia

- Normalize props antes de inicializar `useForm`.
- Preserve nomes de campos alinhados ao controller/FormRequest.
- Trate listas aninhadas com componentes pequenos e previsíveis.
- Quando editar um item, carregue o registro e reapresente a forma original sem mutação acidental.

## Sinais De Atenção

- `useEffect` para derivar estado puro.
- Props demais no componente raiz.
- Formulários que montam payload implícito demais.
- Componentes reutilizáveis que escondem o contrato de dados.
