---
name: laravel-database-performance
description: Diretrizes estritas para otimização de banco de dados, motores de armazenamento (InnoDB) e indexação de consultas.
---

# Skill: Laravel Database Performance

Este projeto exige foco absoluto na **performance de banco de dados e escalabilidade**, considerando que a arquitetura Multi-Tenant com Single Database vai concentrar um grande volume de dados na mesma instância.

## 1. Engine de Banco de Dados (InnoDB)
- O MySQL/MariaDB moderno deve operar **exclusivamente com o InnoDB**.
- O Laravel 12 já delega a criação de tabelas para o engine padrão do banco (que é InnoDB). Você **não precisa** definir `$table->engine = 'InnoDB'` manualmente, mas tenha a garantia mental de que transações ACID, chaves estrangeiras e row-level locking dependem dessa premissa.

## 2. Índices são Obrigatórios
Jamais crie um campo que será usado ativamente em cláusulas `WHERE`, `ORDER BY` ou no campo de "Pesquisa" de tabelas frontend sem adicionar um índice.
- **Chaves Estrangeiras**: Sempre indexe chaves estrangeiras (ex: `$table->uuid('tenant_id')->index()`).
- **Campos de Busca Textual**: Nomes, documentos (CPF/CNPJ), e-mails, títulos. Aplique `$table->index('nome_do_campo')`.
- **Status/Booleanos**: Se você filtra listas ativamente pelo `status` ou `ativo`, adicione índices (frequentemente índices compostos com o `tenant_id` funcionam melhor: `$table->index(['tenant_id', 'status'])`).

## 3. Restrições de Unicidade (`unique()`)
A restrição `$table->unique()` atua automaticamente como um índice de alta performance. 
Em bancos Multi-Tenant, a maioria das garantias de unicidade devem ser acopladas ao inquilino: `$table->unique(['tenant_id', 'ecad'])`.

## 4. Evitando Table Scans
Ao refatorar queries Eloquent em Services ou Controllers (Thin Controllers), observe se a combinação de colunas buscada está coberta por um índice. Em rotinas críticas de relatório ou dashboard, a ausência de índice causará `Full Table Scan`, o que é inaceitável.
