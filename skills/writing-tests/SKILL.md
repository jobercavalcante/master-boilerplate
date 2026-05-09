---
name: writing-tests
description: Escreva testes que protegem comportamento real e reduzem regressões. Use quando criar, refatorar ou corrigir código, especialmente em features Laravel, Inertia, controllers, validações, migrations, relacionamentos ou fluxos com risco de quebra.
---

# Writing Tests

Use este skill para criar testes úteis, curtos e alinhados ao comportamento do sistema.

## Diretrizes

1. Teste comportamento, não implementação.
2. Prefira objetos reais e o stack HTTP completo quando o risco for de integração.
3. Comece pelo caso feliz e adicione um caso de erro relevante.
4. Escreva o teste antes do fix quando estiver corrigindo bug.
5. Mantenha os nomes dos testes legíveis e específicos.
6. Use fixtures e factories quando ajudarem a reduzir ruído.

## Para Laravel (Backend e Integração)

- Prefira feature tests para controllers, validação, relações e Inertia.
- Use `assertRedirect`, `assertSessionHasErrors`, `assertDatabaseHas` e `assertInertia` quando fizer sentido.
- Para multi-tenant, crie o usuário e os dados no mesmo tenant do teste.
- Se a mudança tocar frontend Inertia, valide props e componentes da página.

## Testes End-to-End (E2E) com Laravel Dusk

- **É OBRIGATÓRIO** escrever testes E2E usando **Laravel Dusk** (em `tests/Browser/`) para qualquer nova funcionalidade full-stack.
- Todo módulo deve ter um script correspondente espelhando o plano definido em `_reversa_sdd/e2e-tests.md`.
- No ambiente de testes Dusk, lide com o delay do React chamando métodos de espera de estado visual (`waitFor()`, `waitForText()`) antes de interagir.
- Estes testes atuarão como *Quality Gate* e devem passar localmente via `php artisan dusk` antes do encerramento da tarefa.

## Evite

- Mockar demais o que o próprio framework já resolve.
- Cobrir só o caminho feliz quando a mudança é arriscada.
- Testes que replicam o código em vez de proteger o contrato.
