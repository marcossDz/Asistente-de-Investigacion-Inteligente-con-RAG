"""
Módulo para procesamiento de documentos.
Extrae texto y divide en chunks.
"""
from typing import List
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from app.config import CHUNK_SIZE, CHUNK_OVERLAP

def load_document(file_path: str) -> List[Document]:
    """Carga documentos desde diferentes fuentes."""
    if file_path.startswith('http://') or file_path.startswith('https://'):
        loader = WebBaseLoader(file_path)  # Sin headers
        return loader.load()
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"El archivo {file_path} no existe")
    if file_path.suffix.lower() == '.pdf':
        loader = PyPDFLoader(str(file_path))
        return loader.load()
    elif file_path.suffix.lower() in ['.txt', '.md']:
        loader = TextLoader(str(file_path), encoding="utf-8")
        return loader.load()
    elif file_path.suffix.lower() == '.csv':
        loader = CSVLoader(str(file_path), encoding="utf-8")
        return loader.load()
    else:
        raise ValueError(f"Formato no soportado: {file_path.suffix}")

def split_documents(documents: List[Document]) -> List[Document]:
    """Divide documentos en fragmentos según configuración."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )
    return text_splitter.split_documents(documents)

def process_document(file_path: str) -> List[Document]:
    """Procesa un documento y lo divide en chunks."""
    documents = load_document(file_path)
    return split_documents(documents)