def character_frequency(string):
    string = string.lower()
    frequency = {}
    for char in string:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

if __name__ == "__main__":
    print(character_frequency("Hello, World!"))
