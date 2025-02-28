from django.shortcuts import render,redirect
from . models import JobSeeker,Login,Employer,Enquiry,Jobs
import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render (request,'about.html')
def jobseekerreg(request):
    return render (request,'jobseekerreg.html')
def employerreg(request):
    return render (request,'employerreg.html')
def login(request):
    return render(request,'login.html')
def contact(request):
    return render(request,'contact.html')
def jsreg(request):
    name=request.POST
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    dob=request.POST['dob']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    keyskills=request.POST['keyskills']
    regdate=datetime.datetime.today()
    password=request.POST['password']
    usertype='jobseeker'
    js=JobSeeker(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,dob=dob,qualification=qualification,experience=experience,keyskills=keyskills,regdate=regdate)
    log=Login(userid=emailaddress,password=password,usertype=usertype)
    js.save()
    log.save()
    msg='registration is successfully'
    return render(request,'jobseekerreg.html',{'msg':msg})

def ereg(request):
    firmname=request.POST['firmname']
    firmwork=request.POST['firmwork']
    firmaddress=request.POST['firmaddress']
    cpname=request.POST['cpname']
    cpcontactno=request.POST['cpcontactno']
    cpemailaddress=request.POST['cpemailaddress']
    aadharno=request.POST['aadharno']
    panno=request.POST['panno']
    gstno=request.POST['gstno']
    regdate=datetime.datetime.today()
    password=request.POST['password']
    usertype='employer'
    e=Employer(firmname=firmname,firmwork=firmwork,firmaddress=firmaddress,cpname=cpname,cpcontactno=cpcontactno,cpemailaddress=cpemailaddress,aadharno=aadharno,panno=panno,gstno=gstno,regdate=regdate)
    log=Login(userid=cpemailaddress,password=password,usertype=usertype)
    e.save()
    log.save()
    msg='registration is successfully'
    return render(request, 'employerreg.html', {'msg': msg})
def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    posteddate=datetime.datetime.today()
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,posteddate=posteddate)
    enq.save()
    msg='enquiry submittion successfull'
    return render(request,'contact.html',{'msg':msg})
def validate(request):
    userid=request.POST['userid']
    password=request.POST['password']
    usertype=request.POST['usertype']
    try:
        obj=Login.objects.get(userid=userid,password=password)
        if obj.usertype=='employer':
            request.session['employer']=userid
            return redirect('emphome')
    except:
        msg='invalid user'
    return render(request,'login.html',{'msg':msg})
def emphome(request):
    return render(request,'emphome.html')
def postjob(request):
    try:
        if request.session['employer']:
            return render(request,'postjob.html')
    except:
        return render(request,'login.html')
def manageapp(request):
    try:
        if request.session['employer']:
            return render(request,'manageapp.html')
    except:
        return render(request,'login.html')
def empchangepassword(request):
    try:
        if request.session['employer']:
            return render(request,'empchangepassword.html')
    except:
        return render(request,'login.html')
def emplogout(request):
    request.session['employer']=None
    return render(request,'login.html')
def pjob(request):
    obj=Employer.objects.get(cpemailaddress=request.session['employer'])
    firmname=obj.firmname
    emailaddress=obj.cpemailaddress
    jobtitle=request.POST['jobtitle']
    post=request.POST['post']
    jobdesc=request.POST['jobdesc']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    location=request.POST['location']
    salarypa=request.POST['salarypa']
    posteddate=datetime.datetime.today()
    j=Jobs(firmname=firmname,jobtitle=jobtitle,post=post,jobdesc=jobdesc,qualification=qualification,experience=experience,location=location,salarypa=salarypa,posteddate=posteddate,emailaddress=emailaddress)
    j.save()
    msg='job is posted'
    return render(request,'postjob.html',{'msg':msg})
def empchangepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg='message='
    if newpassword!=confirmpassword:
        msg=msg+'Newpassword and Confirmpassword are not equal'
        return render(request,'empchangepassword.html',{'msg':msg})
    userid=request.session['employer']
    usertype='employer'
    try:
        obj=Login.objects.get(userid=userid,password=oldpassword,usertype=usertype)
        log=Login(userid=userid,password=newpassword,usertype=usertype)
        log.save()
        return redirect('emplogout')
    except:
        msg=msg+'Old Password is not matched'
    return render(request,'empchangepassword.html',{'msg':msg})



