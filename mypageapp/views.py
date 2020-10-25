from django.shortcuts import render,redirect, redirect,get_object_or_404
from django.contrib import auth
from mainapp.models import *
from .models import *
from django.db.models import Max 
import random,string
# Create your views here.
def post_search(request): 
    return render(request, 'post_search.html')

def post_search_detail(request):
    code = request.POST["code"]
    box = Box.objects.filter(code = code)
    if not box:
        return render(request,'post_search.html',{'error':'존재하지 않는 송장번호입니다.'})
    else :
        state = reversed(State.objects.filter(box = box[0]))
        states = reversed(State.objects.filter(box = box[0]))
        return render(request,'post_search_detail.html',{'box':box,'state': state,'states':states})
    
def timeline(request):#비로그인시에도 넘겨줄수있도록
    if request.user.is_authenticated:
        yoo = get_object_or_404(User, username=request.user)
        name = yoo.name
        mybox= Box.objects.filter(receiver = name)|Box.objects.filter(sender=name)
        state=State.objects.filter(box_latest= True)
        return render(request, 'timeline.html',{'mybox':mybox,'state':state})
    else:
        return redirect('login')
def mypage(request):
    if request.user.is_authenticated:
        return render(request,'mypage.html')
    else:
        return redirect('login')

def post_reservation(request):
    boxes=Box.objects.all()
    _LENGTH = 8 # 자리수 설정
    string_pool = string.digits # "0123456789" 
    result = "" # 결과 값 
    loop=True
    while loop:
        loop=False
        for i in range(_LENGTH) : # 랜덤한 하나의 숫자를 뽑아서, 문자열 결합을 한다.
            result += random.choice(string_pool)
        for boxes in boxes:
            if boxes.code==result: #코드 중복값 있으면 다시 loop돌리기
                loop=True
        code=result

    if request.method == 'POST':
        box = Box()
        box.box_type=True
        box.code=code
        box.company='롯데택배'

        box.sender=request.POST['sender']
        box.sender_phone=request.POST['sender_phone']
        box.sender_address=request.POST['sender_address']
        box.visit_date=request.POST['visit_date']
        box.receiver=request.POST['receiver']
        box.receiver_phone=request.POST['receiver_phone']
        box.receiver_address=request.POST['receiver_address']
        box.box_detail=request.POST['box_detail']
        
        box.box_amount=request.POST['box_amount']
        box.box_size=request.POST['box_size']
        box.box_value=request.POST['box_value']
        box.box_pay=request.POST['box_pay']

        box.box_step='1'
        box.worker="미정"
        box.worker_phone="010-"
        box.save()
        return redirect('post_reserve_look')#조회로넘어가게
    return render(request,'post_reservation.html')

def post_reserve_look(request):
    if request.user.is_authenticated:
        yoo = get_object_or_404(User, username=request.user)
        name = yoo.name
        mybox=reversed(Box.objects.filter(sender=name))
        return render(request,'post_reserve_look.html',{'mybox':mybox})
    else:
        return redirect('login')

def post_reserve_delete(request):
    mybox_id = request.POST['mybox_id']
    mybox = Box.objects.get(id = mybox_id)
    mybox.delete()
    return redirect('post_reserve_look')

def post_reserve_look_detail(request,pk):
    if request.user.is_authenticated:
        mybox = Box.objects.filter(pk = pk)
        return render(request,'post_reserve_look_detail.html',{'mybox':mybox})
    else:
        return redirect('login')
