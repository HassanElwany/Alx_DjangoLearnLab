from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Profile, Post, Comment
from .forms import ProfileUpdateForm, CustomUserCreationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()  # Fetch related comments
        context['comment_form'] = CommentForm()  # Provide a form for adding comments
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        """Ensure only the author can update the post."""
        post = self.get_object()
        return post.author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to edit this post.")
        return super().handle_no_permission()


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        """Ensure only the author can delete the post."""
        post = self.get_object()
        return post.author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to delete this post.")
        return super().handle_no_permission()


# New views for comment management

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added!")
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        post = self.object.post  # Get the related post
        messages.success(self.request, "Your comment has been deleted.")
        return redirect('post_detail', pk=post.pk)

    def test_func(self):
        """Ensure only the comment author can delete the comment."""
        comment = self.get_object()
        return comment.author == self.request.user