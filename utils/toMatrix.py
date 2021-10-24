with open("matrix.txt") as file_in:
    lines = []
    mat = []
          
    for line in file_in:
        for i in range(7436): 
            lines.append(line)
        mat[i] = lines

print(mat)