from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user_router import router as user_router
from routers.product_router import router as product_router

app = FastAPI(
    title="API REST 2026",
    description="API desarrollada con FastAPI y PostgreSQL aplicando arquitectura en 5 capas",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Incluir los routers
app.include_router(user_router)
app.include_router(product_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"mensaje": "Bienvenido a la API REST de FastAPI"}