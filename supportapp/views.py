from django.shortcuts import render,redirect, get_object_or_404 
from mainapp.models import *
from .models import *
from django.contrib import auth
# Create your views here.

def custom_voice(request):
    a = reversed(Qna.objects.all())
    return render(request, 'custom_voice.html', {'qna': a})

    

def custom_voice_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'pic' in request.FILES:
            aa = Qna.objects.filter(user = request.user)
            qna = Qna()
            qnacontent = request.POST.get('q_content')
            qnatitle = request.POST.get('q_title')
            qnatype = request.POST.get('q_type')
            qnaboxcode = request.POST.get('q_boxcode')
            qnatime = request.POST.get('q_time')
            qnapublic = request.POST.get('public')
            qnaanswer = request.POST.get('answers')
            pic = request.FILES['pic']

            qna.q_content = qnacontent
            qna.q_title = qnatitle
            qna.q_type =qnatype
            qna.q_boxcode =qnaboxcode 
            qna.q_time =qnatime 
            qna.public =qnapublic
            qna.pic = pic
            qna.answers = qnaanswer
            qna.user = request.user
            qna.save()
            return redirect('custom_voice')

        elif request.method == 'POST':
            aa = Qna.objects.filter(user = request.user)
            qna = Qna()
            qnacontent = request.POST.get('q_content')
            qnatitle = request.POST.get('q_title')
            qnatype = request.POST.get('q_type')
            qnaboxcode = request.POST.get('q_boxcode')
            qnatime = request.POST.get('q_time')
            qnapublic = request.POST.get('public')
            qnaanswer = request.POST.get('answers')

            qna.q_content = qnacontent
            qna.q_title = qnatitle
            qna.q_type =qnatype
            qna.q_boxcode =qnaboxcode 
            qna.q_time =qnatime 
            qna.public =qnapublic
            qna.answers = qnaanswer
            
            qna.user = request.user
            qna.save()
            return redirect('custom_voice')
        return render(request, 'custom_voice_new.html')
    else:
        return redirect('login')

    



def custom_voice_detail(request, pk):
    #if request.method == 'GET':
    aa = get_object_or_404(Qna, pk = pk)
    aa.today = aa.today +1
    aa.save()
    #post_id = request.POST.get('post_id') #히든인풋을 post_id로 저장
    #aa = Qna.objects.POST.get(id = post_id)
    return render(request, 'custom_voice_detail.html',{'aa':aa})


def deletevoice(request): 
    post_id = request.GET['post_id'] 
    post = Qna.objects.get(id = post_id)
    post.delete() #타이틀이나 컨텐츠 저장할 필요없이 삭제만 해주면됨
    return redirect( 'custom_voice')


def custom_voice_edit(request): #post로 받아오자
    if request.method == 'POST' and 'pic' in request.FILES:
        post_id = request.POST['post_id'] #히든인풋을 post_id로 저장
        aa = Qna.objects.get(id=post_id)#그걸 id로 받아서 오브젝트로 받아옴
        qnacontent = request.POST.get('q_content')
        qnatitle = request.POST.get('q_title')
        qnatype = request.POST.get('q_type')
        qnaboxcode = request.POST.get('q_boxcode')
        qnatime = request.POST.get('q_time')
        qnapublic = request.POST.get('public')
        qnaanswer = request.POST.get('answers')
        pic = request.FILES['pic']
        
        aa.q_content = qnacontent
        aa.q_title = qnatitle
        aa.q_type =qnatype
        aa.q_boxcode =qnaboxcode 
        aa.q_time =qnatime 
        aa.public =qnapublic
        aa.answers = qnaanswer
        aa.pic = pic
        aa.user = request.user
        aa.save()
        return redirect('custom_voice')

    elif request.method == 'POST':
        post_id = request.POST['post_id']
        aa = Qna.objects.get(id=post_id)
        qnacontent = request.POST.get('q_content')
        qnatitle = request.POST.get('q_title')
        qnatype = request.POST.get('q_type')
        qnaboxcode = request.POST.get('q_boxcode')
        qnatime = request.POST.get('q_time')
        qnapublic = request.POST.get('public')

        aa.q_content = qnacontent
        aa.q_title = qnatitle
        aa.qnatype =qnatype
        aa.q_boxcode =qnaboxcode 
        aa.q_time =qnatime 
        aa.public =qnapublic
        aa.user = request.user
        aa.save()
        return redirect('custom_voice')

    else :
        post_id = request.GET['post_id']
        aa = Qna.objects.get(id = post_id )
        return render(request, 'custom_voice_edit.html', { 'aa' : aa })
        

    