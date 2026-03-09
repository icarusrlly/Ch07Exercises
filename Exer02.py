def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True

print(uses_only('banana', 'ban'))
print(uses_only('apple', 'apl'))
print(uses_only('grape', 'gra'))