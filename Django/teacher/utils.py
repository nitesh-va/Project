
from teacher.models import  Teacher
from student.models import Student


def get_teacher_performance():
    """Retrieve the performance data for teachers based on emp_id."""
    passing_threshold = 33.0
    performance_data = []

    # Get all teachers
    teachers = Teacher.objects.all()
    for teacher in teachers:
        students = Student.objects.filter(emp_id=teacher)  # Filter by emp_id
        total_students = students.count()
        total_passed = students.filter(percentage__gte=passing_threshold).count()

        passing_percentage = (total_passed / total_students * 100) if total_students > 0 else 0

        performance_data.append({
            "emp_id": teacher.emp_id,
            "passing_percentage": passing_percentage,
            "total_passed": total_passed,
            "total_students": total_students
        })
    
    return performance_data
