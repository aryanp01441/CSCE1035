import csv

def Print_Header():
    print('---------------------------------')
    print('|           Group 3             |')
    print('|          presents             |')
    print('|         FUN with Data         |')
    print('---------------------------------')

def Print_Selection_Menu():
    print('---------------------------------')
    print('| 1. Raw Data                   |')
    print('| 2. Compare Data               |')
    print('| 3. Average                    |')
    print('| 4. Standard Deviation         |')
    print('---------------------------------')

def Data_Library(file_name):
    bool = False

    while bool != True:
        if '.csv' in file_name:
            file = open(file_name)
            file_reader = csv.reader(file)

            header = next(file_reader)
            tmp_header = next(file_reader)

            header_list = []
            header_list.append(str(header[0]))
            header_list.append(str(tmp_header[0]))
            header_list.append(str(tmp_header[1]))

            rows = []

            for row in file_reader:
                rows.append(row)

            file.close()

            tmp_year, tmp_population = map(list, zip(*rows))
            year = []
            population = []

            i = 0
            j = 0

            while i < len(tmp_year):
                year.append(int(tmp_year[i]))
                i += 1

            while j < len(tmp_population):
                population.append(int(tmp_population[j]))
                j += 1

            bool = True

        else:
            file_name = input('Enter file name (ex: file.csv): ')
            bool = False

    return header_list, year, population

def Raw_Data(string):
    list1, list2, list3 = Data_Library(string)
    print('\n  ', list1[0])
    print()
    print('   ', list1[1], ' ->', list1[2])

    i = 0
    while i < len(list2):
        print('       ', list2[i], end='')
        print('     -> ', end=' ')
        print(list3[i])
        i += 1

def Compare_Data(string, string2):
    list1, list2, list3 = Data_Library(string)
    list4, list5, list6 = Data_Library(string2)

    country1 = input('Enter Data 1 name: ')
    country2 = input('Enter Data 2 name: ')

    print('\n              ', list1[0])
    print()
    print('   ', list1[1], ' ->',country1, list1[2], ' ->', country2, list4[2])

    i = 0
    while i < len(list2):
        print('       ', list2[i], end='')
        print('     -> \t', end=' ')
        print(list3[i],'\t-> \t', list6[i])
        i += 1

def Growth_Rate(string):
    list1, list2, list3 = Data_Library(string)

    list = []
    i = 1
    while i <= (len(list) - 1):
        temp = ((list[i] - list[i-1]) / (list[i-1])) * 100
        list.append(temp)
        print(temp)
        i += 1

    print(list)

Print_Header()
print()
Print_Selection_Menu()
print()

user_selection = int(input('Enter choice (9 to quit): '))
file_name = input('Enter file name (ex: file.csv): ')


while user_selection != 9:

    if user_selection == 1:
        Raw_Data(file_name)
        print()

    elif user_selection == 2:
        file_name1 = input('Enter file name (ex: file.csv): ')
        Compare_Data(file_name, file_name1)
        print()

    elif user_selection == 3:
        Growth_Rate(file_name)

    Print_Selection_Menu()
    print()
    user_selection = int(input('Enter choice (9 to quit): '))