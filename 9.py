def student_record(filename):
    file = open(filename, 'a')
    roll = input("Enter roll number : ")
    name = input("Enter Name : ")
    address = input("Enter address : ")
    file.write("\nroll_no " + roll + " name " + name + " address " + address)
    file.close()

def student_read(filename):
    file = open(filename)
    lines = file.read().split('\n')
    for line in lines[1:]:
        words = line.split()
        roll_no = words[1]
        name = words[3] + ' ' + words[4]
        address = ' '.join(words[6:])
        print('\nRoll no. : ' + roll_no + ' , Name : ' + name + ' , Address : ' + address)
    file.close()

def student_search(filename):
    file = open(filename)
    lines = file.read().split('\n')
    roll_no = input("Enter roll no.: ")
    for line in lines[1:]:
        if line.split()[1] == roll_no:
            words = line.split()
            name = words[3] + ' ' + words[4]
            address = ' '.join(words[6:])
            print('\nRoll no.: ' + roll_no + ' , Name: ' + name + ' , Address: ' + address)
            break
    file.close()
choice = ''
while choice != '4':
    print('1. Record Student, 2. Read Students, 3. Search Student, 4. Quit')
    choice = input('')
    if choice == '1':
        student_record('student.txt')
    elif choice == '2':
        student_read('student.txt')
    elif choice == '3':
        student_search('student.txt')
exit()
