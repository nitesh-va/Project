from school.models import School
from department.models import Department 

def run():
     # Fetch all departments
    departments = Department.objects.all()
    # Loop through each department
    for department in departments:
            # Get the associated school
        school = department.school

        if school:
                # Add the department to the school's many-to-many relationship
            school.dept_name.add(department)  # Use add() to link the department
            print("done") 
            school.save()  # Save the changes to the school instance
        else:
            print("Oopies")   

