# FastAPI Modular Template

Template base para construir APIs modernas utilizando FastAPI, SQLAlchemy Async y Alembic, siguiendo una arquitectura modular basada en servicios y repositorios.

Este proyecto busca proporcionar una estructura escalable, limpia y reutilizable para acelerar el desarrollo de nuevos proyectos backend con Python.

---

# Features

* FastAPI
* SQLAlchemy Async
* Alembic
* Arquitectura modular
* Patrón Repository
* Patrón Service
* Paginación reutilizable
* Configuración mediante variables de entorno
* Preparado para PostgreSQL o SQLite
* Tipado moderno con Python 3.12
* Separación clara de responsabilidades

---

# Versions

| Technology | Version |
| ---------- | ------- |
| Python     | 3.12.12 |
| FastAPI    | 0.136.3 |

---

# Project Structure

```txt
fastapi-modular-template/
├── app/
│   ├── common/
│   │   ├── schemas/
│   │   │   └── pagination.py
│   │   ├── helpers.py
│   │   └── pagination.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── models/
│   │   └── __init__.py
│   │
│   ├── modules/
│   │   └── products/
│   │       ├── models.py
│   │       ├── repository.py
│   │       ├── routers.py
│   │       ├── schemas.py
│   │       └── services.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── migrations/
├── env.example
├── .python-version
├── alembic.ini
└── requirements.txt
```

---

# Architecture Explanation

## app/

Contiene toda la lógica principal de la aplicación.

---

## app/common/

Contiene lógica reutilizable y compartida entre múltiples módulos.

Ejemplos:

* paginación
* helpers
* schemas genéricos
* utilidades compartidas

---

## app/core/

Contiene configuraciones globales del proyecto.

### config.py

Maneja las variables de entorno y configuraciones globales.

### database.py

Configura:

* SQLAlchemy Async Engine
* AsyncSession
* Base declarativa
* Dependencia `get_db`

---

## app/models/

Este directorio es utilizado para importar todos los modelos SQLAlchemy del proyecto.

Esto es importante para que Alembic pueda detectar automáticamente los cambios en los modelos al generar migraciones.

Ejemplo:

```python
from app.modules.products.models import Product
```

Luego Alembic importa este módulo para registrar todos los modelos en `Base.metadata`.

---

## app/modules/

Contiene los módulos funcionales de la aplicación.

Cada módulo mantiene su propia lógica separada.

Ejemplo:

```txt
products/
├── models.py
├── repository.py
├── routers.py
├── schemas.py
└── services.py
```

### models.py

Define los modelos SQLAlchemy.

### schemas.py

Define los schemas Pydantic.

### repository.py

Contiene la lógica de acceso a base de datos.

### services.py

Contiene la lógica de negocio.

### routers.py

Define los endpoints HTTP utilizando FastAPI.

---

## app/**init**.py

Permite iniciar el proyecto de forma más sencilla utilizando:

```bash
fastapi dev app
```

Contenido:

```python
from .main import app

if "__main__" == __name__:
    app()
```

---

## migrations/

Contiene:

* configuración de Alembic
* migraciones de base de datos

---

# Installation

## Clone repository

```bash
git clone <repository_url>
cd fastapi-modular-template
```

---

## Create virtual environment

### Linux / Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Crear un archivo `.env` utilizando `env.example` como referencia.

Ejemplo:

```env
DATABASE_URL=sqlite+aiosqlite:///./app.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Generate Secret Keys

## URL Safe Secret

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## Hex Secret

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

# Database Migrations

## Create migration

```bash
alembic revision --autogenerate -m "create products table"
```

---

## Run migrations

```bash
alembic upgrade head
```

---

# Run Development Server

```bash
fastapi dev
```

O también:

```bash
uvicorn app:app --reload
```

---

# API Documentation

Swagger UI:

```txt
http://127.0.0.1:8000/docs
```

ReDoc:

```txt
http://127.0.0.1:8000/redoc
```

---

# Future Improvements

* JWT Authentication
* Role Based Access Control
* Docker support
* Testing setup
* CI/CD
* Redis
* Celery
* WebSockets

---

# License

MIT
