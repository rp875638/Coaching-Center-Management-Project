from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *
import datetime
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        nteacher= Teacher.objects.all()[:5]
        nstudent= Student.objects.all()[:5]
        teacher= User.objects.filter(is_staff = 1,accepted=0)[:5]
        student= User.objects.filter(is_staff=0,accepted=0)[:5]
        return render(request,"index.html",{"details":nteacher,"detail":nstudent,"adetails":teacher,"adetail":student,"tname":"Teacher","sname":"Student"})
    else:
        return render(request,'login.html')
def registerpage(request):
    return render(request,"register.html")
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect('/')
        
    else:
        return render(request,"login.html")    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = request.POST['user']
        if password == confirm_password:
            if user == "teacher":
                User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password,is_staff=True)
                message = "Sucessfully! You are sucessfully register"
                return redirect("/",{"message":message})
            elif user == "student":
                 User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                 message = "Sucessfully! You are sucessfully register"
                 return redirect("/",{"message":message})
            else:
                return redirect('/')
            
        else:
            message = "Your passwords are different!"
            return render(request,"register.html",{"message":message})
        
    else:
        return render(request,"register.html",{"message":"Please!Login first"})    
def logout(request):
    auth.logout(request)
    return redirect("/")
def save(request,id):
    if request.user.is_authenticated and request.method == "POST":
        if request.user.is_staff:
            if Teacher.objects.filter(username=request.POST['username']).exists():
                obj = Teacher.objects.get(username=request.POST['username'])
                obj.username = request.POST['username']
                obj.first_name = request.POST['first_name']
                obj.last_name = request.POST['last_name']
                obj.email = request.POST['email']
                obj.contact = request.POST['contact']
                obj.dob = request.POST['dob']
                obj.subject = request.POST['subject1']
                obj.save()
                return render(request,"index.html")
            else:
                obj = Teacher(username=request.POST['username'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],contact=request.POST['contact'],dob=request.POST['dob'],subject=request.POST['subject1'])
                obj.save()
                return render(request,"index.html")
        else:
            if Student.objects.filter(username=request.POST['username']).exists():
                obj = Student.objects.get(username=request.POST['username'])
                obj.username = request.POST['username']
                obj.first_name = request.POST['first_name']
                obj.last_name = request.POST['last_name']
                obj.email = request.POST['email']
                obj.contact = request.POST['contact']
                obj.dob = request.POST['dob']
                obj.subject1 = request.POST['subject1']
                obj.subject2 = request.POST['subject2']
                obj.subject3 = request.POST['subject3']
                obj.type = request.POST['type']
                obj.save()
                return render(request,"index.html")
            else:
                obj = Student(username=request.POST['username'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],contact=request.POST['contact'],dob=request.POST['dob'],subject1=request.POST['subject1'],subject2=request.POST['subject2'],subject3=request.POST['subject3'],type = request.POST['type'])
                obj.save()
                return render(request,"index.html")
    else:
        return render(request,"login.html")
def save_detail(request,id):
    if request.method == 'POST' and request.user.is_authenticated:
        if request.user.is_staff:
            obj = Teacher.objects.get(username=request.POST['username'])
            obj.username = request.POST['username']
            obj.first_name = request.POST['first_name']
            obj.last_name = request.POST['last_name']
            obj.email = request.POST['email']
            obj.contact = request.POST['contact']
            obj.dob = request.POST['dob']
            obj.subject = request.POST['subject1']
            obj.save()
            return render(request,"index.html")
        else:
            obj = Student.objects.get(username=request.POST['username'])
            obj.username = request.POST['username']
            obj.first_name = request.POST['first_name']
            obj.last_name = request.POST['last_name']
            obj.email = request.POST['email']
            obj.contact = request.POST['contact']
            obj.dob = request.POST['dob']
            obj.subject1 = request.POST['subject1']
            obj.subject2 = request.POST['subject2']
            obj.subject3 = request.POST['subject3']
            obj.type = request.POST['type']
            obj.save()
            return render(request,"index.html")
    else:
        return render(request,"login.html")           
def fees(request,id):
    if request.user.is_authenticated:
        fee= Fees.objects.filter()
        return render(request,"fees.html",{"details":fee,"name":"Fees"})
    else:
        return redirect("/")
def add_fees(request):
    if request.user.is_authenticated:
        obj = Fees(idstudent=request.POST['id'],amount=request.POST['amount'],month=request.POST['month'],year=request.POST['year'],dates=datetime.datetime.now())
        obj.save()
        fee= Fees.objects.filter()
        return render(request,"fees.html",{"details":fee,"name":"Fees"})
    else:
        return redirect("/")
def notification(request,id):
    if request.user.is_authenticated:
        notification= Notifications.objects.filter()
        snotification= StudentNotification.objects.filter()
        tnotification= TeacherNotification.objects.filter()
        return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
    else:
        return redirect("/")
