CATEGORIES = ["електроніка", "одяг", "книги", "дім"]

def search_by_category(category):
    # Пошук товарів за заданою категорією
    if not category:
        return []
    
    result = []
    for cat in CATEGORIES:
        if cat.lower() == category.lower():
            result.append(cat)
            
    return result
