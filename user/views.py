from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from user.models import Contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendance






#============home page==============================
def home(request):
    return render(request, 'home.html')

#==============profile view============================

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Login and Try Again')
        return redirect('/login')
    user=request.user
    print(user)
    posts=Enrollment.objects.filter(user=user)
    context={"posts":posts}
    return render(request, "user/profile.html",context)


#=============signup view==========================
def signup(request):
    if request.method == 'POST':
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)>11 or len(username)<11:
            messages.info(request, 'Phone number must be 11 digits')
            return redirect('/signup')

        if pass1 != pass2:
            messages.info(request, 'Password is not Matching')
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request, 'Phone number is Taken')
                return redirect('/signup')

        except Exception as identifier:
            pass

                
        try:
            if User.objects.get(email=email):
                messages.warning(request, 'email is Taken')
                return redirect('/signup')

        except Exception as identifier:
            pass

        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,'User is created please login')
        return redirect('/login')

    return render(request, 'user/signup.html')


#===============Login view==================================
def handlelogin(request):
    if request.method == 'POST':
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request, 'Login successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
            
    return render(request, 'user/login.html')


#===========logout view=============================

def handlelogout(request):
    logout(request)
    messages.success(request, 'Logout success')
    return redirect('/login')


#===========contact view============================

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()

        messages.info(request, 'Thanks for Contacting us we will get back you soon')
        return redirect('/contact')

    return render(request, 'user/contact.html')


#===============Enrollment views====================

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Login and try again')
        return redirect('/login')
    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={'Membership':Membership, 'SelectTrainer':SelectTrainer}
    if request.method == 'POST':
        FullName=request.POST.get('FullName')
        Email=request.POST.get('email')
        Gender=request.POST.get('Gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        SelectMembershipplan=request.POST.get('SelectMembershipplan')
        SelectTrainer=request.POST.get('SelectTrainer')
        Reference=request.POST.get('Reference')
        Address=request.POST.get('Address')
        myquery=Enrollment(FullName=FullName,Email=Email,Gender=Gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=SelectMembershipplan,SelectTrainer=SelectTrainer,Reference=Reference,Address=Address)
        myquery.save()
        messages.success(request, 'Thanks For Enrollment')
        return redirect('/enroll')
    return render(request, 'user/enroll.html', context)



#============Gallery==================

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request, 'user/gallery.html',context)


#================Attendance=====================

def attendance(request):
    return render(request, 'user/attendance.html')