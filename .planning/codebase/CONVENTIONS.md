# Convenções

* **Git Branching:** Sem commits diretos na `main` ou `master`. Sempre use `feature/nome-da-feature` ou `fix/nome-do-bug`.
* **Commits:** Atômicos e descritivos.
* **Controllers:** Extremamente limpos (Thin Controllers).
* **Validação:** Exclusivamente via FormRequests, sem validações `inline`.
* **Interface UI:** Design premium inspirado em Emil Kowalski (glassmorphism, micro-interações, cores suaves, transições ricas). Nada de interfaces genéricas.
* **Qualidade:** "Verificação antes da conclusão" (testes e build devem passar antes de finalizar a task).
