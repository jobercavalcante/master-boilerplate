---
name: laravel-inertia-feature
description: Implemente features full-stack em Laravel + Inertia React no projeto reconstruído. Use quando criar ou alterar CRUDs, models, migrations, controllers, routes, páginas React/Inertia, formulários, tabelas, relacionamentos Eloquent, ou fluxos que atravessam backend e frontend em `projeto-moderno`.
---

# Laravel Inertia Feature

Use este skill para entregar uma feature coerente de ponta a ponta na stack `Laravel + Inertia + React`.

## Workflow

1. Leia o mínimo de specs e código necessário.
2. Modele banco e Eloquent antes da interface.
3. Crie ou ajuste migration, model, relationships, FormRequests, controller e routes.
4. Passe para Inertia somente os dados que a página usa.
5. Crie páginas em `resources/js/Pages/<Domain>` e componentes reutilizáveis em `Partials` quando houver repetição real.
6. Use `useForm` para formulários Inertia e preserve payloads claros para o backend.
7. Adicione testes feature para persistência, validação e props Inertia relevantes.
8. Rode build e testes antes de finalizar.

## Convenções

- Código app: `projeto-moderno/`.
- Models em `app/Models`.
- Controllers em `app/Http/Controllers`.
- FormRequests em `app/Http/Requests/<Domain>`.
- Páginas Inertia em `resources/js/Pages/<Domain>`.
- Componentes locais da feature em `resources/js/Pages/<Domain>/Partials`.
- Use relações Eloquent nomeadas no idioma do domínio quando já estabelecido no projeto.

## Frontend

- Reuse componentes existentes em `resources/js/Components` e layouts existentes.
- Evite textos explicativos sobre como usar a tela; construa controles claros.
- Mantenha formulários densos, profissionais e previsíveis.
- Para edição, normalize dados recebidos do backend antes de inicializar `useForm`.
- Para arrays aninhados, componentes devem receber `value`, `errors`, `onChange`.

## Backend

- Controllers orquestram: request validado, transação, models/services, redirect/Inertia response.
- Validação fica em FormRequests quando não for trivial.
- Use transação quando salvar entidade principal e relações.
- Preserve Global Scopes multi-tenant existentes.
- Não invente comportamento que a spec não peça; sinalize lacunas.

## Verificação

```powershell
php artisan migrate --force
php artisan test --filter=<Feature>
composer test
npm run build
```
