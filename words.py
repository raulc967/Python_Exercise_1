def print_upper_words(words):
    for word in words:
        print(word.upper)

def print_upper_e(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper)

def print_upper(words, starts_with):
    for word in words:
        for char in starts_with:
            print(word.upper())
