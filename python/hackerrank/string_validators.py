# Solution for: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def has_alphanumeric(string):
    if(len(string) == 1):
        return string.isalnum()

    if(string.isalnum()):
        return True

    center = len(string)//2
    s1 = string[0:center]
    print(s1)
    s2 = string[center+1:-1]
    print(s2)

    return has_alphanumeric(s1) or has_alphanumeric(s2)


def has_alphabetic(string):
    pass
    if(len(string) == 1):
        return string.isalpha()

    if(string.isalpha()):
        return True

    s1 = string[0:len(string)//2]
    s2 = string[(len(string)//2)+1:-1]

    return has_alphabetic(s1) or has_alphabetic(s2)

def has_digit(string):
    pass

def has_lower(string):
    pass

def has_upper(string):
    pass

if __name__ == '__main__':
    s = input()
    
    print(has_alphanumeric(s))
