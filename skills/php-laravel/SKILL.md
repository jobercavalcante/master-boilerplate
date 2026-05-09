---
name: php-laravel
description: Disciplina para trabalhar em codebases Laravel com controllers finos, FormRequests, Eloquent, feature tests e verificação de qualidade. Use quando o usuário pedir implementação, refatoração, validação, rotas, models, migrations, Inertia, multi-tenant, testes ou ajustes de arquitetura em projetos Laravel.
---

# PHP Laravel

Use este skill para mudanças em Laravel com foco em disciplina, previsibilidade e testes.

## Diretrizes

1. Leia o código existente antes de editar.
2. Prefira `FormRequest` para validação e autorização HTTP.
3. Mantenha controllers como orquestradores.
4. Prefira relações Eloquent e transações para persistência de domínio.
5. Preserve scopes de tenant e outras regras globais já existentes.
6. Evite lazy loading em fluxo de desenvolvimento quando possível.
7. Valide o contrato Inertia entre controller e página React.

## Boas práticas

- Use `declare(strict_types=1)` em novos arquivos PHP quando o projeto já seguir esse padrão.
- Extraia regras repetidas para classes ou métodos compartilhados.
- Prefira feature tests cobrindo o caminho feliz e um caso importante de erro.
- Rode `php artisan route:list`, `php artisan test` e `vendor\bin\pint --test` quando a mudança tocar HTTP ou modelagem.

## Sinais Para Usar

- `store`/`update` com `validate()` inline.
- Controllers com muita regra de negócio.
- Mudanças em migrations, models, relations, scopes ou Inertia pages.
- Ajustes em projetos Laravel com multi-tenant, auth, roles ou auditoria.
