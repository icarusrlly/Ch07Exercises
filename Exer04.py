def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True


def check_word(word, available, required):
    if len(word) <= 3:
        return False
    return uses_only(word, available) and (required in word)

print(check_word('color', 'acdlort', 'r'))
print(check_word('ratatat', 'acdlort', 'r'))
print(check_word('rat', 'acdlort', 'r'))
print(check_word('told', 'acdlort', 'r'))
print(check_word('bee', 'acdlort', 'r'))
