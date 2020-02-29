"""dipleo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.conf import settings
from user.views import *
from company.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', UsersList.as_view()),
    url(r'user_profile', UserProfile.as_view()),
    url(r'user_profile/<int:user_id>', UserProfile.as_view()),
    url(r'login', Login.as_view()),
    url(r'add_company', CompanyList.as_view()),
    url(r'add_job', JobList.as_view()),
    url(r'add_job/<int:job_id>', JobList.as_view()),
    url(r'job_search', JobSearch.as_view()),
    url(r'apply_jobs', ApplyJobs.as_view()),
    url(r'apply_jobs/<int:user_id>', ApplyJobs.as_view()),
    url(r'save_jobs', SavedJobs.as_view()),
    url(r'save_jobs/<int:user_id>', SavedJobs.as_view()),
    url(r'top_jobs', showTopJobs.as_view()),
    url(r'change_password', ChangePassword.as_view())

]
