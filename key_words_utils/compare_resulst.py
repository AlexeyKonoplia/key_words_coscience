from sklearn.metrics.pairwise import cosine_similarity

def compare_results(original: str, generated: str, embedding_function) -> str:
    original_embedding = embedding_function(original)
    generated_embedding = embedding_function(generated)
    
    original_embedding = [original_embedding]
    generated_embedding = [generated_embedding]
    return float(cosine_similarity(original_embedding, generated_embedding)[0, 0])