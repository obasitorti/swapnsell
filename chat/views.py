from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Conversation, Message
from swapandsell.models import Product

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(
        buyer=request.user
    ) | Conversation.objects.filter(
        seller=request.user
    )
    return render(request, "chat/inbox.html", {"conversations": conversations})


@login_required
def start_conversation(request, product_id, seller_id):
    product = get_object_or_404(Product, id=product_id)
    seller = get_object_or_404(User, id=seller_id)

    # If conversation already exists, reuse it
    conversation, created = Conversation.objects.get_or_create(
        buyer=request.user,
        seller=seller,
        product=product
    )
    return redirect("chat:conversation_detail", pk=conversation.pk)


@login_required
def conversation_detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)

    # Security check
    if request.user not in [conversation.buyer, conversation.seller]:
        return redirect("chat:inbox")

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Message.objects.create(conversation=conversation, sender=request.user, text=text)
            return redirect("chat:conversation_detail", pk=pk)

    messages = conversation.messages.all()
    return render(request, "chat/conversation_detail.html", {"conversation": conversation, "messages": messages})
