from django.shortcuts import render
from ATES import models
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from ATES.models import EvaluationPost,TeacherInformationPost
from django.utils import timezone
from django.db.models import F,aggregates
import datetime
from .ATESSerializers import EvaluationPostSerializer, TeacherInformationPostSerializer
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework.renderers import TemplateHTMLRenderer
import json

class TeacherViewSet(ModelViewSet):

    queryset = TeacherInformationPost.objects.all()
    serializer_class = TeacherInformationPostSerializer

    @action(method=['get'],detail = True)
    def classes(self,request,pk):
        teachers = TeacherInformationPost.objects.filter(teacherclass=pk)
        teachers = TeacherInformationPostSerializer(teachers,many = True)
        return Response(teachers.data)

    @action(methods=['get'],detail = True)
    def getlist(self,request,pk):
        teacher = TeacherInformationPost.objects.get(teachername=pk)
        teacher = TeacherInformationPostSerializer(teacher)
        return Response(teacher.data)

class EvaluationViewSet(ModelViewSet):
    
    queryset = EvaluationPost.objects.all()
    serializer_class = EvaluationPostSerializer
    @action(methods=['post'],detail= False)
    def update(self,request):
        d = {}
        a = request.data
        d['teachername']=a['teachername']
        d['timestamp']=str(datetime.datetime.now())[:19]
        d['likecount']=0
        d['isroll_call']=True if 'isroll_call' in  a['check'] else False
        d['isquality']=True if 'isquality' in  a['check'] else False
        d['ishighscore']=True if 'ishighscore' in  a['check'] else False
        d['isfunny']=True if 'isfunny' in  a['check'] else False
        d['isrecommend']=True if 'isrecommend' in  a['check'] else False
        d['teacherevaluation']=a['evaluation']
        serializer = EvaluationPostSerializer(data = d)
        if  serializer.is_valid():
            serializer.create(serializer.validated_data)
        teacher = TeacherInformationPost.objects.get(teachername = a['teachername'])
        teacher.countisroll_call += 1 if 'isroll_call' in  a['check'] else 0
        teacher.countisquality += 1 if 'isquality' in  a['check'] else 0
        teacher.countishighscore += 1 if 'ishighscore' in  a['check'] else 0
        teacher.countisfunny += 1 if 'isfunny' in  a['check'] else 0
        teacher.countisrecommend += 1 if 'isrecommend' in  a['check'] else 0
        teacher.save()

        return Response('Success!')

    @action(methods=['get'],detail=True)
    def ilike(self,request,pk):
        evaluation = EvaluationPost.objects.get(timestamp=pk)
        evaluation.likecount +=1
        evaluation.save()
        evaluation = EvaluationPostSerializer(evaluation)
        return Response(evaluation.data)

    @action(methods=['get'],detail= True)
    def sortbyzxhf(self,request,pk):
        evaluation = EvaluationPost.objects.filter(teachername=pk).order_by('-timestamp')
        evaluation = EvaluationPostSerializer(evaluation,many = True)
        return Response(evaluation.data)
    
    @action(methods=['get'],detail= True)
    def sortbydzl(self,request,pk):
        evaluation = EvaluationPost.objects.filter(teachername=pk).order_by('-likecount')
        evaluation = EvaluationPostSerializer(evaluation,many = True)
        return Response(evaluation.data)

