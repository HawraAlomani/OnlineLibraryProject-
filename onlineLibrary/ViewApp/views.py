
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


# delete the review
def delete(request, book_id):
    item = Review.objects.get(pk=book_id)
    item.delete()
    return redirect(resolve_url("view:show_review"))


'''
# to edit the review
def edit(request, book_id):
    if request.method == "POST":
        item = Review.objects.get(pk=book_id)
        form = ReviewForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = Review.objects.get(pk=book_id)
    return render(request, 'edit-review.html', {'item': item})
'''


def edit(request, book_id):
    item = Review.objects.get(id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view:edit', item.id)
    else:
        form = ReviewForm(instance=item)
    return render(request,
                  'edit-review.html',
                  {'form': form})
