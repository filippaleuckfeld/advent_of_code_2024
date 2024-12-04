import numpy as np
import re

def find_mas(matrix, targets = ("MAS", "SAM"), is_anti_diagonal=False):
    results = []
    for offset in range(-matrix.shape[0] + 1, matrix.shape[1]):
        diagonal = np.diagonal(matrix, offset=offset)
        
        if len(diagonal) >= 3:
            diagonal_str = ''.join(diagonal)
            
            matches = [match for target in targets for match in re.finditer(target, diagonal_str)]
            if matches:
                for match in matches:
                    start_idx = match.start()
                    for i in range(start_idx, start_idx + len(match.group())):
                        if diagonal[i] == 'A':
                            row = i if offset >= 0 else i - offset
                            col = i + offset if offset >= 0 else i
                            
                            if is_anti_diagonal:
                                col = matrix.shape[1] - 1 - col
                                
                            results.append((row, col))
            
    return results

def main():
    with open("input.txt", 'r') as file:
        matrix_2d = [list(row.strip()) for row in file]

        matrix = np.array(matrix_2d, dtype=str)
    
    main_diagonal = find_mas(matrix)
    anti_diagonal = find_mas(np.fliplr(matrix), is_anti_diagonal=True)
    
    common_elements = set(main_diagonal) & set(anti_diagonal)

    count = len(common_elements)
    print(count)

if __name__ == "__main__":
    main()