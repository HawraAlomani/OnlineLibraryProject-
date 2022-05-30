from django.shortcuts import render, redirect, resolve_url
from .models import Review
from .forms import ReviewForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# show the reviews
def show_review(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, "show-reviews.html", context)


# add form works correctly, it adds the review to the database :)
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
    else:
        form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(resolve_url("view:show_review"))
    form = ReviewForm()
    context = {"form": form}
    return render(request, "add-review.html", context)
