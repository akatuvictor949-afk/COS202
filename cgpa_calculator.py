def calculate_cgpa():
    print("=" * 50)
    print("     PERSONAL POCKET CGPA CALCULATOR (PPC)")
    print("=" * 50)
    
    total_quality_points = 0
    total_units = 0
    courses = []
    
    print("\nEnter your courses one by one.")
    print("Type 'done' when finished.\n")
    
    while True:
        course_code = input("Course Code (e.g. COS202): ").strip().upper()
        if course_code.lower() == 'done':
            break
        if not course_code:
            print("Course code cannot be empty!")
            continue
            
        try:
            units = int(input(f"Credit Units for {course_code}: "))
            if units <= 0:
                print("Units must be greater than 0!")
                continue
        except ValueError:
            print("Invalid units!")
            continue
        
        print("\nGrade Options: A=5.0, B=4.0, C=3.0, D=2.0, E=1.0, F=0.0")
        grade = input(f"Grade for {course_code}: ").strip().upper()
        
        grade_points = {'A':5.0, 'B':4.0, 'C':3.0, 'D':2.0, 'E':1.0, 'F':0.0}
        
        if grade not in grade_points:
            print("Invalid grade! Use A, B, C, D, E, or F.")
            continue
        
        qp = units * grade_points[grade]
        total_quality_points += qp
        total_units += units
        courses.append((course_code, units, grade, qp))
        
        print(f"✓ Added: {course_code} | {units} units | Grade: {grade}\n")
    
    if total_units == 0:
        print("No courses entered.")
        return
    
    cgpa = total_quality_points / total_units
    
    print("\n" + "="*60)
    print("                    RESULTS")
    print("="*60)
    print(f"{'Course':<10} {'Units':<8} {'Grade':<8} {'QP':<10}")
    print("-" * 60)
    
    for course in courses:
        print(f"{course[0]:<10} {course[1]:<8} {course[2]:<8} {course[3]:<10.1f}")
    
    print("-" * 60)
    print(f"Total Units: {total_units}")
    print(f"Total Quality Points: {total_quality_points:.1f}")
    print(f"\n🎯 YOUR CGPA: {cgpa:.2f}")
    
    if cgpa >= 4.50:
        print("Classification: First Class Honours 👏")
    elif cgpa >= 3.50:
        print("Classification: Second Class Upper 🎉")
    elif cgpa >= 2.50:
        print("Classification: Second Class Lower")
    elif cgpa >= 1.50:
        print("Classification: Third Class")
    else:
        print("Classification: Pass")

if __name__ == "__main__":
    calculate_cgpa()
    input("\nPress Enter to exit...")