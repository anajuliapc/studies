# Solution to HackerRank's problem: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(not year % 4 and (year % 100 or not year % 400)):
        leap = True
    return leap

year = int(input())
print(is_leap(year))
