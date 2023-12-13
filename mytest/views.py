from django.shortcuts import render, redirect
from mytest.models import Post, Mood

# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    
    elif request.method == 'POST':
        try:
            user_id = request.GET['user_id']
            user_pass = request.GET['user_pass']
            user_post = request.GET['user_post']
            user_mood = request.GET['mood']
            mood = Mood.objects.get(status=user_mood)
            post = Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            message=f'成功儲存！請記得你的編輯密碼[{user_pass}]!，訊息需經審查後才會顯示。'.format(user_pass)
            return redirect("test-new")
        except:
            message = '出現錯誤'
            return render(request, 'myform.htnl', locals())

    else:
        massage=f'post/get 出現錯誤'
        return render(request, 'myform.html', locals())