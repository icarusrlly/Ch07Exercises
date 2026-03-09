def uses_none(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

print(uses_none('banana', 'xyz'))
print(uses_none('apple', 'efg'))
print(uses_none("grape", "fgh"))