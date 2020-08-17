from django.shortcuts import render,get_object_or_404, redirect
from .models import *   # Blog class를 가져온다.
from django.utils import timezone # 현재시간 저장
from .form import BlogForm


# Create your views here.

def list(request):
    blogs = Blog.objects.all()  # Blog class에 있는 객체를 모두 가져온다.
    
    return render(request, 'list.html',{'blogs':blogs})



def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)    # class이름, pk=primal key -> DB에 있는 id  # 안되면 404페이지 띄워주세요
    # 댓글
    comments=Comment.objects.filter(blog=blog)
    # 좋아요
    like_num = len(blog.like.all())
    return render(request, 'detail.html',{'blog':blog,'comments':comments,'likes':like_num}) # 객체를 blog에 저장해주세요 -> blog를 detail.html에 보내주세요

def commenting(request, blog_id):
    new_comment = Comment()
    new_comment.blog = get_object_or_404(Blog, pk = blog_id)
    new_comment.author = request.user 
    new_comment.body = request.POST.get('body')
    new_comment.save()
    return redirect('/blog/' + str(blog_id))


def new(request):   # 글을 만드는 작성 폼
# 1. 데이터가 입력된 후 제출 버튼을 누르고 데이터 저장 = POST방식
# 2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 = GET방식
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid(): # 값들이 유효한지 검사해주는 함수
            content = form.save(commit=False)   # 전부 다 저장하지 말고 잠깐 보류
            content.pub_date = timezone.now()
            content.save()
            return redirect('list')

    else:
        form = BlogForm()   # form이라는 함수에 빈 객체 담아준다
        return render(request, 'new.html', {'form':form})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']  # POST방식으로 온 title인 객체를 저장한다
    new_blog.pub_date = timezone.datetime.now() # 이 함수가 저장될 때의 시간을 저장해준다.
    new_blog.body = request.POST['body']    # name이 body인 HTML 태그 안에 있는 검볼을 가져와서 new_blog에 있는 body 컬럼에 저장한다
    new_blog.save() # 저장하는 메소드
    return redirect('/blog/'+str(new_blog.id))   # redirect는 이 안에 있는 url로 이동해주세요 라는 뜻

def edit(request,blog_id):  # 수정 폼 제공해주는 함수, 객체 id 필요
    edit_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html',{'blog':edit_blog})

def update(request,blog_id):
    update_blog = get_object_or_404(Blog, pk = blog_id)
    update_blog.title = request.POST['title'] 
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body = request.POST['body']   
    update_blog.save()
    return redirect('detail', update_blog.id)   # url 패스의 이름이랑 id값을 보내준다!

def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog, pk = blog_id)
    delete_blog.delete()    # 삭제하라는 명령!
    return redirect('list') # 삭제한 객체의 id를 물려받지 못한다. 4번을 삭제하면 4번 안나오고 5번 생성됨!

def like(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.like.add(request.user)
    blog.save()

    return redirect('/blog/'+str(blog_id))
