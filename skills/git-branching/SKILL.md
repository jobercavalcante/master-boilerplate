---
name: git-branching
description: Regra IMUTÁVEL sobre o fluxo Git no projeto O Projeto. Nunca commitar diretamente na branch master. Sempre criar feature branches para qualquer implementação nova.
---

# Git Branching (Regra Imutável)

Esta é uma regra **inviolável** no projeto O Projeto.

## Regra de Ouro
**Nunca commitar diretamente na branch `master`.** Toda implementação nova deve ser feita em uma branch dedicada.

## Workflow Obrigatório

### 1. Antes de iniciar qualquer implementação:
```bash
git checkout master
git pull origin master        # (se houver remote)
git checkout -b <tipo>/<nome>
```

### 2. Nomenclatura de branches:
| Tipo | Uso | Exemplo |
|------|-----|---------|
| `feature/` | Nova funcionalidade | `feature/impersonation` |
| `fix/` | Correção de bug | `fix/login-redirect` |
| `refactor/` | Refatoração sem mudança funcional | `refactor/thin-controllers` |
| `docs/` | Apenas documentação | `docs/e2e-tests-update` |
| `chore/` | Manutenção, tooling, configs | `chore/tailwind-upgrade` |

### 3. Convenções de nomenclatura:
- Usar **kebab-case** (palavras separadas por `-`).
- Ser **descritivo e curto** (máximo 3-4 palavras após o prefixo).
- Usar **português** para consistência com o projeto.

### 4. Durante o desenvolvimento e Commits:
- **REGRA DE COMMIT (MANUAL)**: NUNCA faça commits automáticos sem aprovação prévia. Após concluir uma implementação ou correção, você DEVE parar, exibir ao usuário o que foi alterado e pedir autorização para commitar.
- O commit na feature branch só pode ser executado APÓS o usuário avaliar e permitir explicitamente ("pode commitar", "ok", "faz o commit").
- Seguir o padrão de commits convencionais (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`).

### 5. Ao finalizar a Feature:
- Verificar qualidade (testes, build, lint) conforme skill `verification-before-completion`.
- Informar ao usuário que a branch está pronta para merge.
- Aguardar aprovação explícita do usuário para fazer merge.

### 6. Merge na Master (Aprovação do Usuário):
Quando o usuário indicar aprovação com frases como:
- "está ok", "tá ok", "ok", "pode mergear", "merge", "manda", "aprovo", "beleza", "pode ir", "manda bala", "lgtm", "ship it"

Executar imediatamente:
```bash
git checkout master
git merge <branch-atual> --no-ff -m "merge: <branch-atual> → master"
git branch -d <branch-atual>
```

> **`--no-ff`** garante que o histórico preserve a existência da branch, mesmo que seja fast-forward.
> Após o merge, deletar a branch local para manter o repositório limpo.

### 7. Merge com Conflito:
Se o merge gerar conflitos:
1. **NÃO resolver automaticamente** — listar os arquivos em conflito.
2. Perguntar ao usuário como proceder.
3. Após resolução, commitar o merge.

## O que é PROIBIDO:
- `git commit` sem autorização prévia e avaliação do usuário.
- `git commit` enquanto estiver na branch `master`.
- `git merge <branch>` na master sem aprovação final do usuário.
- `git push --force` em qualquer branch.

## O que é PERMITIDO:
- Criar branches a partir de outras branches (quando necessário).
- Realizar alterações de código (mas sempre solicitar avaliação antes de commitar).
- Fazer `docs/` commits diretamente na master **apenas** para correções de typo em documentação do Reversa (`_reversa_sdd/`, `.reversa/`), mas **ainda assim com aprovação prévia**.

## Checklist de Início de Tarefa
Antes de tocar em qualquer arquivo de código:
1. ✅ Verificar branch atual (`git branch --show-current`)
2. ✅ Se estiver na `master`, criar branch com `git checkout -b <tipo>/<nome>`
3. ✅ Confirmar ao usuário: "Trabalhando na branch `<nome>`"
