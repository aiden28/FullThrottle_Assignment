from django.shortcuts import render
from .models import Member,Activity
from django.http import HttpResponse


def index(request):
    return render(request,'home.html')

def insert(request):
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        country=request.POST.get('country')
        city=request.POST.get('city')
        sDate=request.POST.get('sDate')
        edate=request.POST.get('eDate')
        sTime=request.POST.get('sTime')
        eTime=request.POST.get('eTime')
        print(country)
        try:
            obj=Member.objects.get(id=id)
            q=Activity(id1=obj,startDate=sDate,endDate=edate,startTime=sTime,endTime=eTime)
            q.save()
        except:
            q1=Member(id=id,name=name,country=country,city=city)
            q1.save()
            q2=Activity(id1=Member.objects.get(id=id),startDate=sDate,endDate=edate,startTime=sTime,endTime=eTime)
            q2.save()
        return render(request,'home.html')


    else:
        return render(request,'insert.html')
def selectId(request):
    return render(request,'viewACtivities.html')

def viewActivities(request):
    id=request.GET['id']
    print(id)
    f=5
    f1=4
    try:
        obj=Member.objects.get(id=id)
        ob=Activity.objects.filter(id1=id)
        print(ob)
        print(obj.id)
        print(obj.name)
        print(obj.country)
        print(obj.city)
        id=obj.id
        name=obj.name
        country=obj.country
        city=obj.city
        sDate=[]
        eDate=[]
        sTime=[]
        eTime=[]
        for i in ob:
            sDate.append(i.startDate)
            eDate.append(i.endDate)
            sTime.append(i.startTime)
            eTime.append(i.endTime)
        print(sDate)
        n=len(sDate)
        r=range(1,n+1)
        for i in r:
            print(i)
        data=zip(r,sDate,eDate,sTime,eTime)
        return render(request,'data.html',{'f':f,'f1':f1,'id':id,'name':name,'c':country,'city':city,'data':data})
    except:
        f1=6
        return render(request,'data.html',{'f':f,'f1':f1})







