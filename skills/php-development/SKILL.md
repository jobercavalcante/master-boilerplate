---
name: php-development
description: Melhores práticas para desenvolvimento PHP incluindo PSR-12, type hints, tratamento de erros e segurança. Use quando trabalhar com código PHP.
license: MIT
---

# Desenvolvimento PHP - Melhores Práticas

Esta habilidade fornece orientações especializadas para desenvolvimento PHP seguindo padrões modernos e melhores práticas de segurança.

## 🎯 Padrões de Código (PSR-12)

### Estrutura de Arquivos
- Use `namespace` em todas as classes
- Um arquivo por classe/interface
- Nomes de arquivos em PascalCase
- Estrutura de pastas seguindo PSR-4

### Type Hints e Retorno
```php
// ✅ Correto
public function processUser(int $userId, string $name): User
{
    // implementação
}

// ❌ Evite
public function processUser($userId, $name)
{
    // implementação
}
```

### Early Returns (Fail Fast)
```php
// ✅ Preferível
public function validateUser(int $userId): bool
{
    if ($userId <= 0) {
        return false;
    }

    if (!$this->userExists($userId)) {
        return false;
    }

    return true;
}

// ❌ Evite aninhamento profundo
public function validateUser(int $userId): bool
{
    if ($userId > 0) {
        if ($this->userExists($userId)) {
            return true;
        }
    }
    return false;
}
```

## 🔒 Segurança

### Prepared Statements (Proteção contra SQL Injection)
```php
// ✅ Seguro
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$email]);

// ❌ Vulnerável
$query = "SELECT * FROM users WHERE email = '$email'";
$pdo->query($query);
```

### Validação e Sanitização
- Sempre valide entrada do usuário
- Use `filter_var()` para validação
- Sanitize dados antes de exibir
- Verifique permissões antes de operações

### Proteção CSRF (GLPI)
```php
// ✅ CORRETO para GLPI — Session::checkCSRF() lança exceção se token inválido
Session::checkCSRF($_POST);

// ✅ Em templates Twig — usar a função nativa csrf_token()
// <input type="hidden" name="_glpi_csrf_token" value="{{ csrf_token() }}">

// ❌ ERRADO — verificação manual não usa o mecanismo do GLPI
// if (!isset($_POST['csrf_token']) || $_POST['csrf_token'] !== $_SESSION['csrf_token']) {
//     die('Token CSRF inválido');
// }
```

## ⚡ Performance

### Otimização de Queries
- Evite N+1 queries
- Use JOIN ao invés de múltiplas consultas
- Implemente cache quando apropriado
- Use índices adequados

```php
// ❌ N+1 Query
$users = $db->query("SELECT * FROM users");
foreach ($users as $user) {
    $posts = $db->query("SELECT * FROM posts WHERE user_id = " . $user['id']);
}

// ✅ Otimizado com JOIN
$query = "
    SELECT users.*, posts.*
    FROM users
    LEFT JOIN posts ON users.id = posts.user_id
";
```

### Cache
- Use cache para dados frequentemente acessados
- Considere Redis/Memcached para cache distribuído
- Implemente cache de OPcode (OPcache)

## 🏗️ Arquitetura

### Princípios SOLID
- **S**ingle Responsibility: Uma classe, uma responsabilidade
- **O**pen/Closed: Aberto para extensão, fechado para modificação
- **L**iskov Substitution: Subclasses substituíveis por classes base
- **I**nterface Segregation: Interfaces específicas são melhores
- **D**ependency Inversion: Dependa de abstrações, não implementações

### Padrão Repository
```php
interface UserRepositoryInterface
{
    public function find(int $id): ?User;
    public function save(User $user): void;
    public function delete(int $id): void;
}

class UserRepository implements UserRepositoryInterface
{
    // implementação
}
```

## 📝 Tratamento de Erros

### Exceções Estruturadas
```php
class UserNotFoundException extends Exception
{
    public function __construct(int $userId)
    {
        parent::__construct("Usuário {$userId} não encontrado");
    }
}

try {
    $user = $userRepository->find($userId);
} catch (UserNotFoundException $e) {
    // tratamento específico
} catch (Exception $e) {
    // tratamento genérico
}
```

### Logging Adequado
- Use níveis apropriados (ERROR, WARNING, INFO, DEBUG)
- Não logue dados sensíveis
- Estruture logs para facilitar análise

## 🧪 Testes

### PHPUnit Básico
```php
class UserServiceTest extends TestCase
{
    public function testCreateUser(): void
    {
        $service = new UserService();
        $user = $service->createUser('john@example.com', 'John Doe');

        $this->assertInstanceOf(User::class, $user);
        $this->assertEquals('john@example.com', $user->getEmail());
    }
}
```

### Cobertura de Testes
- Teste métodos públicos
- Teste casos de erro
- Mantenha cobertura > 80%
- Use mocks para dependências externas

## 📚 Como Usar Esta Habilidade

Ao trabalhar com desenvolvimento PHP:

- "Aplique as melhores práticas PSR-12 neste código"
- "Refatore para usar prepared statements"
- "Implemente early returns neste método"
- "Adicione validação de segurança nesta função"
- "Otimize esta query para evitar N+1"

A habilidade irá guiá-lo através de padrões PHP modernos e garantir código seguro, performático e manutenível.