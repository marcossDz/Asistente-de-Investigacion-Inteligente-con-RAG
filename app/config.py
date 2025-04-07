"""
Configuración general del proyecto.
Centraliza parámetros, rutas y otras configuraciones.
"""
import os
from pathlib import Path

# Directorios base
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Asegurar que los directorios existan
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# Configuración de embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384  # Dimensión para el modelo predeterminado

# Configuración de la base de vectores
VECTOR_DB_PATH = PROCESSED_DATA_DIR / "chroma_db"

# Configuración de chunking para documentos
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Número de resultados a recuperar en búsquedas
TOP_K_RESULTS = 5