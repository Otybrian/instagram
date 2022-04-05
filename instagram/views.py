from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Image,Profile,Likes,Comment, Follow
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, CommentForm, UserProfileForm
from django.http  import Http404




# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    photo = Image.objects.all().order_by('-id')
    return render(request, 'home.html',{'photo':photo})


def save_profile(request, sender, instance, created, **kwargs):
    user = instance
    profile = Profile.objects.create(user=request.user)
    if created:
        profile = Profile(user=user)
        profile.save()


@login_required(login_url='/accounts/login/')
def userProfile(request):
    current_user = request.user
    image = Image.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path_info)

    else:
        form = UserProfileForm()

    return render(request, 'profile.html', {"image": image, "profile": profile,"form":form})

@login_required(login_url='/accounts/login/')
def addProfile(request):
    categories= Profile.objects.all()

    if request.method == 'POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category']!='none':
            category=Profile.objects.get(id=data['category'])

        elif data['category_new']!='':
            category, created=Profile.objects.get_or_create(name=data['category_new'])
        else:
            category=None

        profile_pic = Profile.objects.create(
            category=category,
            description=data['description'],
            image=image
        )
        return redirect('profile')

    context= {'categories':categories}
    return render(request,'profile.html',context)

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
def newImage(request):
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('homePage')

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
def postComment(request):
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

@login_required(login_url='/accounts/login/')
def likeImage(request):
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
    return redirect('homePage')

def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('profile', user_profile2.user.username)


def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('profile', user_profile3.user.username)