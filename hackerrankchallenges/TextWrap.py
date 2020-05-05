import textwrap

def wrap(string, max_width):
    parsed = textwrap.wrap(string, max_width)
    x = ""
    for i in parsed:

        x += i+"\n"
    return x



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
