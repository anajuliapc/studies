# Solution for HackerRank problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arrset = set(arr) # turn into set to remove duplicates
    arrset.remove(max(arrset)) # remove max value
    print(max(arrset)) # next max value is the runner up score
