from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout # fro check if user is which actually logs the user in after authentication.
# return HttpResponseRedirect(request.path_info)
from django.contrib.auth.hashers import check_password
from .models import profile

def login_req(request):
    if request.method=="POST":
        email=request.POST.get('mail')
        passwords=request.POST.get('password')
        # print(email, passwords)
        user_obj=User.objects.filter(username=email)#you need to check if a user exists:

        if not user_obj.exists():
            messages.warning(request, "Account not found ")
            return HttpResponseRedirect(request.path_info)
        
        

        user_obj=authenticate(username=email, password=passwords)
        print('your data',user_obj)

        try:
            is_correct = check_password(passwords, user_obj.password) #it used to check is your password match from database
            print(f"Password correct? {is_correct}")  # Should print True
        except :
            print('i think password is wrong')

            
        #for check if account is verify or not
        profilee = profile.objects.filter(name=user_obj).first()  # Ensure correct user
        try :
            if not  profilee.is_verify:
                messages.warning(request, "Account not  Veriy Yet  ")
                return HttpResponseRedirect(request.path_info)
        except Exception as e:
            print(e)
        #End 

        if user_obj:
             login(request,user_obj)
             return redirect('index')
        
        #Since is_verify is in the Profile model, you need to access it through the related_name (profile) in the User model.
        # Check if profile exists & is verified

         #--- hasattr(user_obj, 'profile') → Ensures the user has a profile before checking is_verify.
                               #not user_obj.profile.is_verify → Checks if the profile is not verified.
                               #If the profile doesn’t exist or is not verified, it redirects with a warning message
        # if not hasattr(user_obj, 'profile') or not user_obj.profile.is_verify:
        #     messages.warning(request, "Your account is not verified. Please verify it first.")
        #     return HttpResponseRedirect(request.path_info)
          #-----Ends here

        

        
        messages.warning(request, " invalid username or password")
        return HttpResponseRedirect(request.path_info)
    return render(request, 'Acc/login.html')


def register_page(request):
    if request.method=="POST":
        first=request.POST.get('first')
        last=request.POST.get('last')
        email=request.POST.get('mail')
        passwords=request.POST.get('password')
        user_obj=User.objects.filter(username=email) #you need to check if a user exists:

        if(user_obj.exists()):
            messages.warning(request, "This Email already Exists")
            return HttpResponseRedirect(request.path_info) #go to ecom helper for this detail
        
        user_obj=User.objects.create(first_name=first, last_name=last, email=email, username=email)
        user_obj.set_password(passwords) #You can also change a password programmatically, using set_password():
        user_obj.save()
        messages.success(request, " An mail has been sent your Gmail")
        return HttpResponseRedirect(request.path_info)
        


    return render(request, 'Acc/register.html')

def activate_mail(request, token):
    print(f"🔹 Received Token: {token}")  # Debugging Step 1

    try:
        user_profile = profile.objects.get(mail_token=token)
        print(f"🔹 Found Profile for: {user_profile.name.email}")  # Debugging Step 2

        user_profile.is_verify = True
        user_profile.save()
        
        print(f"✅ Verification Status: {user_profile.is_verify}")  # Debugging Step 3
        
        messages.success(request, "Your email has been verified successfully!")
        return redirect("/")
    
    except profile.DoesNotExist:
        print("❌ Invalid or expired token!")  # Debugging Step 4
        return HttpResponse("Invalid or expired token!")


# from django.http import HttpResponse
