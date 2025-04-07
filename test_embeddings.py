from app.core.embeddings import DocumentEmbeddings

embedder = DocumentEmbeddings()
texts = ["Hola mundo", "Este es un test"]
embeddings = embedder.get_embeddings(texts)
query_embedding = embedder.get_query_embedding("¿Qué es esto?")

print(f"Embeddings generados: {len(embeddings)} textos")
print(f"Longitud del primer embedding: {len(embeddings[0])}")
print(f"Longitud del embedding de consulta: {len(query_embedding)}")