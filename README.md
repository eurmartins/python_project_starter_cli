# Python CLI Starter

Uma ferramenta CLI para gerar projetos Python com templates pré-configurados para FastAPI, Flask e Django, seguindo as melhores práticas da comunidade.

## Funcionalidades

- **Templates modernos**: Estruturas de projeto baseadas nas melhores práticas de cada framework
- **Configuração de banco de dados**: Suporte a SQLite, PostgreSQL e MySQL com configuração automática
- **Bibliotecas adicionais**: Permite adicionar dependências extras ao projeto
- **Interativo**: Interface amigável para configuração

## Instalação

1. Clone ou baixe este repositório
2. Navegue até a pasta do projeto
3. Execute o script:

```bash
python main.py
```

## Uso

### Modo Interativo (Recomendado)

Execute sem argumentos para usar o modo interativo:

```bash
python main.py
```

Será solicitado:
- Framework (fastapi, flask, django)
- Nome do projeto
- Banco de dados (sqlite, postgres, mysql)
- Se escolher postgres/mysql: usuário, senha, host e porta
- Bibliotecas adicionais (opcional)

### Modo com Argumentos

```bash
python main.py --framework fastapi --name meu_projeto --db postgres --libs requests --libs httpx
```

#### Opções Disponíveis

- `--framework`: Escolha do framework (fastapi, flask, django)
- `--name`: Nome do projeto
- `--db`: Banco de dados (sqlite, postgres, mysql)
- `--libs`: Bibliotecas adicionais (pode ser usado múltiplas vezes)

## Estruturas dos Templates

### Django

```
django/
├── manage.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
└── apps/
    └── core/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py
tests/
└── test_health.py
```

### FastAPI

```
fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── example.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── example.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── example.py
│   └── services/
│       ├── __init__.py
│       └── example_service.py
├── tests/
│   ├── __init__.py
│   └── test_example.py
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

### Flask

```
flask/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── hello.py
│   ├── models/
│   │   ├── __init__.py
│   └── extensions.py
├── tests/
│   ├── __init__.py
│   └── test_hello.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

## Configuração de Banco de Dados

### SQLite (Padrão)
- Não requer configuração adicional
- Arquivo local: `db.sqlite3` (Django) ou `app.db` (Flask)

### PostgreSQL/MySQL
- Dependências adicionadas automaticamente
- Configuração via variáveis de ambiente
- Para Django: configura `settings/base.py`
- Para FastAPI/Flask: adiciona `DATABASE_URL` ao `.env.example`

## Próximos Passos Após Criar o Projeto

1. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar ambiente**:
   - Copie `.env.example` para `.env`
   - Ajuste as variáveis conforme necessário

3. **Executar o projeto**:

   **Django**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

   **FastAPI**:
   ```bash
   uvicorn app.main:app --reload
   ```

   **Flask**:
   ```bash
   export FLASK_APP=app
   flask run
   ```

4. **Executar testes**:
   ```bash
   pytest
   ```

## Contribuição

Sinta-se à vontade para contribuir com melhorias nos templates ou novas funcionalidades!

## Licença

Este projeto é open source. Use conforme necessário.