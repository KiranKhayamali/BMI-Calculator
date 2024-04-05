from django.contrib.auth import get_user_model()
from .models import BMIHistory

User = get_user_model()

def display_bmi_history(user):
    bmi_history = BMIHistory.objects.filter(user=user).order_by('-date')
    print("BMI History:")
    for bmi in bmi_history:
        print(f"{bmi.date:%B %d, %Y}: {bmi.bmi}")

user = User.objects.get(username='john_doe')
display_bmi_history(user)