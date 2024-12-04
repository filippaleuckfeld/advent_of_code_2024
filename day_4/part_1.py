import numpy as np

def extract_diagonals(matrix):
    diagonals = []
    for offset in range(-matrix.shape[0] + 1, matrix.shape[1]):
        diagonal = np.diagonal(matrix, offset=offset)
        if len(diagonal) >= 4:
            diagonals.append(''.join(diagonal))
    return diagonals
            
def extract_rows(matrix):
    return [''.join(row) for row in matrix]

def find_occurance_of_xmas(main_diagonals, anti_diagonals, horizontals, verticals):    
    count = 0
    for line in main_diagonals + anti_diagonals + horizontals + verticals:
        count += line.count("XMAS")
        reversed_line = reversed(line)
        count += ''.join(reversed_line).count("XMAS")
    
    return count

def main():
    with open("input.txt", 'r') as file:
        matrix_2d = [list(row.strip()) for row in file]

        matrix = np.array(matrix_2d, dtype=str)
    
    main_diagonals = extract_diagonals(matrix)
    anti_diagonals = extract_diagonals(np.fliplr(matrix))
    horizontals = extract_rows(matrix)
    verticals = extract_rows(matrix.T)
    
    print(find_occurance_of_xmas(main_diagonals, anti_diagonals, horizontals, verticals))


if __name__ == "__main__":
    main()