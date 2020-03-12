from django.db import models

class EvaluationPost(models.Model):
    timestamp = models.CharField(max_length=20)      #时间  
    teachername = models.CharField(max_length=20)       #老师名字
    teacherevaluation = models.CharField(max_length=50)     #评论
    likecount = models.IntegerField()       #评论点赞数
    isroll_call = models.BooleanField(blank=True)       #我认为老师喜欢点名
    isquality = models.BooleanField(blank=True)     #我认为老师教学质量高
    ishighscore = models.BooleanField(blank=True)       #我认为老师给分高
    isfunny = models.BooleanField(blank=True)       #我认为老师上课很有趣
    isrecommend = models.BooleanField(blank=True)       #我人我老师值得被推荐

    class Meta:
        ordering = ('-timestamp',)      #默认按照时间排序。

class TeacherInformationPost(models.Model):
    teachername = models.CharField(max_length=20)       #老师名称
    teacherclass = models.CharField(max_length=100)         #教的哪门课
    isprofessor = models.BooleanField(blank=True)       #是教授
    countisroll_call = models.IntegerField()        #多少人认为喜欢点名
    countisquality = models.IntegerField()      #多少人认为教学质量好
    countishighscore = models.IntegerField()        #多少人认为给分高
    countisfunny = models.IntegerField()        #多少人认为上课很有趣 
    countisrecommend = models.IntegerField()        #多少人认为老师值得被推荐