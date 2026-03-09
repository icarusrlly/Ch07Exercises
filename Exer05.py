def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True

def uses_all(word, required):
    return uses_only(required, word)

print(uses_all('banana', 'bam'))
print(uses_all('apple', 'apl'))
print(uses_all('grape', 'gra'))
