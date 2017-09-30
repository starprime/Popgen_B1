from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .models import User

#for update
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

##for user
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


class IndexView(generic.ListView):
    template_name = 'EnterPage/index.html'

    def get_queryset(self):
        return User.objects.all()

class DetailsView(generic.DetailView):
    model = User
    template_name = 'EnterPage/Detail.html'

class UserCreate(CreateView):
    model = User
    fields = ['username','email','password']

class UserUpdate(UpdateView):
    model = User
    fields = ['username','email','password']

class UserDelete(UpdateView):
    model = User
    success_url = reverse_lazy('EnterPage:index')

## get request for the first time
## post request to submit the form
class UserFormView(View):
    form_class=UserForm
    template_name='EnterPage/registration_form.html'

    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            # clean ,normalize the data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User Objects if cred are correct

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('EnterPage:index')

        return render(request,self.template_name,{'form':form})





