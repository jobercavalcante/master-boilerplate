# Estrutura do Código

A estrutura seguirá o padrão default do Laravel 12+ com modificações para React/Inertia:

* `app/Http/Controllers/`: Thin Controllers.
* `app/Http/Requests/`: Validações.
* `app/Services/` ou `app/Actions/`: Lógica de negócio.
* `resources/js/`: Aplicação React (Pages, Components, Layouts).
* `tests/Feature/`: Feature Tests.
* `tests/Browser/`: Testes E2E (Dusk).
* `boilerplate/`: Arquivos de configuração do agente IA (não é código do app, mas controla como ele é gerado).
