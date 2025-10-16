# Jacob Cardon
# CS1400 - MWF - 8:30am

def main():
    """asks user how many rows in pyramid and prints pyramid to terminal"""
    print(make_number_pyramid(int(input("Enter number of desired rows: "))))

def make_number_pyramid(row_count:int):
    """
    Returns number of rows equal row_count in a pyramid.
    example: 1
            2 2
           3 3 3
    """
    result = ""
    first_col = True
    max_len = (len(str(row_count)) * row_count) + (row_count - 1)#length of bottom row
    #constructs each row
    for row in range(row_count+1):
        row_text = ""
        #constructs each column
        for col in range(row):
            #adds space in between numbers
            if not first_col:
                row_text += " "
            first_col = False#ensures only columns in between numbers contains a space
            row_text += str(row)
        beginning_spaces = (max_len // 2 - len(row_text) // 2) * " "
        result += beginning_spaces + row_text + "\n"
        first_col = True
    return result

main()

