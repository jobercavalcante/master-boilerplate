---
name: laravel-formrequests
description: Refatore validações inline de controllers Laravel para FormRequest classes. Use quando controllers tiverem `$request->validate(...)`, regras duplicadas de store/update, autorização simples por request, ou quando o usuário pedir controllers mais magros, separação de camadas, request validation, FormRequest, Store/Update requests, ou clean controllers em Laravel/Inertia.
---

# Laravel FormRequests

Use este skill para mover validação e autorização HTTP para `app/Http/Requests`, mantendo controllers focados em orquestrar fluxo, persistência e resposta.

## Workflow

1. Identifique o controller e os métodos com validação inline.
2. Crie requests específicos por intenção, normalmente `StoreXRequest` e `UpdateXRequest`.
3. Mova regras para `rules()` e autorização para `authorize()`.
4. Use `$request->validated()` no controller.
5. Se store/update compartilham regras, extraia um método privado no request base apenas quando reduzir duplicação real.
6. Preserve nomes de campos e payloads existentes; não renomeie contrato frontend sem atualizar Inertia e testes.
7. Atualize testes para cobrir pelo menos um payload válido e uma validação relevante.

## Padrão Do Projeto

- Aplicação reconstruída fica em `projeto-moderno/`.
- Não altere arquivos do projeto-legado original fora de `projeto-moderno/`, `.reversa/` ou `_reversa_sdd/` quando estiver dentro de fluxo Reversa.
- Prefira FormRequests em `projeto-moderno/app/Http/Requests/<Domain>/`.
- Controllers devem receber requests tipados:

```php
public function store(StoreUsuarioRequest $request): RedirectResponse
{
    $validated = $request->validated();
}
```

## Regras De Validação

- Use regras Laravel nativas quando bastarem.
- Use `Rule::in(...)`, `Rule::exists(...)` e `Rule::unique(...)` para regras que precisam contexto.
- Em update, derive exceções de unicidade ou escopo usando o model route-bound quando existir.
- Para arrays aninhados, mantenha regras explícitas para o array e para cada campo `items.*.campo`.
- Para boolean de formulário React/Inertia, aceite `boolean`.

## Autorização

- Retorne `true` apenas quando a rota já estiver protegida por middleware suficiente.
- Se houver tenant ou ownership claro, valide no `authorize()` ou dependa do route model binding com Global Scope já existente.
- Não coloque persistência, sync de relações ou side effects no FormRequest.

## Verificação

Rode conforme o escopo:

```powershell
php artisan test --filter=<FeatureOuController>
vendor\bin\pint --test app\Http\Controllers app\Http\Requests tests
```

Se a mudança impactar Inertia, rode também:

```powershell
npm run build
```
