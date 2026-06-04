students_db =[]

while True:
    print('\n--- Student Database ---')
    print('1.add student 2. view all 3. search 4. exit')
    choice = input('choice: ').strip()

    if choice == '1':
        name = input('Name: ')
        marks = []
        for sub in ['Math', 'Science', 'English']:
            m = float(input(f'{sub} marks: '))
            marks.append(m)
        avg = sum(marks) / len(marks)
        students_db.append({'name': name, 'marks': marks, 'average': avg})
        print(f'{name} added . average {avg:.2f}')

    elif choice == '2':
        if not students_db:
            print('No students in database.')
        else:
            students_db.sort(key=lambda x: x['average'], reverse=True)
            for idx, student in enumerate(students_db, 1):
                print(f"{idx}. {student['name']:15} Avg: {student['average']:.2f}")

    elif choice == '3':
        search = input('Enter name: ').strip().lower()
        found = [s for s in students_db if s['name'].lower() == search]
        print(f'Found {len(found)} result(s):')
        for s in found:
            print(f"{s['name']:15} Marks: {s['marks']} Avg: {s['average']:.2f}")
    
    elif choice == '4':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Try again.')