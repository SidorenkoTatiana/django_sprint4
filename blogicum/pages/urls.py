from django.urls import path
from .views import StaticPageView, RulesView

app_name = 'pages'

urlpatterns = [
    path('about/', StaticPageView.as_view(), name='about'),
    path('rules/', RulesView.as_view(), name='rules'),
]
