"""
Módulo para interacción con la base de datos vectorial.
Maneja la indexación y búsqueda de documentos.
"""
from typing import List
import os

from langchain.schema import Document
from langchain_chroma import Chroma
from langchain.embeddings.base import Embeddings

from app.config import VECTOR_DB_PATH
from app.core.embeddings import DocumentEmbeddings


class VectorStore:
    """Clase para gestionar la base de datos vectorial."""
    
    def __init__(self):
        """Inicializa la conexión con la base de datos vectorial."""
        self.embeddings = DocumentEmbeddings().embeddings
        os.makedirs(VECTOR_DB_PATH, exist_ok=True)
        
        self.db = Chroma(
            persist_directory=str(VECTOR_DB_PATH),
            embedding_function=self.embeddings
        )
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        Añade documentos a la base de datos vectorial.
        
        Args:
            documents: Lista de documentos a añadir
        """
        if documents:
            self.db.add_documents(documents)
    
    def search(self, query: str, k: int = 5) -> List[Document]:
        """
        Busca documentos similares a una consulta.
        
        Args:
            query: Texto de consulta
            k: Número de resultados a devolver
            
        Returns:
            Lista de documentos similares
        """
        return self.db.similarity_search(query, k=k)