def add_notification(request):
    if request.user.is_authenticated:
        print(request.POST)
        if request.POST['types'] == "Teacher":
            obj = TeacherNotification(notify=request.POST['notify'],is_seen=0,ndate=datetime.datetime.now())
            obj.save()
            notification= Notifications.objects.filter()
            snotification= StudentNotification.objects.filter()
            tnotification= TeacherNotification.objects.filter()
            return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
        elif request.POST['types'] == "Student":
            obj = StudentNotification(notify=request.POST['notify'],is_seen=0,ndate=datetime.datetime.now())
            obj.save()
            notification= Notifications.objects.filter()
            snotification= StudentNotification.objects.filter()
            tnotification= TeacherNotification.objects.filter()
            return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
        elif request.POST['types'] == "Everyone":
            obj = Notifications(notifications=request.POST['notify'],dates=datetime.datetime.now())
            obj.save()
            notification= Notifications.objects.filter()
            snotification= StudentNotification.objects.filter()
            tnotification= TeacherNotification.objects.filter()
            return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
    else:
        redirect("/")
def delete_notification(request,types,id):
    if request.user.is_authenticated:
        if types == "all":
            notification = Notifications.objects.get(idnotifications=id)
            notification.delete()
            notification= Notifications.objects.filter()
            snotification= StudentNotification.objects.filter()
            tnotification= TeacherNotification.objects.filter()
            return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
        elif types=="teacher":
            notification = TeacherNotification.objects.get(idnotification=id)
            notification.delete()
            notification= Notifications.objects.filter()
            snotification= StudentNotification.objects.filter()
            tnotification= TeacherNotification.objects.filter()
            return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
        elif types == "student":
            notification = StudentNotification.objects.get(idnotification=id)
            notification.delete()
            notification= Notifications.objects.filter()
            snotification= StudentNotification.objects.filter()
            tnotification= TeacherNotification.objects.filter()
            return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
        else:
            notification= Notifications.objects.filter()
            snotification= StudentNotification.objects.filter()
            tnotification= TeacherNotification.objects.filter()
            return render(request,"notifiaction.html",{"details":notification,"sdetails":snotification,"tdetails":tnotification,"name":"Notification"})
    else:
        return render(request,"index.html")
def batch(request,id):
    if request.user.is_authenticated:
        batch= Batch.objects.all()
        return render(request,"batch.html",{"details":batch,"name":"Batch"})
    else:
        return redirect("/")
def add_batch(request):
    if request.user.is_authenticated:
        obj = Batch(idteacher=request.POST['id'],subject=request.POST['subject'],type=request.POST['type'],start_time=request.POST['start_time'],end_time=request.POST['end_time'])
        obj.save()
        batch= Batch.objects.all()
        return render(request,"batch.html",{"details":batch,"name":"Batch"})
    else:
        redirect("/")
def tests(request,id):
    if request.user.is_authenticated:
        test= Test.objects.filter()
        return render(request,"test.html",{"details":test,"name":"Test"})
    else:
        return redirect("/")
def results(request,id):
    if request.user.is_authenticated:
        result= Result.objects.filter()
        return render(request,"result.html",{"details":result,"name":"Result"})
    else:
        return redirect("/")   
def add_tests(request):
    if request.user.is_authenticated:
        obj = Test(idbatch=request.POST['id'],subject=request.POST['subject'],topic=request.POST['topic'],start_time=request.POST['start_time'],end_time=request.POST['end_time'],dates=request.POST['dates'])
        obj.save()
        test= Test.objects.filter()
        return render(request,"test.html",{"details":test,"name":"Test"})
    else:
        return redirect("/")
def add_results(request):
    if request.user.is_authenticated:
        obj = Result(idstudent=request.POST['id'],subject=request.POST['subject'],obtain_marks=request.POST['obtain_marks'],total_marks=request.POST['total_marks'],rdate=request.POST['rdate'])
        obj.save()
        result= Result.objects.filter()
        return render(request,"result.html",{"details":result,"name":"Result"})
    else:
        return redirect("/")
def assignments(request,id):
    if request.user.is_authenticated:
        assignment= Assignment.objects.filter()
        return render(request,"assignment.html",{"details":assignment,"name":"Assignment"})
    else:
        return redirect("/")
def add_assignments(request):
    if request.user.is_authenticated:
        obj = Assignment(idbatch=request.POST['id'],subject=request.POST['subject'],topic=request.POST['topic'],issuedate=request.POST['issuedate'],duedate=request.POST['duedate'])
        obj.save()
        assignment= Assignment.objects.filter()
        return render(request,"assignment.html",{"details":assignment,"name":"Assignment"})
    else:
        return redirect("/")
