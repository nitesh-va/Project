from teacher.models import Teacher  # Adjust the import according to your app structure
from user.models import User    # Replace 'your_app' with the actual app name
def run():
    for teacher in Teacher.objects.all():
        # Check if a user already exists with the same username to avoid duplicates
        if not User.objects.filter(username=teacher.name).exists():
            user = User(
                
                username=teacher.name,
                email=f"{teacher.name.replace(' ', '').lower()}@gmail.com",  # Creating a sample email
            )

            user.save()
            print(f"Created user: {user.username}")
        else:
            print(f"User with username '{teacher.name}' already exists.")