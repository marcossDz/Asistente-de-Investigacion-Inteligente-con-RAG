from app.core.document_processor import process_document
from app.db.vector_store import VectorStore
import shutil
from app.config import VECTOR_DB_PATH

# Limpia la base de datos
shutil.rmtree(VECTOR_DB_PATH, ignore_errors=True)

file_path = "data/raw/test.csv"
docs = process_document(file_path)
vector_store = VectorStore()
vector_store.add_documents(docs)
results = vector_store.search("prueba", k=3)
for i, res in enumerate(results):
    print(f"Resultado {i}: {res.page_content[:50]}...")