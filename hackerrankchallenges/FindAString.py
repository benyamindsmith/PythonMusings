import re

def count_substring(string , sub_string):

    index=[]

    for i in range(len(string)):
        if string.startswith(sub_string,i):
            index.append(i)

    return len(index)


   

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
