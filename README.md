# Aplicación Flask con PostgreSQL - Dockerizada

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Aplicación Flask con base de datos PostgreSQL en contenedores Docker, lista para producción. Incluye tests con cobertura del 80%+ usando pytest.

## 🚀 Inicio rápido

### Requisitos
- Docker 20.10+
- Docker Compose 2.0+

### Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/javiburn/unir_final_project_local_deployment.git
   cd flask-postgres-docker

2. Crea el archivo de entorno:

    ```bash
    cp .example_env .env

Edita el .env con tu configuración.

3. Construye e inicia los servicios:

    ```bash
    docker-compose up --build -d

4. Verifica que esté funcionando:

    ```bash
    docker-compose ps

### 🌐 Acceso a la aplicación
- Aplicación Flask: http://localhost:5000

- PostgreSQL:

    ```bash
    docker exec -it flask-postgres-docker-db-1 psql -U tu_usuario_db tu_base_de_datos

### 🧪 Ejecutar tests
Los tests están en el directorio tests/ con cobertura del 80%+.

Ejecuta los tests con:
    ```bash
    docker-compose exec flask-app pytest -v --cov=app --cov-report=term-missing

### 📂 Estructura del proyecto
    ```bash
    ├── app/
    │   ├── __init__.py          # Factoría de la aplicación
    │   ├── config.py            # Configuración
    │   ├── models.py            # Modelos de la base de datos
    │   ├── routes.py            # Rutas de la aplicación
    ├── tests/
    │   ├── test_config.py       # Tests de configuración
    │   ├── test_models.py       # Tests de modelos
    │   └── test_routes.py       # Tests de rutas
    ├── Dockerfile               # Contenedor de Flask
    ├── docker-compose.yml       # Orquestación
    ├── .example_env             # Plantilla de variables
    ├── manage.sh                # Script para inicializar el proceso
    ├── requirements.txt         # Dependencias Python
    └── manage.py                # Entrypoint Python

### 🔧 Configuración
Variables de entorno principales (en .env):
    ```ini
FLASK_ENV=development
DATABASE_URL=postgresql://usuario:contraseña@db:5432/nombre_db
SECRET_KEY=tu-clave-secreta

### 📈 Monitorización
Ver uso de recursos:
    ```bash
    docker stats
### 🚨 Solución de problemas
Conflictos de puertos: Verifica que los puertos 5000 (Flask) y 5432 (Postgres) estén libres

Problemas con la base de datos: Ejecuta docker-compose down -v para reiniciar volúmenes

Cambios en dependencias: Reconstruye con docker-compose up --build