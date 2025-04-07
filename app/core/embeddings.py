"""
Módulo para gestión de embeddings.
Convierte texto en vectores.
"""
from typing import List
from langchain_huggingface import HuggingFaceEmbeddings 
from app.config import EMBEDDING_MODEL

class DocumentEmbeddings:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
    
    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self.embeddings.embed_documents(texts)
    
    def get_query_embedding(self, text: str) -> List[float]:
        return self.embeddings.embed_query(text)