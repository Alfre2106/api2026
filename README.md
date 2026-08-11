

```markdown
# 🚀 API REST 2026 - FastAPI & PostgreSQL

API RESTful desarrollada con **FastAPI** y **PostgreSQL**, implementando una **arquitectura limpia modular de 5 capas** para garantizar la escalabilidad, mantenibilidad y desacoplamiento del código.

---

## 🛠️ Tecnologías Utilizadas

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Base de Datos:** [PostgreSQL](https://www.postgresql.org/)
* **Driver BD:** `psycopg2-binary`
* **Validación de Datos:** [Pydantic](https://docs.pydantic.dev/)
* **Servidor ASGI:** `Uvicorn`
* **Variables de Entorno:** `python-dotenv`

---

## 🏗️ Arquitectura en 5 Capas

El proyecto está estructurado bajo el principio de separación de responsabilidades:

```text
api2026/
├── config/           # Capa 1: Configuración global y variables de entorno (.env)
├── database/         # Capa 2: Manejo de conexiones a PostgreSQL
├── schemas/          # Capa 3: Modelos Pydantic para validación de entrada/salida
├── services/         # Capa 4: Lógica de negocio y consultas SQL desacopladas
├── routers/          # Capa 5: Rutas HTTP, códigos de estado (200, 201, 204, 404)
├── main.py           # Punto de entrada de la aplicación y middleware CORS
├── .env              # Credenciales y datos sensibles de conexión
├── .gitignore        # Exclusión de archivos sensibles para Git
└── requirements.txt  # Dependencias del proyecto

```

---

## 📑 Endpoints de la API

La API cuenta con módulos CRUD completos para **Usuarios** y **Productos**:

### 👤 Módulo Usuarios (`/usuarios`)

| Método | Ruta | Descripción | Estado HTTP |
| --- | --- | --- | --- |
| **GET** | `/usuarios/` | Obtener todos los usuarios | `200 OK` |
| **GET** | `/usuarios/{id}` | Obtener usuario por ID | `200 OK` / `404 Not Found` |
| **POST** | `/usuarios/` | Crear un nuevo usuario | `201 Created` |
| **PUT** | `/usuarios/{id}` | Actualizar un usuario | `200 OK` / `404 Not Found` |
| **DELETE** | `/usuarios/{id}` | Eliminar un usuario | `204 No Content` / `404 Not Found` |

### 📦 Módulo Productos (`/productos`)

| Método | Ruta | Descripción | Estado HTTP |
| --- | --- | --- | --- |
| **GET** | `/productos/` | Obtener todos los productos | `200 OK` |
| **GET** | `/productos/{id}` | Obtener producto por ID | `200 OK` / `404 Not Found` |
| **POST** | `/productos/` | Crear un nuevo producto | `201 Created` |
| **PUT** | `/productos/{id}` | Actualizar un producto | `200 OK` / `404 Not Found` |
| **DELETE** | `/productos/{id}` | Eliminar un producto | `204 No Content` / `404 Not Found` |

---

## ⚙️ Instalación y Configuración Local

1. **Clonar el repositorio:**
```bash
git clone [https://github.com/Alfre2106/api2026.git](https://github.com/Alfre2106/api2026.git)
cd api2026

```


2. **Crear e inicializar el entorno virtual:**
```bash
python -m venv myvenv
# En Windows:
.\myvenv\Scripts\activate

```


3. **Instalar dependencias:**
```bash
pip install -r requirements.txt

```


4. **Configurar el archivo `.env`:**
Crea un archivo `.env` en la raíz con las credenciales de tu base de datos:
```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_NAME=api_db

```


5. **Iniciar el servidor de desarrollo:**
```bash
uvicorn main:app --reload

```


6. **Probar la API:**
Abre tu navegador e ingresa a `http://127.0.0.1:8000/docs` para interactuar con la documentación generada por Swagger UI.

```





