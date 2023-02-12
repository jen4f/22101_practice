def main():
    # asks user for file name
    file_name = input("Enter file name: ")
    # displays file name
    print("The file name is", get_name(file_name))
    # display sum of file values
    print("The sum of all values in the file is", format(get_sum(file_name), ".2f"))
    # displays number of lines in file
    print("The total number of lines in the file is", get_n_lines(file_name))
    # displays average value per line
    file_mean = get_sum(file_name)/get_n_lines(file_name)
    print("The mean value per line in the file is", format(file_mean, ".2f"))
    # displays number of positive values, negative values, and zeros
    print("The file contains", get_pnz(file_name))
    # displays maximum and minimum value in file
    print("In this file,", get_max_min(file_name))

# function to get the file name
def get_name(file):
    # remember to use f-strings this way to display file name
    return f"{file}" 

# function to calculate the sum
def get_sum(file):
    file_sum = 0
    with open(f"{file}", "r") as infile:
        for line in infile:
            file_sum += float(line.strip())
    return file_sum

# function to calculate the number of lines
def get_n_lines(file):
    n_lines = 0
    with open(f"{file}", "r") as infile:
        for line in infile:
            n_lines += 1
    return n_lines

# function to calculate the number of positive, negative and zero numbers
def get_pnz(file):
    n_positive = 0
    n_negative = 0
    n_zero = 0
    with open(f"{file}", "r") as infile:
        for line in infile:
            line = float(line.strip())
            if line > 0:
                n_positive += 1
            elif line < 0:
                n_negative += 1
            else:
                n_zero += 1
    return f"{n_positive} positive numbers, {n_negative} negative numbers, {n_zero} zeros."

# function to calculate the maximum and minimum value
def get_max_min(file):
    max_num = None
    min_num = None
    n_line = 0
    with open(file, "r") as infile:
        for line in infile:
            n_line += 1
            line = float(line.strip())
            if n_line == 1:
                max_num = line
                min_num = line
            elif n_line > 1 and line > max_num:
                max_num = line
            elif n_line > 1 and line < min_num:
                min_num = line
            else:
                pass
    return (f"{max_num} is the maximum number, {min_num} is the minimum number.")

main()