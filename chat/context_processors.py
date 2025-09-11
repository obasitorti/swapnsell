from django.db.models import Q
from .models import Message, Conversation

def unread_messages_count(request):
    if request.user.is_authenticated:
        unread_count = Message.objects.filter(
            conversation__in=Conversation.objects.filter(
                Q(buyer=request.user) | Q(seller=request.user)
            ),
            is_read=False
        ).exclude(sender=request.user).count()
        return {"unread_count": unread_count}
    return {}
