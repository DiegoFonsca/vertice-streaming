# Vértice — Plataforma de Streaming

Uma plataforma de streaming desenvolvida como projeto de portfólio Full Stack, com identidade visual própria e foco no aprendizado de desenvolvimento web com Python.

## 🌐 Acesse o projeto

**Aplicação online:** https://vertice-streaming.onrender.com

## Sobre o projeto

O **Vértice** é uma aplicação web inspirada nas plataformas modernas de streaming. O projeto foi desenvolvido para colocar em prática conceitos de desenvolvimento Front-end e Back-end, integração com banco de dados, autenticação de usuários e organização de aplicações Flask.

## Funcionalidades

- Cadastro de usuários.
- Login e logout.
- Armazenamento seguro de senhas utilizando hash.
- Proteção de formulários contra ataques CSRF.
- Catálogo de filmes.
- Pesquisa de títulos no catálogo.
- Adição e remoção de filmes dos favoritos.
- Página pessoal Minha Lista.
- Integração com banco de dados PostgreSQL.

## Tecnologias utilizadas

**Back-end**

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

**Front-end**

- HTML5
- CSS3
- JavaScript

**Banco de dados**

- PostgreSQL

**Segurança**

- Werkzeug Password Hashing
- Flask-WTF e proteção CSRF
- Variáveis de ambiente para configurações sensíveis

## Executar o projeto localmente

### 1. Pré-requisitos

- Python instalado.
- PostgreSQL instalado e em execução.
- Git instalado.

### 2. Clonar o repositório

```bash
git clone https://github.com/DiegoFonsca/vertice-streaming.git
cd vertice-streaming
```

### 3. Criar e ativar o ambiente virtual

No Windows, execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando os nomes de variáveis esperados pela aplicação:

```env
SECRET_KEY=sua_chave_secreta
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=vertice
```

Crie previamente o banco de dados PostgreSQL e configure as credenciais de acordo com seu ambiente.

**Importante:** o arquivo `.env` contém informações privadas e não deve ser enviado ao GitHub.

### 6. Criar as tabelas

```bash
python criar_tabelas.py
```

### 7. Executar a aplicação

```bash
python run.py
```

Acesse no navegador:

http://127.0.0.1:5000

## Status do projeto

O Vértice está em desenvolvimento. Novas funcionalidades, páginas de reprodução de conteúdo e melhorias visuais poderão ser adicionadas ao longo da evolução do projeto.

## Autor

**Diego Fonseca**

Desenvolvedor em formação, estudando Python, desenvolvimento web e arquitetura de aplicações Full Stack.

- GitHub: [DiegoFonsca](https://github.com/DiegoFonsca)
- Repositório: [vertice-streaming](https://github.com/DiegoFonsca/vertice-streaming)
