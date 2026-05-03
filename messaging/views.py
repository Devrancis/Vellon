from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Conversation, Message
from products.models import Product

@login_required
def conversation_list_view(request):
    conversations = Conversation.objects.filter(
        Q(buyer=request.user) | Q(seller=request.user)
    ).order_by('-updated_at')
    return render(request, 'messaging/inbox.html', {'conversations': conversations})

@login_required
def chat_detail_view(request, pk):
    conversation = get_object_or_404(Conversation.objects.select_related('buyer', 'seller', 'product'), pk=pk)
    
    # Permission check
    if request.user != conversation.buyer and request.user != conversation.seller:
        messages.error(request, "Access denied.")
        return redirect('inbox')
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=content
            )
            # Update updated_at timestamp
            conversation.save() 
            return redirect('chat_detail', pk=pk)

    messages_list = conversation.messages.all()
    # Mark messages as read
    conversation.messages.filter(~Q(sender=request.user), read=False).update(read=True)
    
    return render(request, 'messaging/chat.html', {
        'conversation': conversation,
        'messages_list': messages_list
    })

@login_required
def start_conversation_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.store.owner == request.user:
        messages.info(request, "This is your own product.")
        return redirect('product_detail', slug=product.slug)
    
    conversation, created = Conversation.objects.get_or_create(
        buyer=request.user,
        seller=product.store.owner,
        product=product
    )
    return redirect('chat_detail', pk=conversation.pk)
