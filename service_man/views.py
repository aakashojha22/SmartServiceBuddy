from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,UpdateView,DeleteView )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from service_man.models import ServiceManInfo
from client_request.models import ClientRequest



# Create your views here.

class IndexView(TemplateView):
    template_name = 'service_man/index.html'


class PendingRequestView(ListView,LoginRequiredMixin):
    model = ClientRequest
    template_name = 'service_man/pending_request.html'
    def get_queryset(self):
       return ClientRequest.objects.filter(appointment_date__gte=timezone.now()).order_by('-appointment_date')

class PastRequestView(ListView,LoginRequiredMixin):
    model = ClientRequest
    template_name = 'service_man/past_request.html'
    def get_queryset(self):
       return ClientRequest.objects.filter(appointment_date__lt=timezone.now()).order_by('-appointment_date')




class RequestDetailView(DetailView,LoginRequiredMixin):
    model = ClientRequest
    template_name = 'service_man/request_detail.html'





            ###################################
            ##Function that required pk match##
            ###################################

"""
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=CommentForm
    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
"""