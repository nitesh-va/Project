from department.models import Department

def run():
    try:
        # Fetch the department by its ID
        department = Department.objects.all()

        # Check if the department has an HOD
        if department.hod:
            hod_teacher = department.hod
            
            # Print details of the HOD teacher in the department
            print(f"HOD Teacher: {hod_teacher.name} (ID: {hod_teacher.emp_id})")
        else:
            print(f"No HOD assigned for department '{department.department_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# run(dept_id)  # Call with the desired department ID
