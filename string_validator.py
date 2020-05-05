if __name__ == '__main__':
    s = input()

def string_validator(string):
    alnum_count=[]
    alpha_count=[]
    digits=[]
    lowercase=[]
    uppercase=[]
    for i in string:
        if i.isalnum():
            alnum_count.append(i)
        if i.isalpha():
            alpha_count.append(i)
        if i.isdigit():
            digits.append(i)
        if i.islower():
            lowercase.append(i)
        if i.isupper():
            uppercase.append(i)

    tests=[alnum_count,
           alpha_count,
           digits,
           lowercase,
           uppercase]
    for j in tests:
        if len(j)!=0:
            print(True)
        else:
            print(False)

string_validator(s)
