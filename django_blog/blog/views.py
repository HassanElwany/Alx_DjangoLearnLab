from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileUpdateForm, CustomUserCreationForm
from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = Profile
    template_name = "blog/profile_list.html"
    context_object_name = "profiles"
    paginate_by = 10  # Optional: Paginate profiles


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = "blog/profile_detail.html"
    context_object_name = "profile"

    def get_object(self):
        return self.request.user.profile  # Ensure the user views only their profile


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "blog/profile_form.html"
    success_url = reverse_lazy("profile_detail")

    def get_object(self):
        return self.request.user.profile  # Restrict updates to the logged-in user's profile

    def form_valid(self, form):
        messages.success(self.request, "Your profile has been updated successfully.")
        return super().form_valid(form)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Create profile for new user
        Profile.objects.create(user=self.object)
        messages.success(self.request, "Registration successful! Please log in.")
        return response


class ProfileDeleteView(DeleteView):
    model = User
    template_name = "blog/profile_confirm_delete.html"
    success_url = reverse_lazy("register")  # Redirect to registration after deletion

    def get_object(self):
        return self.request.user  # Allow users to delete their own account

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Your account has been deleted.")
        return super().delete(request, *args, **kwargs)
