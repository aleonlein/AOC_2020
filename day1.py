

def evaluate_no_list(x):
    inner_idx = 0
    outer_idx = -1
    for i in range(len(x)//2):
        try:
            if (x[inner_idx] + x[outer_idx]) > 2020:
                outer_idx -= 1
                continue
            elif (x[inner_idx] + x[outer_idx]) == 2020:
                print(x[inner_idx], x[outer_idx])
                return
            else: 
                inner_idx += 1
        except IndexError:
            print("No values match")

x = [1721, 979, 366, 299, 675, 1456]
x.sort()
evaluate_no_list(x)