from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import User,Auction_listing,watchlist,Bid,closedlist,Comment
from django import forms

def index(request):
    closed_item = [x.product for x in closedlist.objects.all()]
    product = list(Auction_listing.objects.all())
    items = [x for x in product if x not in closed_item]
    return render(request, "auctions/index.html",{"items":items})


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
@login_required
def entry(request,pk):
    if request.method=="POST":

            name = request.POST["product_name"]
            price = request.POST["price"]
            des = request.POST["des"]
            photo = request.POST["photo"]
            categorys = request.POST["categorys"]
    else:
        return render(request,"auctions/create_listing.html",{"message":"Enter product details."})


    try:
        user = User.objects.get(pk=pk)
        item = Auction_listing.objects.create(product_name=name,price=price,des=des,photo=photo,categorys=categorys,user=user)
        item.save()
    except:
        
        return render(request,"auctions/create_listing.html",{"message":"data cannot be stored."})

    return HttpResponseRedirect(reverse("index"))
@login_required
def details(request,pk):
    item = Auction_listing.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)
    comments = Comment.objects.filter(product=item)

    if watchlist.objects.filter(user=request.user)== None:
        return render(request,"auctions/details.html",{"item":item})
    else:
        if request.user == Auction_listing.objects.get(pk=pk).user:
            
            return render(request,"auctions/details.html",{"item":item,"comments":comments})

        else:
            try:
                b= [x.amount for x in Bid.objects.filter(BOP=item)]
                bid = max(b)
                count = len(b)

                message = str(count)+"(s) bid so far."+"Required bid above "+str(bid)+"$ price"
            except:
                bid = item.price
                message = "please bid above "+str(bid)+"$ price" 
            
            if request.method == "POST":
                amount = request.POST['bid']
            
                if int(amount) >= bid:
                    
                    try:
                        b = Bid.objects.get(user=user,BOP=item)
                        b.amount = amount
                        b.save()
                    except:
                        b = Bid.objects.create(user=user,BOP=item,amount=amount)
                        b.save()
                    item.price = amount
                    item.save()

                    b= [x.amount for x in Bid.objects.filter(BOP=item)]
                    bid = max(b)
                    count = len(b)
                    message = str(count)+"(s) bid so far."+"Required bid above "+str(bid)+"$ price"
                    

                else:
                    message = "Your value is lower than "+str(bid)+"$ price" 
            try:
                current = Bid.objects.get(user=user,BOP=item).amount
            except:
                current = None  
            try:   
                watchlists = list(watchlist.objects.get(user=request.user.id).product.all())
                product =item in watchlists
            except:
                product = None
            return render(request,"auctions/details.html",{"item":item,"products":product,"message":message,"current":current,"comments":comments})
            
@login_required
def watchlistf(request):
    message = "No item in watchlist"
    try:
        watchlists = watchlist.objects.get(user=request.user.id).product.all()
        close = [x.product for x in closedlist.objects.all()]
        items = [x for x in watchlists if x not in close]

    except:
        items = None
      
    return render(request,"auctions/watchlist.html",{"watchlists":items,"message":message})

def deleteI(request,pk):
    if len(list(watchlist.objects.get(user=request.user.id).product.all()))>1:
        watchlists = watchlist.objects.get(user=request.user.id)
        item = Auction_listing.objects.get(pk=pk)
        watchlists.product.remove(item)
    else:
        watchlist.objects.get(user=request.user.id).delete()

    return HttpResponseRedirect(reverse("watchlist"))
@login_required
def addI(request,pk):
    item = Auction_listing.objects.get(pk=pk)
    try:
        watchlists = watchlist.objects.get(user=request.user.id)
        
    except:
        user = User.objects.get(pk=request.user.id)
        watchlists = watchlist.objects.create(user=user)
        
    watchlists.product.add(item)
    return HttpResponseRedirect(reverse("watchlist"))
@login_required
def close_bid(request,pk):
    try:
        product = Auction_listing.objects.get(pk=pk)
        bids = Bid.objects.filter(BOP=product)
        if bids:
            amount = max(bids.values_list('amount',flat=True))
            winner = bids.get(amount=amount).user
            if winner in [x.user for x in closedlist.objects.filter(product=product).all()]:
                announce = closedlist.objects.get(winner=winner,product=product)
                announce.amount=amount
            else:

                announce = closedlist(winner=winner,product=product,amount=amount)
        else:
            amount = product.price
            if None in [x.user for x in closedlist.objects.filter(product=product).all()]:
                announce = closedlist.objects.get(winner=None,product=product)
                announce.amount=amount
            else:
            
                announce = closedlist(product=product,amount=amount)
        announce.save()
        
        
    except:
        message = "no product in this list"




    message = "no product in this list"
    closed_bid = list(closedlist.objects.all())
    return render(request,"auctions/closed_listing.html",{"items":closed_bid,"message":message})
@login_required
def bidding_list(request,pk):
    product = Auction_listing.objects.get(pk=pk)
    product = closedlist.objects.get(product=product)
    return render(request,"auctions/closed_listing.html",{"product":product})
@login_required
def announce_winner(request,pk):

    look = request.user in [x.winner for x in closedlist.objects.all()]
    products = [x for x in closedlist.objects.filter(winner =request.user)]
    items = [x for x in closedlist.objects.all()]

    return render(request,"auctions/announce_winner.html",{"look":look,"products":products,"items":items})
@login_required
def get_comment(request,pk):
    if request.method =='POST':
        item = Auction_listing.objects.get(pk=pk)
        c_message = request.POST['comment']
        c = Comment.objects.create(user=request.user,product=item,com=c_message)
        c.save()
    return redirect("details",pk=pk)
@login_required
def category(request):

    return render(request,"auctions/category.html")
@login_required
def cat_details(request,cat):
    product = Auction_listing.objects.filter(categorys=cat)
    closed_item = [x.product for x in closedlist.objects.all()]
    products = [x for x in product if x not in closed_item]
    return render(request,"auctions/index.html",{"items":products})

    

        
        
        



