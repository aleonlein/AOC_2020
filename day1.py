import requests

def evaluate_no_list(x):
    inner_idx = 0
    outer_idx = -1
    for i in range(len(x)):
        try:
            if (x[inner_idx] + x[outer_idx]) > 2020:
                outer_idx -= 1
                continue
            elif (x[inner_idx] + x[outer_idx]) == 2020:
                print(x[inner_idx], x[outer_idx])
                return x[inner_idx] * x[outer_idx]  
            else: 
                inner_idx += 1
        except IndexError:
            print("No values match")

with open(r"C:\Users\Arielle\code\for_fun\AOC_2020\day1_data.txt", 'r') as f:
    array = [[int(x) for x in line.split()][0] for line in f]
    
array.sort()
value = evaluate_no_list(array)
print(value)