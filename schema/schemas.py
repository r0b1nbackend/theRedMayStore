def individual_serial(book) -> dict:
    return {
        "id":str(book["_id"]),
        "book":book["book"],
        "author":book["author"],
        "description":book["description"],
        "price":book["price"],
        "isHave":book["isHave"]
    }


def list_serial(books) -> list:
    return [individual_serial(books) for book in books]