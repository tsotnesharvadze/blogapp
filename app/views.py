from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from .forms import CommentForm

# Create your views here.
def index(request):
	
	def my_sort(a):
		return len(a.comment_set.all())
	postebis_sia=Post.objects.all()
	popularuli_postebi=[i for i in postebis_sia]
	popularuli_postebi.sort(key=my_sort,reverse=True)
	popularuli_postebi=popularuli_postebi[:5]

	return render(request,'app/new.html',{"postebis_sia":postebis_sia,
		"popularuli_postebi":popularuli_postebi})


def srulad(request,posti_id):
	form=CommentForm()
	posti_srulad=Post.objects.get(pk=posti_id)
	if request.method=="POST":
		posti_srulad.comment_set.create(
			komentari=request.POST.get("new_comment"))
	return render(request,'app/srulad.html',{"posti":posti_srulad,"form":form})


