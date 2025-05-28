from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(email, token):
    subject="verify your gmail "
    verification_link = f"http://192.168.1.57/accounts/activate/{token}/"
    print('link is this:',verification_link)
  # Change the domain for production

    message = f"""
    Hi,
    Please click the link below to verify your email:
    {verification_link} If you did not request this, please ignore this email.
    """
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Make sure this is set correctly
            [email],
            fail_silently=False,  # This will raise an error if mail fails
        )
        print("✅ Email sent successfully!")  # Debugging Step 3
    except Exception as e:
        print(f"❌ Error sending email: {e}")  # Debugging Step 4
