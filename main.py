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
    
def add_student_averages(student_list):    
    for student in student_list:
        acu_grade = 0
        for sb in SUBJECTS:
            gr = student[sb]
            acu_grade += gr
        student['average'] = acu_grade / len(SUBJECTS)
    
def average_student_mark(student_list):
    sum_of_averages = 0
    for student in student_list:
        sum_of_averages += student['average']
    return sum_of_averages / len(student_list)

def get_subject_averages(student_list):
    subject_averages = {subject : 0 for subject in SUBJECTS}

    for student in student_list:
        for subject in SUBJECTS:
            subject_averages[subject] += student[subject]
    
    for subject in subject_averages:
        subject_averages[subject] = subject_averages[subject] / len(student_list)
    
    return subject_averages

def get_grade_level_averages(student_list):
    grade_level_averages = {lvl:[] for lvl in range(1,9)}

    for student in student_list:
        level = student['grade']
        average = student['average']
        grade_level_averages[level].append(average)
    
    for lvl in grade_level_averages:
        grade_level_averages[lvl] = sum(grade_level_averages[lvl]) / len(grade_level_averages[lvl])
    
    return grade_level_averages

def main():
    students_lst = []
    for i in range(NUM_STUDENTS):
        rc = load_report_card('students', i)
        students_lst.append(rc)
    
    # 1
    add_student_averages(students_lst)
    # 2
    average_student_grade = average_student_mark(students_lst)

    # 2
    subject_averages = get_subject_averages(students_lst)
    sorted_subject_averages = sorted(subject_averages.items(), key=lambda x: x[1])
    easiest_subject = sorted_subject_averages[-1][0]
    hardest_subject = sorted_subject_averages[0][0]

    # 3 
    grade_level_averages = get_grade_level_averages(students_lst)
    sorted_grade_level_averages = sorted(grade_level_averages.items(), key=lambda x: x[1])
    best_lvl = sorted_grade_level_averages[-1][0]
    worst_lvl = sorted_grade_level_averages[0][0]

    # 4
    print(students_lst[:2])
    
    students_sorted_by_grade = sorted(students_lst, key=lambda x: x['average'])
    best_student = students_sorted_by_grade[-1]['id']
    worst_student = students_sorted_by_grade[0]['id']

    print(f"Average Student Grade: {average_student_grade}")
    print(f"Hardest Subject: {hardest_subject}")
    print(f"Easiest Subject: {easiest_subject}")
    print(f"Best Performing Grade: {best_lvl}")
    print(f"Worst Performing Grade: {worst_lvl}")
    print(f"Best Student ID: {best_student}")
    print(f"Worst Student ID: {worst_student}")
if __name__ == '__main__':
    main()