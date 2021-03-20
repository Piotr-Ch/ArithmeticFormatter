def arithmetic_arranger(problems, x=False):
    #check the no of problems; limit is five
    if len(problems) > 5:
        print('Error: Too many problems.')
        quit()

    list_of_blocks = []
    for block in problems:
        if '*' in block or '/' in block:
            print('Operators must be + or -')
            quit()
        list_of_blocks.append(block.split())

    for element in list_of_blocks:
        if not element[0].isdigit() or not element[2].isdigit():
            print('Numbers must only contain digits.')
            quit()
        if len(element[0]) > 4 or len(element[2]) > 4:
            print('Numbers cannot be more than four digits.')
            quit()

    first_row = []
    second_row = []
    third_row = []
    fourth_row = []

    for item in list_of_blocks:
        if len(item[0]) <= len(item[2]):
            second_row.append(item[1] +' '+ item[2])
            first_row.append(' '*len(item[2]) + item[0])
            third_row.append('-'*(len(item[1] +' '+ item[2])))
            if item[1] == '+':
                sum_length = len(str(int(item[0]) + int(item[2])))
                if sum_length > len(item[2]):
                    fourth_row.append(" " + str(int(item[0]) + int(item[2])))
                else:
                    fourth_row.append("  " + str(int(item[0]) + int(item[2])))
            if item[1] == '-':
                diff_length = len(str(int(item[0]) - int(item[2])))
                if diff_length < len(item[2]):
                    fourth_row.append("  " + str(int(item[0]) - int(item[2])))
                else:
                    fourth_row.append(" " + str(int(item[0]) - int(item[2])))

        else:
            first_row.append('  '+ item[0])
            second_row.append(item[1] +' '*(len(item[0])+ 2 - len(item[1]) - len(item[2]))+ item[2])
            third_row.append('-' * (len(item[0]) + 2))
            if item[1] == '+':
                sum_length = len(str(int(item[0]) + int(item[2])))
                if sum_length > len(item[0]):
                    fourth_row.append(' '+str(int(item[0]) + int(item[2])))
                else:
                    fourth_row.append('  ' + str(int(item[0]) + int(item[2])))
            if item[1] == '-':
                diff_length = len(str(int(item[0]) - int(item[2])))
                if diff_length < len(item[0]):
                    fourth_row.append('   ' + str(int(item[0]) - int(item[2])))
                else:
                    fourth_row.append('  ' + str(int(item[0]) - int(item[2])))
    if x:
        print('    '.join(first_row) + '\n' + '    '.join(second_row) + '\n' + '    '.join(third_row) +
            '\n' + '    '.join(fourth_row))
    else:
        print('    '.join(first_row) + '\n' + '    '.join(second_row) + '\n' + '    '.join(third_row))

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 - 49"], True)






