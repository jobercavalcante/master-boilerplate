# Arquitetura

* **Modelo:** Monolito Moderno
* **Comunicação Backend/Frontend:** Inertia.js (Sem necessidade de API RESTful tradicional para o frontend)
* **Arquitetura de Software:** Clean Architecture Simplificada
  * **Thin Controllers:** Apenas orquestração de HTTP.
  * **FormRequests:** Para validação de dados.
  * **Services/Actions:** Para regras de negócio e lógica complexa.
* **Diagramas:** Baseados no modelo C4 presentes no diretório `system-design/`.
