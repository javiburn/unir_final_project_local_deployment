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
   ```

2. Crea el archivo de entorno:

    ```bash
    cp .example_env .env
    ```

Edita el .env con tu configuración.

3. Construye e inicia los servicios:

    ```bash
    docker-compose up --build -d
    ```

4. Verifica que esté funcionando:

    ```bash
    docker-compose ps
    ```

### 🌐 Acceso a la aplicación
- Aplicación Flask: http://localhost:5000

- PostgreSQL:

    ```bash
    docker exec -it flask-postgres-docker-db-1 psql -U tu_usuario_db tu_base_de_datos
    ```

### 🧪 Ejecutar tests
Los tests están en el directorio tests/ con cobertura del 80%+.

Ejecuta los tests con:
    ```
    docker-compose exec flask-app pytest -v --cov=app --cov-report=term-missing
    ```

### 📂 Estructura del proyecto
    ```
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
    ```

### 🔧 Configuración
Variables de entorno principales (en .env):
    ```
    FLASK_ENV=development
    DATABASE_URL=postgresql://usuario:contraseña@db:5432/nombre_db
    SECRET_KEY=tu-clave-secreta
    ```

## 👥 Desarrollo Colaborativo

### 🪵 Estrategia de Ramas (Git Flow)

Para el trabajo en equipo seguimos este flujo de trabajo:
    ```mermaid
    gitGraph
        commit
        branch develop
        checkout develop
        commit
        branch feature/nueva_funcionalidad
        commit
        commit
        checkout develop
        merge feature/nueva_funcionalidad
        checkout main
        merge develop
## Ramas Principales

### `main` (producción)
- Versión estable del proyecto
- Solo se actualiza mediante Pull Requests aprobados
- Se usa `rebase` para mantener historial limpio

### `develop` (pre-producción)
- Integración de features completadas
- Entorno de pruebas avanzadas
- Paso previo obligatorio antes de `main`

## Ramas de Trabajo
### `feature/<nombre>`
- Desarrollo de nuevas funcionalidades
- Nomenclatura: `feature/login`, `feature/payment-integration`
- Se mergean a `develop` cuando están completas

## 🔁 Flujo de Trabajo

1. **Crear rama desde develop**:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/mi_feature
2. **Trabajar localmente y hacer commits**:
   ```bash
   git add .
    git commit -m "feat: añade sistema de autenticación"
3. **Sincronizar con cambios remotos**:
    ```bash
    git fetch origin
    git merge origin/develop
4. **Publicar cambios**:
    ```bash
    git push origin feature/mi_feature
5. **Crear Pull Request a develop**:
- Revisión de código obligatoria
- Tests automáticos deben pasar
- Aprobación por al menos 1 miembro
6. **Promoción a producción:**:
- Merge desde develop a main via PR
- Tag con versión semántica (v1.0.0)
## 📌 Reglas Clave

- ❌ **Nunca hacer push directo** a `main` o `develop`  
  *(Siempre usar Pull Requests)*

- ⚠️ **Resolver conflictos** en la rama de origen  
  *(Nunca en `main` o `develop`)*

- 🔄 **Actualizar localmente** al menos 1 vez al día  
  *(Ejecutar `git pull origin develop` regularmente)*

- ✍️ **Commits descriptivos**  
  ```bash
  git commit -m "feat: añadir sistema de autenticación"
  git commit -m "fix: corregir error en validación de formulario"

## 🔧 Conventional Commits

Utilizamos [Conventional Commits](https://www.conventionalcommits.org) para mensajes estandarizados:
    ```bash
    git commit -m "feat: añadir autenticación con Google"
    git commit -m "fix: resolver error en cálculo de totales"
    git commit -m "docs: actualizar guía de instalación"
## Conventional Commits

### Tipos permitidos de commits:

| Tipo       | Descripción                              | Ejemplo                          |
|------------|------------------------------------------|----------------------------------|
| `feat`     | Nueva funcionalidad                     | `feat: añadir login con Google`  |
| `fix`      | Corrección de errores                   | `fix: reparar cálculo de IVA`    |
| `docs`     | Cambios en documentación                | `docs: actualizar README.md`     |
| `style`    | Formato (sin afectar código)            | `style: ajustar indentación`     |
| `refactor` | Mejoras de código existente             | `refactor: optimizar consultas`  |
| `test`     | Añadir/mejorar tests                    | `test: añadir pruebas API`       |
| `chore`    | Tareas de mantenimiento                 | `chore: actualizar dependencias` |

## 📋 Requisitos para Pull Requests

### 📝 Descripción obligatoria
```markdown
## Qué cambia
- [Descripción técnica clara de las modificaciones]

## Por qué
- [Explicación del propósito/necesidad del cambio]

## Cómo probar
1. [Pasos específicos para verificar]
2. [Casos de prueba clave]
3. [Configuraciones especiales requeridas]
### 📈 Monitorización
Ver uso de recursos:
    ```
    docker stats
    ```
### 🚨 Solución de problemas
Conflictos de puertos: Verifica que los puertos 5000 (Flask) y 5432 (Postgres) estén libres

Problemas con la base de datos: Ejecuta docker-compose down -v para reiniciar volúmenes

Cambios en dependencias: Reconstruye con docker-compose up --build