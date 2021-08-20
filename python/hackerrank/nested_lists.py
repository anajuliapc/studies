# Solution to https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    # Lambda function to get list of min records in list
    min_record = lambda arr: [item for item in arr
                              if item[1] == min(item[1] for item in arr)]

    # Get min records from the list that already removed the lowest value
    second_lowest_score = min_record([record for record in records
                                      if record not in min_record(records)])

    for name in sorted([name for [name, score] in second_lowest_score]):
         print(name) 

