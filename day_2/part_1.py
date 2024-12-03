def is_increasing(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def is_decreasing(lst):
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def check_trend(lst):
    if is_increasing(lst):
        return True
    elif is_decreasing(lst):
        return True
    else:
        return False

def is_differing_by_one_two_three(lst):
    if all(abs(lst[i] - lst[i + 1]) in {1, 2, 3} for i in range(len(lst) - 1)):
        return True

def main():
    safe = 0
    with open("input.txt", 'r') as file:
        for line in file:
            report = [int(elem) for elem in line.split()]
            check_trend(report)
            if check_trend(report) == True:
                if is_differing_by_one_two_three(report) == True:
                    safe += 1

                
    print(safe)
                    
                
if __name__ == "__main__":
    main()