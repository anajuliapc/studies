# Solution to HackerRank's problem: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def print_int(n):
    if(n == 1):
        return 1
    return str(print_int(n-1))+str(n)

if __name__ == '__main__':
    n = int(input())
    print(print_int(n))
