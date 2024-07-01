from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Doctor, Patient
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
def signup(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address_line1 = request.POST.get('address-line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        image=request.FILES.get('profile-photo')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use a different email.')
            return render(request, 'signup.html')

        # Create the User object
        user = User.objects.create_user(username=email, email=email, password=password)
        
        if user_type == 'doctor':
            # Create Doctor object
            doctor = Doctor(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                address_line1=address_line1,
                city=city,
                state=state,
                pincode=pincode,
                image=image
            )
            doctor.save()
            messages.success(request, 'Doctor account created successfully.')
            
        elif user_type == 'patient':
            patient = Patient(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                address_line1=address_line1,
                city=city,
                state=state,
                pincode=pincode,
                image=image
            )
            patient.save()
            messages.success(request, 'Patient account created successfully.')
        
        return redirect('login')
    
    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type') 
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if user_type == 'doctor':
                try:
                    doctor = Doctor.objects.get(email=email) 
                    return redirect('doctor')
                except Doctor.DoesNotExist:
                    messages.error(request, 'Doctor profile not found.')
                    return render(request, 'login.html')

            elif user_type == 'patient':
                try:
                    patient = Patient.objects.get(email=email)
                    return redirect('patient')
                except Patient.DoesNotExist:
                    messages.error(request, 'Patient profile not found.')
                    return render(request, 'login.html')

        else:
            # Authentication failed
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')

    else:
        # Render the login form for GET requests
        return render(request, 'login.html')

@login_required(login_url='login')
def doctor(request):
    doctor = get_object_or_404(Doctor, email=request.user.email)
    return render(request, 'doctor_dashboard.html', {'user': doctor})

@login_required(login_url='login')
def patient(request):
    patient = get_object_or_404(Patient, email=request.user.email)
    print(patient)
    return render(request, 'patient_dashboard.html', {'user': patient})

def Logout(request):
    logout(request)
    return redirect('login')