def movieEntity(item) -> dict:
    return{
        "idM": str(item["_id"]),
        "src": item["src"],
        "genero": item["genero"],
        "clasif": item["clasif"],
        "year": item["year"],
        "duracion": item["duracion"],
        "comments": item["comments"]
    }

def moviesEntity(entity) -> list:
    return [movieEntity(item) for item in entity]