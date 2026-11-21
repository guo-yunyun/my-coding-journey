def count_vowels(text):
    vowels = 'aeiouAEIOU'
    result = {}
    for char in text:
        if char in vowels:
            result[char] = result.get(char, 0) + 1
    return result


text = 'hello world'
print(count_vowels(text))
