from django.urls import path
from . import views
from .views import CommentCreateView, CommentDeleteView


app_name='comments'

urlpatterns = [
    path('<int:event_pk>/ajouter_comment', CommentCreateView.as_view(), name='ajouter_comment'),
    path('<int:event_pk>/supprimer_comment', CommentDeleteView.as_view(), name='supprimer_comment'),
]