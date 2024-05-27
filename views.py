from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from proApp import dbconnection
from proApp import prediction
from django.core.files.storage import FileSystemStorage
from datetime import date

# Create your views here.
def home(request):  
    return render(request,'index.html',{})
def predict(request): 
    if request.method=='POST':
        Text_input =request.POST.get("nws") 
        Text_input =request.POST.get("nws") 
        print(type(Text_input))
        #print(Text_input)
        pr=int(prediction.predict(Text_input))
        #print(pr)
        qry="select * from user_revw order by id desc"
        data=dbconnection.selectalldata(qry)
        return render(request,'predict.html',{'nws':Text_input,'data':data,'pr':pr})
    qry="select * from user_revw order by id desc"
    data=dbconnection.selectalldata(qry)
    return render(request,'predict.html',{'data':data})
def addrating(request):  
    if request.method=='POST':
        n =request.POST.get("nme") 
        cmnt =request.POST.get("cmnt") 
        rt =request.POST.get("rt") 
        import datetime
        x = datetime.datetime.now()
        qry="INSERT INTO `user_revw`(`nme`, `cmnt`, `rat`, `dt`) VALUES ('"+n+"','"+cmnt+"','"+rt+"','"+str(x)+"')"
        dbconnection.insertdata(qry)
        return HttpResponseRedirect("http://127.0.0.1:8000/predict/")
    return render(request,'predict.html',{})