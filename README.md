# Encurtador de URL

Um sistema simples de encurtamento de URLs construído com Flask, com interface moderna em preto e branco.

## Funcionalidades

- Encurtar URLs longas em códigos curtos
- Sistema de autenticação de usuários
- Interface responsiva e moderna
- Copiar links para a área de transferência
- Compartilhar links
- Gerenciar links pessoais

## Como executar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente (opcional):
```bash
export SECRET_KEY="sua-chave-secreta"
export DATABASE_URL="sqlite:///app.db"
```

3. Execute as migrações do banco de dados:
```bash
flask db init
flask db migrate
flask db upgrade
```

4. Execute a aplicação:
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## Estrutura do projeto

```
encurtadorurl/
├── app.py                 # Arquivo principal da aplicação
├── db.py                  # Configuração do banco de dados
├── requirements.txt       # Dependências Python
├── models/
│   ├── link.py           # Modelo Link
│   └── user.py           # Modelo User
├── routes/
│   ├── link_routes.py    # Rotas principais
│   └── oauth.py          # Rotas de autenticação
├── templates/            # Templates HTML
│   ├── index.html
│   ├── login.html
│   └── register.html
├── static/               # Arquivos estáticos
│   └── styles.css
└── utils/
    └── utils.py          # Utilitários
```

## Tecnologias utilizadas

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de dados**: SQLite (pode ser alterado para PostgreSQL/MySQL)
- **Estilo**: Design minimalista em preto e branco
