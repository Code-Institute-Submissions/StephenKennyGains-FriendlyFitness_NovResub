""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to see all reviews
made by users and admin along with CRUD functions"""

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


# Create your views here.


class UserReview(generic.ListView):

    """ Sets the view for reviews to display to the review page.
    No Pagination needed"""

    model = Review
    queryset = Review.objects.order_by("-created_on")
    template_name = "review.html"


class CreateReview(View):

    """ Sets the view for review creation"""

    def get(self, request):

        """ Gets the page, review form and user status for posting"""

        form = ReviewForm(request.GET or None)
        if request.user.is_authenticated:
            return render(
                request,
                "create_review.html",
                {
                    "form": form,
                    "review_form": ReviewForm()
                },
            )

        return render(request, "review.html")

    def post(self, request):

        """ Uses the review form and required fields to post
        new reviews to the database."""

        form = ReviewForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.user = request.user
                post.save()
                messages.success(request,
                                 "You successfully posted a review")
            return HttpResponseRedirect(reverse("review"))
