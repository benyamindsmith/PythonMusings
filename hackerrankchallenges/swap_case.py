def swap_case(s):
    new_string=''
    for letter in s:
        if letter.isupper():
            new_string += letter.lower()
        elif letter.islower():
            new_string += letter.capitalize()
        else:
            new_string += letter

    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
