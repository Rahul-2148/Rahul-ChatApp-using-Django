"""
contrib word in django is used to add extra features in django framework
Backend file h ye

Note: Delete single or delete selected or clear aa chat wala koi bhi delete related nhi bna paya mai😥
"""

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db.models import Q
from django.utils.dateformat import DateFormat
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def chatRoom(request, username):
    receiver = User.objects.filter(username=username).first() #.first means get the first object
    
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=request.user))
    ).order_by('timestamp')
    
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Message.objects.create(sender=request.user, receiver=receiver, content=message)

    return render(request, 'chat/chat.html', {'receiver': receiver, 'messages': messages})

@login_required
def get_messages(request, username):
    receiver = get_object_or_404(User, username=username)

    # First mark unread messages (received by current user from receiver)
    Message.objects.filter(sender=receiver, receiver=request.user, is_read=False).update(is_read=True)

    # Then fetch fresh queryset (to include updated is_read values)
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=receiver) | Q(sender=receiver, receiver=request.user)
    ).order_by('timestamp')

    messages_data = [{
        "sender": message.sender.username,
        "receiver": message.receiver.username,
        "content": message.content,
        "timestamp": DateFormat(message.timestamp).format("H:i"),
        "is_read": message.is_read,
        "id": message.id
    } for message in messages]

    return JsonResponse({"message": messages_data})


@csrf_exempt
@login_required
def send_message(request, username):
    if request.method == 'POST':
        receiver = User.objects.filter(username=username).first()
        content = request.POST.get('msg')  # JS fetch sends 'msg='
        if receiver and content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return HttpResponse("Message sent")
    return HttpResponse("Invalid request", status=400)

# @csrf_exempt
# def delete_message(request):
#     data = json.loads(request.body)
#     message = Message.objects.get(id=data['id'], sender=request.user)
#     message.delete()
#     return JsonResponse({'status': 'success'})

# @csrf_exempt
# def delete_selected_messages(request):
#     data = json.loads(request.body)
#     Message.objects.filter(id__in=data['ids'], sender=request.user).delete()
#     return JsonResponse({'status': 'success'})

# @csrf_exempt
# def clear_chat(request, username):
#     receiver = User.objects.get(username=username)
#     Message.objects.filter(
#         sender=request.user,
#         receiver=receiver
#     ).delete()
#     return JsonResponse({'status': 'success'})