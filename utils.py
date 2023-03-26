def load_words(file_name) -> list[str]:
    with open(file_name) as f:
        data = f.read().split()
    return data


words = load_words("./data/valid_words.txt")
answers = load_words("./data/valid_words.txt")

t = 0
