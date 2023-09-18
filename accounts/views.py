from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView,DetailView
from .forms import SignUpForm
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('boards')
    return render(request,'signup.html',{'form':form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name','last_name','email',)
    template_name = 'edit_my_account.html'
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})


    def get_object(self):
        return self.request.user

class UserProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile_user'
