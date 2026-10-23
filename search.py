"""
Модуль для пошуку товарів за категоріями.
"""

CATEGORIES = ["електроніка", "одяг", "книги", "дім"]

def search_by_category(category):
    # Пошук товарів за заданою категорією з урахуванням пробілів та регістру
    if not category:
        return []
    
    clean_category = category.strip().lower()
    result = []
    
    for cat in CATEGORIES:
        if cat.lower() == clean_category:
            result.append(cat)
            
    return result
