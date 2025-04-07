from app.core.document_processor import process_document

file_path = "data/raw/test.txt"  # O "data/raw/test.pdf" si usas un PDF
docs = process_document(file_path)
for i, doc in enumerate(docs):
    print(f"Chunk {i}: {doc.page_content[:50]}... (longitud: {len(doc.page_content)})")