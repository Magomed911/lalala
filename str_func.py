def upper_case(string):
    """
    функция возвращает строку в большом регистре
    """
    return string.upper()

def capitalize_words(string):
    """
    Преобразует каждое слово в строке,
    поступившей на вход функции, так,
    чтобы первая буква каждого слова была заглавной.
    """
    return ' '.join(word.capitalize() for word in string.split())