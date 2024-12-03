def is_increasing(lst):
    if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
        return True

def is_decreasing(lst):
    if all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
        return True

def is_differing_by_one_two_three(lst):
    if all(abs(lst[i] - lst[i + 1]) in {1, 2, 3} for i in range(len(lst) - 1)):
        return True
    
def remove_element(lst, index):
    return lst[:index] + lst[index + 1:]

def main():
    safe = 0
    with open("input.txt", 'r') as file:
        for line in file:
            report = [int(elem) for elem in line.split()]
            if (is_increasing(report) or is_decreasing(report)) and is_differing_by_one_two_three(report):
                safe += 1
                continue
            else:
                for index in range(len(report)):
                    new_report = remove_element(report, index)
                    if (is_increasing(new_report) or is_decreasing(new_report)) and is_differing_by_one_two_three(new_report):
                        safe += 1
                        break
                    
    print(safe)
                    
                
if __name__ == "__main__":
    main()
