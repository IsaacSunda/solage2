from django.urls import path
from school.views import HomePage, registration, FormDetail, FromList, Thank, Upate
from . import views

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("registration/create/", registration.as_view(), name="fo_create"),
    path("registration/<int:pk>/", FormDetail.as_view(), name="formdetail"),
    path("reg/", FromList.as_view(), name="form"),
    path("Thanks", Thank.as_view(), name="thank"),
    path("search_result",views.search_result,name="search_result"),
    path("update/<int:pk>/", Upate.as_view(), name="update")
]