def take_attendence(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            attentence= Teacher.objects.filter()
            return render(request,"attendence.html",{"details":attentence,"name":"Attendence"})
        elif request.user.is_staff:
            attentence = Student.objects.filter()
            return render(request,"attendence.html",{"details":attentence,"name":"Attendence"})
        else:
            attentence = Student.objects.filter()
            return render(request,"attendence.html",{"details":attentence,"name":"Attendence"})
    else:
        return redirect("/")
def attendence(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            attendence = TeacherAttendence.objects.filter(idteacher = request.user.id)
            return render(request,"attendence.html",{"ydetails":attendence,"name":"Attendence"})
        else:
            attendence = StudentAttendence.objects.filter(idstudent = request.user.id)
            return render(request,"attendence.html",{"ydetails":attendence,"name":"Attendence"})
    else:
        return render(request,"login.html")
def t_attendence(request):
    if request.method == "POST" and request.user.is_authenticated:
        teacher = Teacher.objects.all()
        for data in teacher:
            obj = TeacherAttendence.objects.create(idteacher = data.idteacher,dates = request.POST['dates'],is_present = request.POST[str(data.idteacher)])
        attentence= Teacher.objects.filter()
        return render(request,"attendence.html",{"details":attentence,"name":"Attendence"})
    else:
        return render(request,"login.html")
def s_attendence(request):
    if request.method == "POST" and request.user.is_authenticated:
        student = Student.objects.all()
        for data in student:
            obj = StudentAttendence.objects.create(idstudent = data.idstudent,dates = request.POST['dates'],is_present = request.POST[str(data.idstudent)],is_reject = 0)
        attentence= Student.objects.filter()
        return render(request,"attendence.html",{"details":attentence,"name":"Attendence"})
    else:
        return render(request,"login.html")
def setting(request):
    if request.user.is_authenticated:
        return render(request,"settings.html")
    else:
        return redirect("/")
def profile(request,id):
    if request.user.is_authenticated:
        
        try:
            if request.user.is_staff:
                d= User.objects.get(pk=id)
                data = Teacher.objects.get(username=d.username)
                return render(request,"profile.html",{"detail":data})
            else:
                d= User.objects.get(pk=id)
                data = Student.objects.get(username=d.username)
                return render(request,"profile.html",{"detail":data})
        except:
            data= User.objects.get(pk=id)
            return render(request,"profile.html",{"detail":data})
    else:
        return redirect("/")
def changepassword(request):
    if request.user.is_authenticated:
        print(request.POST)
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            obj = User.objects.get(username=request.user.username)
            obj.set_password(password)
            obj.save()
            return redirect("/")
        else:
             return redirect("index")  
def teachers(request,id):
    if request.user.is_authenticated:
        nteacher= User.objects.filter(is_staff=1,is_superuser=0,accepted=0)
        teacher= Teacher.objects.filter()
        return render(request,"teacher.html",{"details":nteacher,"detail":teacher,"name":"Teacher"})
    else:
        return redirect("/")
def students(request,id):
    if request.user.is_authenticated:
        nstudent= User.objects.filter(is_staff=0,is_superuser=0,accepted=0)
        student= Student.objects.filter()
        return render(request,"student.html",{"details":nstudent,"detail":student,"name":"Student"})
    else:
        return redirect("/")
def details(request,types,id):
    if request.user.is_authenticated:
        if types == "Teacher":
            detail = Teacher.objects.get(idteacher=id)
            return render(request,"details.html",{"detail":detail})
        elif types == "Student":
            detail = Student.objects.get(idstudent = id)
            return render(request,"details.html",{"detail":detail})
    else:
        return redirect("/")  
def salary(request,id):
    if request.user.is_authenticated:
        salary= Salary.objects.filter()
        return render(request,"salary.html",{"details":salary,"name":"Salary"})
    else:
        return redirect("/")
def add_salary(request):
    if request.user.is_authenticated:
        obj = Salary(iduser=request.POST['id'],amount=request.POST['amount'],month=request.POST['month'],year=request.POST['year'],dates=datetime.datetime.now())
        obj.save()
        salary= Salary.objects.filter()
        return render(request,"salary.html",{"details":salary,"name":"Salary"})
    else:
        return redirect("/")
def accept(request,id):
    if request.user.is_authenticated:
        obj = User.objects.get(pk=id)
        obj.accepted = 1
        obj.save()
        if obj.is_staff and (obj.is_superuser == False):
            teacher= User.objects.filter(is_staff=1,is_superuser=0,accepted=0)
            return render(request,"data.html",{"details":teacher,"name":"Teacher"})
        elif  (obj.is_staff == False) and (obj.is_superuser == False):
            student= User.objects.filter(is_staff=0,is_superuser=0,accepted=0)
            return render(request,"data.html",{"details":student,"name":"Student"})
        
    else:
        return redirect("/")
