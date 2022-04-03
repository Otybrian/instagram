from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Image,Profile,Likes,Comment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, CommentForm, ProfileForm
from django.http  import Http404




# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    photo = Image.objects.all().order_by('-id')
    return render(request, 'home.html',{'photo':photo})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    image = Image.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path_info)

    else:
        form = ProfileForm()

    return render(request, 'profile.html', {"image": image, "profile": profile,"form":form})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

@login_required(login_url='/accounts/login/')
def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image =Image.objects.get(id=image_id)
        if user in image.like.all():
            image.like.add(user)
        else:
            image.like.add(user)    
            
        liked,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if liked.value =='Like':
               liked.value = 'Unlike'
        else:
               liked.value = 'Like'

        liked.save()       
    return redirect('home')

@login_required(login_url='/accounts/login/')
def comment(request):
    current_user=request.user
    comment=Comment.objects.filter()
    image=Image.objects.filter(image=id).all()
    
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save()
            image.user = current_user
            comment.save_comment()
        return HttpResponseRedirect(request.path_info)
    else:
        form=CommentForm()
    return render(request,'comments.html',{"form":form,"comments":comment,"image":image})