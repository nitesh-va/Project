from department.models import Department
from teacher.models import Teacher

def run():
    # Fetch all Teacher records
    teachers = Teacher.objects.all()

    # Loop through each Teacher
    for teacher in teachers:
        try:
            # Check if the teacher is associated with a department
            if teacher.dept_name:
                # Get the department's Head of Department (HOD)
                dept = teacher.dept_name  # This is a ForeignKey to Department
                if dept.hod:
                    # Update the teacher's HOD with the name of the HOD from the department
                    teacher.hod = dept.hod.name  # Assuming HOD is a Teacher model instance
                    teacher.save()  # Save the teacher with the updated HOD
                    print(f"Updated HOD for teacher {teacher.name} (emp_id: {teacher.emp_id}) to {dept.hod.name}")
                else:
                    print(f"No HOD found for department {dept.department_name} (teacher: {teacher.name})")
            else:
                print(f"Teacher {teacher.name} (emp_id: {teacher.emp_id}) is not assigned to a department.")
        except Exception as e:
            print(f"Error updating HOD for teacher {teacher.name} (emp_id: {teacher.emp_id}): {e}")
