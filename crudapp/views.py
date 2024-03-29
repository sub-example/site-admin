from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import TestForm, InfoModelFormAdd, SignUpForm
from .models import InfoModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    my_dict = {
        'goal':'CRUD機能搭載のアプリを作成する',
        'limit_term':'11/22(Thr)',
        'name':'yusuke',
        'form':TestForm(),
        'insert_forms':'ここに入力内容が表示されます',
    }
    
    if (request.method == 'POST'):
        my_dict['insert_forms'] = 'もじ：'+request.POST['text'] +'<br>整数型：'+request.POST['num'] + '<br>メールアドレス:'+request.POST['email']
        my_dict['form'] = TestForm(request.POST)
    return render(request,'crudapp/index.html',my_dict)

def info(request):
    infodata = InfoModelForm.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    my_dict2 = {
        'title':'テストタイトル',
        'val':infodata,
        'header':header,
    }
    
    return render(request, 'crudapp/info.html',my_dict2)

def create(request):
    if (request.method == 'POST'):
        obj = InfoModelForm()
        info = InfoModelFormAdd(request.POST,instance=obj)
        info.save()
        return redirect(to='/info')
    
    modelform_dict = {
        'title':'データを入力してください',
        'form':InfoModelFormAdd(),
    }
    return render(request, 'crudapp/create.html',modelform_dict)

def update(request,num):
    obj = InfoModelForm.objects.get(id=num)
    
    if (request.method == 'POST'):
        info = InfoModelFormAdd(request.POST, instance=obj)
        info.save()
        return redirect(to='/info')
    update_dict = {
        'title':'登録情報更新画面',
        'id':num,
        'form':InfoModelFormAdd(instance=obj),
    }
    return render(request,'crudapp/update.html',update_dict)

def delete(request,num):
    obj = InfoModelForm.objects.get(id=num)
    if (request.method == 'POST'):
        obj.delete()
        return redirect(to='/info')
    delete_dict = {
        'title':'削除確認',
        'id':num,
        'obj':obj,
    }
    return render(request,'crudapp/delete.html',delete_dict)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crudapp:index')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'crudapp/signup.html',context)

@login_required
def detail(request,question_id):
    user = request.user
    question = get_object_or_404(Question,pk=question_id)
    
    if request.method == 'POST':
        form = VoteForm(request.POST,question=question)
        if form.is_valid():
            form.save()
            return redirect('crudapp:results', question_id=question.id)
    else:
        form = VoteForm(question=question)
    context={'user':user, 'question':question,'form':form}
    return render(request,"crudapp/detail.html",context)