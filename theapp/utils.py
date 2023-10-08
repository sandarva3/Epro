alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
          14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


def encrypt_text(text):
    conversion = []
    for char in text:
        if char.isspace():
            conversion.append('_')
        elif char.isalpha():
            index = alphabet.index(char.lower())
            conversion.append(str(number[index]))
        else:
            conversion.append(char)
    return (' '.join(conversion))


def decrypt_text(numbers):
    output = []
    number_list = numbers.split()  # Split the input into individual numbers
    for num in number_list:
        if num.isdigit() and 1 <= int(num) <= 26:
            output.append(alphabet[int(num) - 1])
        elif num == '_':
            output.append(' ')
        else:
            output.append(num)
    return ''.join(output)
