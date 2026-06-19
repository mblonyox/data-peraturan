exception_words = ['di', 'ke', 'dari', 'dan', 'atau', 'untuk', 'yang', 'pada', 'tentang', 'atas']

def titlecase(text: str) -> str:
    words = text.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or word.lower() not in exception_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())

    return ' '.join(result)