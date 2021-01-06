from django.conf.urls import url,include
from .views import employee,project,rankingCreteria,employeeRating,login,changepassword
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as auth_views
from django.urls import path
router = SimpleRouter()
router.register(r'project', project.ProjectList,basename='project')

urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^employee/list/$', employee.EmployeeList.as_view(), name='employeeList'),
    url(r'^employee/show/(?P<pk>\d+)/$', employee.EmployeeShow.as_view(), name='empDetail'),
    url(r'^ranking-creteria/list/$',rankingCreteria.RankingCreateriaList.as_view(),name='rankingCreteria'),
    url(r'^ranking-creteria/show/(?P<pk>\d+)/$',rankingCreteria.RankingCreateriaShow.as_view()),
    url(r'^employee-rating/list/$', employeeRating.EmployeeRatingList.as_view()),
    url(r'^employee-rating/show/(?P<pk>\d+)/$', employeeRating.EmployeeRatingShow.as_view()),
    url(r'^login/$',login.LoginApiView.as_view()),
    url(r'^logout/$', login.Logout.as_view()),
    url(r'^change-password/$',changepassword.ChangePassword.as_view()),
]
schema_view = get_swagger_view(title='Employee ManageMent API')
urlpatterns += url(r'^api-docs/$', schema_view),
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)