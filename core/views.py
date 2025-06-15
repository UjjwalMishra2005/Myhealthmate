from django.shortcuts import render,redirect
from django.contrib.auth import login
def home(request):
    return render(request, 'main.html',{'is_authenticated': request.user.is_authenticated}) 

# def signup(request):
#     return render(request, 'signup.html')   
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        adhaar_number = request.POST.get('adhaar_number')
        mobile_number = request.POST.get('mobile_number')

        # Authenticate the user
        user = Patient.objects.filter(adhaar_number=adhaar_number, phone_number=mobile_number).first()

        if user:
            # Log the user in
            login(request, user)
            return redirect('home')
        else:
            # Invalid credentials
            print("Invalid login credentials.")
            error = "Invalid Adhaar number or mobile number."
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html', {'error': None})
# import random
# import string
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient


# def generate_random_password(length=12):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        adhaar_number = request.POST.get('adhaar_number')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        # gender = request.POST.get('gender')

        if Patient.objects.filter(adhaar_number=adhaar_number).exists():
            print( "Adhaar number already registered.")
            return redirect('signup')

        # if Patient.objects.filter(phone_number=phone_number).exists():
        #     messages.error(request, "Phone number already registered.")
        #     return redirect('signup')

        password = 'dhnwirt57h3noegg'
        patient = Patient.objects.create_user(
            username=adhaar_number,
            full_name=full_name,
            adhaar_number=adhaar_number,
            phone_number=phone_number,
            city=city,
            state=state,
            password=password  # Set but not shown to user
        )

        
        print("Signup successful! You can now log in.")
        login(request, patient)
        return redirect('home')

    return render(request, 'signup.html')
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Token,Department

# @csrf_exempt  # Only for prototyping! Use @csrf_protect with CSRF token in production.
# @login_required
# def save_token(request):
#     if request.user.is_authenticated:
#         print('request method:', request.method)
#         print('request body:', request.body)
#         if request.method == 'POST':
#             data = json.loads(request.body)
#             # Do something with `data`, like saving to DB
#             new_token = Token(
#             patient=request.user,
#             center_name=data.get('center_name'),
#             center_code=data.get('center_code')
#         )
#             new_token.save()

#             print("Received token data:", data)
#             print(new_token.token_number)
            
#             return JsonResponse({'status': 'success'})
#         return JsonResponse({'error': 'Invalid method'}, status=405)
from django.utils import timezone
@login_required
def serve(request):
    if request.user.is_superuser or request.user.is_staff:

        if request.method == 'POST':
            dept = request.POST.get('department')
            token_id = request.POST.get('token_id')
            token = Token.objects.get(id=token_id)
            token.served_at = timezone.now()
            token.department = dept
            token.is_active = False
            token.save()
            return redirect('/')
        depts = Department.objects.all()
        tokens = Token.objects.filter(is_active = True)
        tokens_count = tokens.count()
        return render(request, 'serve.html',{'tokens': tokens, 'tokens_count': tokens_count, 'departments': depts})
    return redirect('home')




from .models import Doctor  # Assuming Doctor model has ForeignKey to Department

def get_doctors(request):
    dept_id = request.GET.get('department')
    doctors = Doctor.objects.filter(department_id=dept_id)
    return render(request, 'partials/doctor_select.html', {'doctors': doctors})



from django.db import IntegrityError


@csrf_exempt
@login_required
def save_token(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                data = json.loads(request.body)

                new_token = Token(
                    patient=request.user,
                    center_name=data.get('center_name'),
                    center_code=data.get('center_code')
                )

                new_token.save()  # This can raise IntegrityError

                print("Received token data:", data)
                print("Assigned token number:", new_token.token_number)

                return JsonResponse({'status': 'success', 'token_number': new_token.token_number})

            except IntegrityError as e:
                print("IntegrityError:", str(e))
                return JsonResponse({'error': 'Token already exists for this user today.'}, status=409)

            except Exception as e:
                print("Unexpected error while saving token:", str(e))
                return JsonResponse({'error': 'Server error', 'details': str(e)}, status=500)

        return JsonResponse({'error': 'Invalid method'}, status=405)

    return JsonResponse({'error': 'Unauthorized'}, status=401)




