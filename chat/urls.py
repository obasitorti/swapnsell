from django.urls import path
from .import views

app_name = "chat"

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("conversation/<int:pk>/", views.conversation_detail, name="conversation_detail"),
    path("start/<int:product_id>/<int:seller_id>/", views.start_conversation, name="start_conversation"),
]
