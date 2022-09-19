from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import json
from .models import AuctionList, User


def index(request):
    user = request.user
    if user is not None:
        # list = json.loads(user.watchlist)
        # contador = len(list) 
        list = [2,3]
        contador = 2
        return render(request, "auctions/index.html", {
           "auctions": AuctionList.objects.filter(active=True),
           "contador": contador,
           "logueado": False
        })
    else:
        return render(request, "auctions/index.html", {
           "auctions": AuctionList.objects.filter(active=True),
           "contador": contador,
           "logueado": True
        })
        


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new_auction(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        url_image = request.POST["image"]
        auction = AuctionList()
        auction.active = True
        auction.title = title
        auction.description = description
        auction.price = starting_bid
        auction.url_image = url_image
        userid = request.POST["userid"]
        user_object = User.objects.get(id=userid)
        auction.user = user_object
        auction.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "auctions/new_auction.html")


def listing(request, id):
    user = request.user
    list = json.loads(user.watchlist)
    contador = len(list)
    listing = AuctionList.objects.get(id=id)
    if len(listing.url_image) == 0:
        withimg = False
    else:
        withimg = True
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "listedby": listing.user.username,
        "withimg": withimg,
        "contador": contador,

    })


def add_to_watchlist(request, id):
    user = request.user
    list = json.loads(user.watchlist)
    list.append(id)
    user.watchlist = json.dumps(list)
    user.save()
    return HttpResponseRedirect(reverse("listing", args=[id]))


def watchlist(request):
    return HttpResponseRedirect(reverse("index"))
