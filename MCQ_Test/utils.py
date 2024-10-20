# Create utils.py in the app (e.g., MCQ_Test)
from django.core.mail import send_mail
from django.conf import settings
# In urls.py



def send_mcq_result_email(student_email, student_name, score):
    subject = "Your MCQ Test Result"
    message = f"Dear {student_name},\n\nYou have completed the MCQ test. Your score is: {score}.\n\nThank you for participating!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [student_email]

    send_mail(subject, message, from_email, recipient_list)
