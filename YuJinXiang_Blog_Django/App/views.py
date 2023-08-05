from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from App.models import *
from datetime import datetime


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render(request, 'front/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponse('--用户名或密码错误--')
        else:
            login(request, user)
            return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def index_view(request):
    boards = BoardModel.objects.all()

    board_id = request.GET.get('board_id', default=0)

    if board_id:
        board = BoardModel.objects.get(id=board_id)

    q = request.GET.get('q')
    page = request.GET.get('page', default=1)

    query_obj = PostModel.objects.filter(is_active=True).order_by('-is_topping', '-create_time', 'id')

    if q:
        query_obj = query_obj.filter(title__contains=q)
    if board_id:
        query_obj = query_obj.filter(board=board)

    per_page = 10
    paginator = Paginator(query_obj, per_page=per_page)
    posts = paginator.page(page)
    pages = paginator.page_range

    for post in posts:
        post.create_time = post.create_time.strftime("%Y-%m-%d %H:%M:%S")

    context = {
        'posts': posts,
        'boards': boards,
        "current_board": int(board_id),
        'page_range': pages,
        'current_page': int(page),
        'total_page': paginator.num_pages
    }
    return render(request, 'front/index.html', context)


@login_required
def post_view(request):
    boards = BoardModel.objects.filter(is_active=True)
    if request.method == 'GET':
        return render(request, 'front/post.html', {'boards': boards})
    elif request.method == 'POST':
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        board_id = request.POST['board_id']
        board = BoardModel.objects.get(id=board_id)
        post = PostModel(title=title, content=content, board=board, author_id=user.id)
        post.save()
        return render(request, 'front/detail.html', {'boards': boards, 'post': post})


@login_required
def post_edit_view(request, post_id):
    boards = BoardModel.objects.filter(is_active=True)
    post = PostModel.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'front/post_edit.html', {'boards': boards, 'post': post})
    elif request.method == 'POST':
        title = request.POST['new_title']
        content = request.POST['new_content']
        board_id = request.POST['board_id']
        board = BoardModel.objects.get(id=board_id)
        post.title = title
        post.content = content
        post.board = board
        post.save()
        return render(request, 'front/detail.html', {'boards': boards, 'post': post})


def detail_view(request, post_id):
    user = request.user
    boards = BoardModel.objects.filter(is_active=True)
    post = PostModel.objects.get(id=post_id)
    if post.author != user:
        post.read_count += 1
        post.save()
    return render(request, 'front/detail.html', {'boards': boards, 'post': post})


@login_required
def post_delete_view(request, post_id):
    post = PostModel.objects.get(id=post_id)
    post.is_active = False
    post.save()
    return HttpResponseRedirect('/')


def friend_view(request):
    return render(request, 'front/friends.html')


def resource_view(request):
    return render(request, 'front/resource.html')


def create_post(request):
    for e in range(100):
        post = PostModel()
        post.title = f'啊{e}'
        post.content = f"哦{e}"
        post.board = BoardModel.objects.get(id=1)
        post.author = User.objects.get(id=1)
        post.save()
    return HttpResponse("添加成功")
