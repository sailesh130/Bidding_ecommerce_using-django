from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("entry/<int:pk>", views.entry, name="entry"),
    path("details/<int:pk>",views.details,name="details"),
    path("watchlist",views.watchlistf,name="watchlist"),
    path("delete/<int:pk>",views.deleteI,name="delete"),
    path("add/<int:pk>",views.addI,name="add"),
    path("close/<int:pk>",views.close_bid,name="close"),
    path("closebidding/<int:pk>",views.bidding_list,name="Closed_details"),
    path("closed_list/<int:pk>",views.announce_winner,name="winner"),
    path("comment/<int:pk>",views.get_comment,name="comment"),
    path("category",views.category,name="category"),
    path("catdetails/<str:cat>",views.cat_details,name="catdetails"),

]
