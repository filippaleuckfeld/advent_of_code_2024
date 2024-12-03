def can_be_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def main():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        
        multiplications = []
        for line in lines: 
           while line != "":
            multiplication = []
            if line[:4] == "mul(":
                line = line[4:]
                index = line.find(",")
                possible_int = line[:index]
                if can_be_int(possible_int):
                    multiplication.append(int(possible_int))
                    line = line[index+1:]
                    index = line.find(")")
                    if can_be_int(line[:index]):
                        multiplication.append(int(line[:index]))
                        line = line[index:]
                        multiplications.append(multiplication)
            else:
                line = line[1:]
        
        sum = 0
        for multiplication in multiplications:
            sum += multiplication[0] * multiplication[1]
        print(sum)
        
                    
                    
                


            
                                    
                        
                    
                    
if __name__ == "__main__":
    main()