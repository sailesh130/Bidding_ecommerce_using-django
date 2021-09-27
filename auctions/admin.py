from django.contrib import admin

# Register your models here.
from .models import Auction_listing,Bid,Comment,User,watchlist,closedlist

admin.site.register(Auction_listing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(watchlist)
admin.site.register(closedlist)