from teacher.models import Teacher
from user.models import User  # Assuming the User model is in the 'users' app
from django.db.utils import IntegrityError
from department.models import Department





# # def run():
# #     teachers = Teacher.objects.filter(is_active=True)
    
    # for teacher in teachers:
    #     # Default role is 'staff'
    #     role = 'staff'
        
    #     # Check if the teacher is the HOD of any department
    #     # If the teacher's name matches the department's HOD, assign 'HOD' role
    #     departments = Department.objects.filter(is_active=True)
        
    #     for department in departments:
    #         if department.hod == teacher:
    #             role = 'HOD'
    #             break 
        
# #         # Extract performance from the teacher model
# #         performance = teacher.performance if hasattr(teacher, 'performance') else None

# #         try:
# #             # Create new Custom_User instance using teacher data
# #             user = User(
# #                 username=str(teacher.name),  # Using teacher's name as the username
# #                 email=f"{teacher.name}@gmail.com",  # Generate email based on teacher's name
# #                 name=teacher.name,
# #                 emp_id=teacher.emp_id,
# #                 performance=performance,
# #                 dept_name=teacher.dept_name,  # Assign department
# #                 school_name=teacher.school_name,  # Assign school (if applicable)
# #                 role=role,  # Assign role based on whether they are HOD or not
# #                 is_active=teacher.is_active,  # Assign active status
# #             )
 
# #             # Save the user (this will trigger the password generation in the save method)
# #             user.save()
 
# #             print(f"Created user: {user.username} with role {user.role}, performance {user.performance} and a generated password.")
 
# #         except IntegrityError as e:
# #             print(f"Error creating user for {teacher.name}: {e}")

# from teacher.models import Teacher
# from user.models import User  # Assuming the User model is in the 'users' app
# from django.db.utils import IntegrityError
# from department.models import Department

# def run():
#     teachers = Teacher.objects.filter(is_active=True)
    
#     for teacher in teachers:
#         # Default role is 'staff'
#         role = 'staff'
        
#         # Check if the teacher is the HOD of any department
#         # If the teacher's name matches the department's HOD, assign 'HOD' role
#         departments = Department.objects.filter(is_active=True)
        
#         for department in departments:
#             if department.hod == teacher:
#                 role = 'HOD'
#                 break 
        
#         # Extract performance from the teacher model
#         performance = teacher.performance if hasattr(teacher, 'performance') else None

#         try:
#             # Create new Custom_User instance using teacher data
#             # Adjust the email generation to remove spaces and only use the first name
#             email_username = teacher.name.split()[0].lower()  # Use the first name in lowercase for email
            
#             # Create the user instance
#             user = User(
#                 username=teacher.name,  # Using teacher's name as the username
#                 email=f"{email_username}@gmail.com",  # Generate email using only first name
#                 name=teacher.name,
#                 emp_id=teacher.emp_id,
#                 performance=performance,
#                 dept_name=teacher.dept_name,  # Assign department
#                 school_name=teacher.school_name,  # Assign school (if applicable)
#                 role=role,  # Assign role based on whether they are HOD or not
#                 is_active=teacher.is_active,  # Assign active status
#             )
 
#             # Save the user (this will trigger the password generation in the save method)
#             user.save()
 
#             print(f"Created user: {user.username} with role {user.role}, performance {user.performance} and a generated password.")
 
#         except IntegrityError as e:
#             print(f"Error creating user for {teacher.name}: {e}")
from django.db import IntegrityError
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from user.models import User
from teacher.models import Teacher  # Make sure to import Custom_User and Teacher
 
def create_users_for_teachers():
    # Filter for active teachers
    teachers = Teacher.objects.filter(is_active=True)  
 
    users_to_create = []
 
    for teacher in teachers:
        role = 'staff'
        
        # Check if the teacher is the HOD of any department
        # If the teacher's name matches the department's HOD, assign 'HOD' role
        departments = Department.objects.filter(is_active=True)
        
        for department in departments:
            if department.hod == teacher:
                role = 'HOD'
                break  
       
        # Generate a username based on the teacher's name and employee ID
        base_username = f"{teacher.name.lower().replace(' ', '_')}"
        username = base_username
       
        # Check if the username already exists. If so, append a random string to make it unique.
        while User.objects.filter(username=username).exists():
            # Append a random string of length 4 to the base username
            username = f"{base_username}_{get_random_string(4)}"
       
        # Assign the role based on whether the teacher is an HOD or not
        
            
        # Split the teacher's name into first name and last name
 
        # Automatically generate the email username@school.com
        email_username = teacher.name.split()[0].lower()  # Using school name in domain
       
        # Extract performance from the teacher model (if it exists)
        performance = getattr(teacher, 'performance', None)  # Use getattr to safely get performance value
 
        # Generate a random password (you can adjust the length and complexity)
        random_password = get_random_string(12)  # Random 12-character password
       
        department = teacher.dept_name if teacher.dept_name else None
        school = teacher.school_name if teacher.school_name else None
 
        try:
            # Create new Custom_User instance using teacher data
            user = User(
                username=teacher.name,  # Using teacher's name as the username
                email=f"{email_username}@gmail.com",  # Generate email using only first name
                name=teacher.name,
                emp_id=teacher.emp_id,
                performance=performance,
                dept_name=teacher.dept_name,  # Assign department
                school_name=teacher.school_name,  # Assign school (if applicable)
                role=role,  # Assign role based on whether they are HOD or not
                is_active=teacher.is_active,
                temp_pass=random_password # Assign active status
            )
            user.set_password(random_password)  # Hash the password for security
            users_to_create.append(user)  # Add user to the list of users to be created
 
            # Print the username, role, performance, and generated password for debugging
            print(f"Prepared user: {user.username} with role {user.role}, performance {user.performance} and a generated password.")
            print("Password:", random_password)
            print("Hashed password:", user.password)
        except IntegrityError as e:
            print(f"Error creating user for {teacher.name}: {e}")
 
    # Bulk create users if there are users to create
    if users_to_create:
        User.objects.bulk_create(users_to_create)
        print(f"Successfully created {len(users_to_create)} users.")
    else:
        print("No users were created.")
 
def run():
    print("Starting user creation for teachers...")
    create_users_for_teachers()
    print("User creation process completed.")
 
if __name__ == "__main__":
    run()
 