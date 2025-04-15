from django.urls import path
from . import views
from .views import CommentCreateView, CommentDeleteView


app_name='comments'

urlpatterns = [
    path('ajouter_comment/<str:titre>', CommentCreateView.as_view(), name='ajouter_comment'),
    path('supprimer_comment/', CommentDeleteView.as_view(), name='supprimer_comment'),
]