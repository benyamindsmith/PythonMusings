def split_and_join(line):
    
    update = line.split(sep=" ")
    
    return '-'.join(update)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
