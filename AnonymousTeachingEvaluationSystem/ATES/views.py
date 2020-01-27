from django.shortcuts import render
from ATES import models
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from ATES.models import EvaluationPost,TeacherImformationPost
from django.utils import timezone
from django.db.models import F,aggregates
import datetime
def like_add(request):
    string = request.POST.get('timestamp')
    stringlist = string.split('.')
    stringlist[1] = stringlist[1][:6]
    string = '.'.join(stringlist)
    print(string)
    teachers = models.EvaluationPost.objects.filter(timestamp=string)
    teachers.update(likecount = F('likecount') + 1)
    teacher = teachers.first()
    Dict = {'New':str(teacher.likecount)}
    return JsonResponse(Dict)

def homepage(request):
    return render(request,'homepage.html')

def searchinformation(request):
    if request.method == 'POST':
        searchname = request.POST.get("searchname")
        searchtype = request.POST.get("radio")
        if searchtype == "teachername":
            request.session["teachername"] = searchname
            teacherinformation = models.TeacherImformationPost.objects.filter(teachername = searchname)
            evaluations = models.EvaluationPost.objects.filter(teachername = searchname).order_by('-likecount')
            count = evaluations.count()
            return render(request, 'teacherinformation.html', {'teacherinformation':teacherinformation,'evaluations':evaluations,'teachername':searchname,'count':count})
        else:
            teacherinformation = models.TeacherImformationPost.objects.filter(teacherclass = searchname)
            count = []
            for teacher in teacherinformation:
                evaluations = models.EvaluationPost.objects.filter(teachername = teacher.teachername)
                count.append(evaluations.count())
            zipdata = zip(teacherinformation,count)
            return render(request, 'searchteacher.html', {'zipdata':zipdata})

def sortby(request):
    if request.method == 'POST':
        if (request.POST.get("sortby")) == '最新回复':
            teachername = request.session["teachername"]
            teacherinformation = models.TeacherImformationPost.objects.filter(teachername = teachername)
            evaluations = models.EvaluationPost.objects.filter(teachername = teachername).order_by('-timestamp')
            count = evaluations.count()
            return render(request, 'teacherinformation.html', {'teacherinformation':teacherinformation,'evaluations':evaluations,'teachername':teachername,'count':count})
        if (request.POST.get("sortby")) == '点赞量':
            teachername = request.session["teachername"]
            teacherinformation = models.TeacherImformationPost.objects.filter(teachername = teachername)
            evaluations = models.EvaluationPost.objects.filter(teachername = teachername).order_by('-likecount')
            count = evaluations.count()
            return render(request, 'teacherinformation.html', {'teacherinformation':teacherinformation,'evaluations':evaluations,'teachername':teachername,'count':count})

def createinformation(request):
    if request.method == 'POST':
        teacher = EvaluationPost()
        teachername = request.session["teachername"]
        TeacherImformation = models.TeacherImformationPost.objects.get(teachername=teachername)
        teacher.timestamp = datetime.datetime.now()
        teacher.teachername = teachername
        teacher.teacherevaluation = request.POST.get("evaluation")
        teacher.likecount = 0
        if request.POST.getlist("isroll_call"):
            teacher.isroll_call = True
            TeacherImformation.countisroll_call += 1
        else:
            teacher.isroll_call = False
        if request.POST.getlist("isquality"):
            teacher.isquality = True
            TeacherImformation.countisquality += 1
        else:
            teacher.isquality = False
        if request.POST.get("ishighscore"):
            teacher.ishighscore = True
            TeacherImformation.countishighscore += 1
        else:
            teacher.ishighscore = False
        if request.POST.get("isfunny"):
            teacher.isfunny = True
            TeacherImformation.countisfunny += 1
        else:
            teacher.isfunny = False
        if request.POST.get("isrecommend"):
            teacher.isrecommend = True
            TeacherImformation.countisrecommend += 1
        else:
            teacher.isrecommend = False
        teacher.save()
        TeacherImformation.save()
        teacherinformation = models.TeacherImformationPost.objects.filter(teachername = teacher.teachername)
        evaluations = models.EvaluationPost.objects.filter(teachername = teacher.teachername)
        count = evaluations.count()
    return render(request, 'teacherinformation.html', {'teacherinformation':teacherinformation,'evaluations':evaluations,'teachername':teacher.teachername,'count':count})
