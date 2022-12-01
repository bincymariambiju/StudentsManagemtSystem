====rfrom django.shortcuts import render,redirect
from django.http import HttpResponse
from studcamp.models import Contact,Signup,Course,Staff,Feedback,Session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from studcamp.forms import CourseForm



# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    #return HttpResponse("this is index page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request,'contact.html')
def contact_view(request):
    contact = Contact.objects.all()
    return render(request,"contact_view.html",{'studcamp':contact})

def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        myuser= authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect("/adminhome")
        else:
            return redirect("/adminlogin")
    #return HttpResponse("this is index page")
    return render(request,'adminlogin.html')

def adminbase(request):
    return render(request,'adminbase.html')
def adminhome(request):
    return render(request,'adminhome.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        qualification = request.POST.get("qualification")
        course = request.POST.get("course")
        password = request.POST.get("password")
        cpassword = request.POST.get("password")
        signup = Signup(name=name,email=email,phone=phone,qualification=qualification,course=course,password=password,cpassword=cpassword)
        signup.save()
        if( password != cpassword):
            return redirect("/signup")
        try:
            if User.object.get(username=name):
                return redirect("/signup")
        except:
            pass
        user=User.objects.create_user(name,email,password)
        user.username=name
        user.save()
        return redirect("/studentslogin")
        
    return render(request,'signup.html')
def studentslogin(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("passwrd")
        myuser= authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect("/studenthome")
        else:
            return redirect("/studentslogin")
    return render(request,"studentslogin.html")
def studentbase(request):
    return render(request,'studentbase.html')

def studenthome(request):
    return render(request,'studenthome.html')
def signup_view(request):
    stud = Signup.objects.all()

    return render(request,'signup_view.html',{'studcamp':stud})

def destroy(request,id):
    
    studcamp = Signup.objects.get(id=id)
    studcamp.delete()
    return redirect('/signup_view')


# def add_course(request):  
#     if request.method == "POST":  
#         form = CourseForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/add_course')  
#             except:  
#                 pass  
#     else:  
#         form = CourseForm()  
#     return render(request,'add_course.html',{'form':form})

def add_course(request):
    if request.method == "POST":
        cid = request.POST.get("cid")
        cname = request.POST.get("cname")
        duration = request.POST.get("duration")
        fee = request.POST.get("fee")
        course = Course(cid=cid,cname=cname,duration=duration,fee=fee)
        course.save()

    return render(request,'add_course.html')

def course_view(request):
    show = Course.objects.all()
    return render(request,"course_view.html",{'studcamp':show})
def course_destroy(request,id):
    studcamp = Course.objects.get(id=id)
    studcamp.delete()
    return redirect('/course_view2')



def course_view2(request):
    show = Course.objects.all()
    return render(request,"course_view2.html",{'studcamp':show})
def edit_course(request,id):
    show = Course.objects.get(id=id)
    return render(request,"edit_course.html",{'studcamp':show})
def update_course(request,id):
    if request.method == "POST":
        show = Course.objects.get(id=id)
        show.cid = request.POST.get("cid")
        show.cname = request.POST.get("cname")
        show.duration = request.POST.get("duration")
        show.fee = request.POST.get("fee")
        try:  
            show.save()
            return redirect('/course_view2',)  
        except:  
            pass  
    return render(request,"edit_course.html",studcamp)

def staff(request):
    if request.method == "POST":
        sid = request.POST.get("sid")
        sname = request.POST.get("sname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        qualification = request.POST.get("qualification")
        subject = request.POST.get("subject")
        salary = request.POST.get("salary")
        staff = Staff(sid=sid,sname=sname,email=email,phone=phone,address=address,qualification=qualification,subject=subject,salary=salary)
        staff.save()
    
    return render(request,"staff.html")
def staff_view(request):
    staff = Staff.objects.all()
    return render(request,"staff_view.html",{'studcamp':staff})
def edit_staff(request,id):
    staff = Staff.objects.get(id=id)
    return render(request,"edit_staff.html",{'studcamp':staff})
def update_staff(request,id):
    if request.method == "POST":
        staff = Staff.objects.get(id=id)
        staff.sid = request.POST.get("sid")
        staff.sname = request.POST.get("sname")
        staff.email = request.POST.get("email")
        staff.phone = request.POST.get("phone")
        staff.address = request.POST.get("address")
        staff.qualification = request.POST.get("qualification")
        staff.subject = request.POST.get("subject")
        staff.salary = request.POST.get("salary")
        
        try:  
            staff.save()
            return redirect('/staff_view',)  
        except:  
            pass  
    return render(request,"edit_staff.html",{'studcamp':staff})

def staff_view2(request):
    staff = Staff.objects.all()
    
    return render(request,"staff_view2.html",{'studcamp':staff})

def staff_destroy(request,id):
    studcamp = Staff.objects.get(id=id)
    studcamp.delete()
    return redirect('/staff_view')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        feedback = Feedback(name=name,email=email,desc=desc)
        feedback.save()
    
    return render(request,"feedback.html")

def feedback_view(request):
    feedback = Feedback.objects.all()
    return render(request,"feedback_view.html",{'studcamp':feedback})
def session(request):
    if request.method == "POST":
        session = request.POST.get('session')
        shr = request.POST.get('shr')
        msg = request.POST.get('msg')
        session = Session(session=session,shr=shr,msg=msg)
        session.save()

    return render(request,'session.html')
def session_view(request):
    session = Session.objects.all()
    return render(request,'session_view.html',{'studcamp':session})
def edit_session(request,id):
    session = Session.objects.get(id=id)
    return render(request,"edit_session.html",{'studcamp':session})
def update_session(request,id):
    if request.method == "POST":
        session = Session.objects.get(id=id)
        session.session = request.POST.get('session')
        session.shr = request.POST.get('shr')
        session.msg = request.POST.get('msg')
        try:  
            session.save()
            return redirect('/session_view',)  
        except:  
            pass  
    return render(request,"edit_session.html",{'studcamp':session})

def session_view2(request):
    session = Session.objects.all()
    return render(request,'session_view2.html',{'studcamp':session})

def destroy_session(request,id):
    studcamp = Session.objects.get(id=id)
    studcamp.delete()
    return redirect('/session_view')





