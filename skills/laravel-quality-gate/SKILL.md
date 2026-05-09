---
name: laravel-quality-gate
description: Execute checagens de qualidade para mudanças Laravel/Inertia. Use antes de finalizar tarefas, commits ou PRs nesta stack, especialmente após alterar migrations, models, controllers, FormRequests, páginas React/Inertia, testes, assets Vite, ou plano Reversa.
---

# Laravel Quality Gate

Use este skill para validar uma mudança antes de entregar ou commitar.

## Escolha De Checks

- Backend PHP alterado: `php artisan test --filter=<teste-focado>`, depois `composer test`.
- Frontend alterado: `npm run build`.
- Migrations alteradas: `php artisan migrate --force` e `php artisan migrate:status`.
- Rotas/controllers alterados: `php artisan route:list`.
- PHP novo ou editado: `vendor\bin\pint --test <arquivos>`.
- Fluxo Inertia alterado: teste feature com `assertInertia`.

## Ordem Recomendada

1. Rode o teste mais próximo da mudança.
2. Corrija falhas de contrato ou validação.
3. Rode build se houver React/Vite.
4. Rode suíte completa.
5. Rode Pint em modo `--test`.
6. Verifique `git status --short`.

## Comandos Base

```powershell
php artisan test --filter=<NomeDoTeste>
composer test
npm run build
vendor\bin\pint --test app tests database
php artisan migrate:status
```

## Interpretação

- Falha de Vite manifest normalmente significa build ausente ou entrypoint quebrado.
- Falha de `assertInertia` costuma indicar props desalinhadas entre controller e página.
- Falha de tenant em teste normalmente pede usuário com `tenant_id` e model criado dentro do mesmo tenant.
- Warnings de depreciação do Vite não bloqueiam entrega, mas devem ser mencionados se persistirem.

## Entrega

Informe checks executados e resultado. Se algum check não foi executado, diga por quê.
