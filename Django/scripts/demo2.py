from student.models import Student

def run():
    # Fetch all students
    students = Student.objects.all()

    # Loop through each student
    for student in students:
        try:
            # Get the teacher associated with the student using emp_id
            teacher = student.emp_id  # This retrieves the Teacher instance directly

            if teacher:
                # Check if the teacher has a department assigned
                if teacher.dept_name:
                    # Update the student's department to the teacher's department
                    student.dept_name = teacher.dept_name
                    # Save the updated student instance
                    student.save()  
                    print(f'Successfully updated student {student.roll_no}: '
                          f'Department to {teacher.dept_name.department_name}.')
                else:
                    print(f'Teacher {teacher.name} (ID: {teacher.emp_id}) has no department assigned.')
            else:
                print(f'Student {student.roll_no} has no associated teacher.')
        except Exception as e:
            print(f'Error updating student {student.roll_no}: {e}')