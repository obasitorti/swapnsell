from .models import Message

def unread_messages_count(request):
    if request.user.is_authenticated:
        return {
            "unread_count": Message.objects.filter(receiver=request.user, is_read=False).count()
        }
    return {"unread_count": 0}
