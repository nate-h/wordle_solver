def get_lines(file_name) -> list[str]:
    with open(file_name) as f:
        data = f.read().split()
    return data


words = get_lines("./data/valid_words.txt")
answers = get_lines("./data/valid_words.txt")

t = 0
