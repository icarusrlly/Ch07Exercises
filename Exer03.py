def uses_all(word, letters):
    for char in letters:
        if char not in word:
            return False
    return True

print(uses_all('banana', 'ban'))
print(uses_all('apple', 'api'))
print(uses_all('grape', 'pro'))