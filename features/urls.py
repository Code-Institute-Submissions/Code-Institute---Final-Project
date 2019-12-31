from django.urls import path

from . import views

app_name = 'features_main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='features'),
    path('<int:pk>/', views.FeatureView.as_view(), name='feature page'),
    path('<int:feature_id>/comment/', views.add_comment, name='add comment'),
    path('<int:feature_id>/vote/', views.vote, name='vote'),
    path('add_feature/', views.create_feature, name='add feature'),
]