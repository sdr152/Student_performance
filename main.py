import json
import os

NUM_STUDENTS = 1000
SUBJECTS = ['math', 'science', 'history', 'english', 'geography']

def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    #print('1--', base_path)
    #print('2--', file_path)
    #print('3--', path)

    try:
        with open(path, 'r') as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

def average_student_mark(student_list):
    count = 0
    acu_grade = 0
    for student in student_list:
        for sb in SUBJECTS:
            gr = student[sb]
            acu_grade += gr
            count += 1
    print(f"Average Student Grade: {acu_grade/count}")

def hardest_subject(student_list):
    lowest_grade = 100
    subject = None

    for sub in SUBJECTS:
        count, acu_grade = 0, 0
        for student in student_list:
            grade = student[sub]
            acu_grade += grade
            count += 1
        average = acu_grade / count
        if average < lowest_grade:
                lowest_grade = average
                subject = sub
    print(f"Hardest Subject: {subject}")

def easiest_subject(student_list):
    highest_grade = 0
    subject = None

    for sub in SUBJECTS:
        count, acu_grade = 0, 0
        for student in student_list:
            grade = student[sub]
            acu_grade += grade
            count += 1
        average = acu_grade / count
        if average > highest_grade:
            highest_grade = average
            subject = sub
    print(f"Easiest Subject: {subject}")

def best_performing_grade(student_list):
    highest_grade = 0
    best_Grade = None    
    for i in range(1,9):
        acu_grade, count = 0, 0
        for student in student_list:
            if student['grade'] == i:
                for sub in SUBJECTS:
                    grade = student[sub]
                    acu_grade += grade
                    count += 1
        average = acu_grade / count
        if average > highest_grade:
            highest_grade = average
            best_Grade = i
    print(f"Best Performing Grade: {best_Grade}")

def worst_performing_grade(student_list):
    lowest_grade = 100
    worst_Grade = None
    for i in range(1, 9):
        acu_grade, count = 0, 0
        for student in student_list:
            if student['grade'] == i:
                for sub in SUBJECTS:
                    grade = student[sub]
                    acu_grade += grade
                    count += 1
        average = acu_grade / count
        if average < lowest_grade:
            lowest_grade = average
            worst_Grade = i
    print(f"Worst Performing Grade: {worst_Grade}")                

def best_student_id(student_list):
    highest_grade = 0
    id = None

    for student in student_list:
        acu_grade, count = 0, 0
        for sub in SUBJECTS:
            grade = student[sub] 
            acu_grade += grade
            count += 1
        average = acu_grade / count
        if average > highest_grade:
            highest_grade = average
            id = student['id']
    print(f"Best student ID: {id}")

def worst_student_id(student_list):
    lowest_grade = 100
    id = None

    for student in student_list:
        acu_grade, count = 0, 0
        for sub in SUBJECTS:
            grade = student[sub] 
            acu_grade += grade
            count += 1
        average = acu_grade / count
        if average < lowest_grade:
            lowest_grade = average
            id = student['id']
    print(f"Worst student ID: {id}")

def main():
    students_lst = []
    for i in range(1000):
        rc = load_report_card('students', i)
        students_lst.append(rc)
    
    # 1
    average_student_mark(students_lst)

    # 2
    hardest_subject(students_lst)

    # 3 
    easiest_subject(students_lst)

    # 4
    best_performing_grade(students_lst)

    # 5
    worst_performing_grade(students_lst)
    
    #6
    best_student_id(students_lst)

    #7
    worst_student_id(students_lst)
if __name__ == '__main__':
    main()