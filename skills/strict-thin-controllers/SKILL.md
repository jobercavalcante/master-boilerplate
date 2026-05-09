---
name: strict-thin-controllers
description: Regra IMUTÁVEL sobre a arquitetura dos Controllers no projeto O Projeto. Controllers NUNCA devem ter regras de negócio ou consultas ao banco de dados diretamente (Eloquent Queries).
---

# Strict Thin Controllers (Regra Imutável)

Esta é uma regra **inviolável** no projeto O Projeto.

## Regra de Ouro
**Controllers não devem ter nenhuma regra de negócio nem realizar consultas (queries) diretamente.**

## O que é PROIBIDO em um Controller:
- Usar métodos do Eloquent que acessam o banco de dados diretamente (`User::where(...)`, `Model::with(...)`, `Model::paginate()`, `Model::get()`).
- Escrever regras de negócio, cálculos, ou formatações de dados.
- Fazer lógica condicional de filtro dentro do método do Controller (`$query->when(...)`).

## O que é PERMITIDO:
- Injetar Serviços (`Services`) via construtor ou resolvê-los.
- Repassar parâmetros (ex: `$request->validated()` ou `$request->all()`) para o Serviço.
- Retornar Views (Inertia), Redirects ou JSON formatado.
- Delegar criação, atualização e busca exclusivamente para as classes de Serviço correspondentes.

## Padrão Esperado
Todo Controller deve agir apenas como um "maestro", delegando o trabalho pesado para a camada de Serviço. 

**Exemplo Errado:**
```php
public function index(Request $request) {
    $users = User::with('profile')->paginate(10);
    return Inertia::render('Users/Index', ['users' => $users]);
}
```

**Exemplo Correto:**
```php
public function index(Request $request, UserService $service) {
    $users = $service->getPaginatedUsers($request->all());
    return Inertia::render('Users/Index', ['users' => $users]);
}
```
