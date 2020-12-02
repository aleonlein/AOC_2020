import requests

def find_the_two_values(x,sum):
    inner_idx = 0
    outer_idx = -1

    for i in range(len(x)):
        try:
            if (x[inner_idx] + x[outer_idx]) > sum:
                outer_idx -= 1
                continue
            elif (x[inner_idx] + x[outer_idx]) == sum:
                print(x[inner_idx], x[outer_idx])
                return x[inner_idx] * x[outer_idx]  
            else: 
                inner_idx += 1
        except IndexError:
            print("No values match")

def find_three_values(array, sum):
    for i in range(len(array)):
        for j in range(len(array)-1):
            j = j + 1
            for k in range(len(array)-2):
                k = k + 2
                # print(i,j,k)
                if (array[i] + array[j] + array[k]) == sum:
                    print(array[i] , array[j] , array[k])
                    return array[i] * array[j] * array[k]


with open(r"C:\Users\Arielle\code\for_fun\AOC_2020\day1_data.txt", 'r') as f:
    array = [[int(x) for x in line.split()][0] for line in f]

# array = [1721,979,366,299,675,1456]
array.sort()
value = find_three_values(array, 2020)
print(value)
