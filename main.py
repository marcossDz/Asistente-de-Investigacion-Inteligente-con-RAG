"""
Punto de entrada principal para el Asistente de Investigación Inteligente.
Inicia el servidor FastAPI.
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Crear aplicación FastAPI
app = FastAPI(
    title="Asistente de Investigación Inteligente",
    description="API para el Asistente de Investigación basado en RAG",
    version="0.1.0",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, restringir a orígenes específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta básica para verificar que el servidor está funcionando
@app.get("/")
async def root():
    return {
        "message": "Asistente de Investigación Inteligente API",
        "status": "online",
        "version": "0.1.0"
    }

# Importar y registrar rutas de la API (se implementará más adelante)
# from app.api.routes import router as api_router
# app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)