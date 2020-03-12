from ATES import views
from django.urls import path,re_path
from django.views.generic import TemplateView
urlpatterns = [
    re_path(r'^teacherinformation/$',views.EvaluationViewSet.as_view({'post':'update'})),
    re_path(r'^teacherinformation/(?P<pk>[\u4e00-\u9fa5_a-zA-Z0-9%]+)/$',views.TeacherViewSet.as_view({'get':'getlist'})),
    re_path(r'^teacherinformation/evaluation/dzl/(?P<pk>[\u4e00-\u9fa5_a-zA-Z0-9%]+)/$',views.EvaluationViewSet.as_view({'get':'sortbydzl'})),
    re_path(r'^teacherinformation/evaluation/zxhf/(?P<pk>[\u4e00-\u9fa5_a-zA-Z0-9%]+)/$',views.EvaluationViewSet.as_view({'get':'sortbyzxhf'})),
    re_path(r'^teacherinformation/evaluation/dz/(?P<pk>\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})/$',views.EvaluationViewSet.as_view({'get':'ilike'})),
    re_path(r'^classinformation/(?P<pk>[\u4e00-\u9fa5_a-zA-Z0-9%]+)/$',views.TeacherViewSet.as_view({'get':'classes'}))
]
