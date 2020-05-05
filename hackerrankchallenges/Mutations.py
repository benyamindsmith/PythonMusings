def mutate_string(string, position, character):

    new_string = list(string)
    
    new_string[position] = character

    new_string=''.join(new_string)

    return new_string


if __name__ == '__main__':
