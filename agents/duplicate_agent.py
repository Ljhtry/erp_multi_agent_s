from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

historical_materials = [
    "山地自行车车架",
    "铝合金车架",
    "自行车轮胎26寸",
    "碳纤维车把"
]

embeddings = model.encode(historical_materials)

index = faiss.IndexFlatL2(384)
index.add(np.array(embeddings, dtype=np.float32))

def check_duplicate(material_name):
    query_embedding = model.encode([material_name])

    D, I = index.search(np.array(query_embedding, dtype=np.float32), 1)

    similarity = D[0][0]

    matched_material = historical_materials[I[0][0]]

    return {
        "matched_material": matched_material,
        "distance": float(similarity),
        "possible_duplicate": similarity < 1.0
    }
