import string


def decipher(text, number):
    new_string = ''
    for letter in text:
        if letter in alphabets_list:
            index = alphabets_list.index(letter)
            new_index = (index + number)%26
            new_letter = alphabets_list[new_index]
            new_string += new_letter
        else:
            new_string += letter 
    print(new_string)
    
alphabets = string.ascii_uppercase
alphabets_list = list(alphabets)

plain_text = input('Enter text to be decrypted. ').upper()
shift_number = int(input('Enter shift number. '))

decipher(plain_text, shift_number)