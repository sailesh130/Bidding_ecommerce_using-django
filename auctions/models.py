from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class User(AbstractUser):
    pass

class Auction_listing(models.Model):
	product_name = models.CharField(max_length=64)
	price = models.IntegerField()
	des = models.CharField(max_length=256)
	photo =models.URLField(max_length=520)
	categorys=models.CharField(max_length=128,blank=True,null=True)
	date = models.DateField(auto_now=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='lister')


	def __str__(self):
		return f"{self.user} register {self.product_name}"

class Bid(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bidder')
	BOP  = models.ForeignKey(Auction_listing,on_delete=models.CASCADE,related_name='bid_product')
	amount = models.IntegerField()

	def __str__(self):
		return f"{self.user} bid {self.BOP} with {self.amount}"

class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commenter')
	product = models.ForeignKey(Auction_listing,on_delete=models.CASCADE,related_name='CommentOnProduct')
	com = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user} comment on {self.product}"

class watchlist(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='watchlister')
	product= models.ManyToManyField(Auction_listing,blank=True,related_name='watchproduct')

	def __str__(self):
		return f"{self.user} watchlist {self.product}"

class closedlist(models.Model):
	winner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='winner',blank=True,null=True)
	product = models.ForeignKey(Auction_listing,on_delete=models.CASCADE,related_name='closed_product')
	amount = models.IntegerField()

	def __str__(self):
		return f"{self.winner} wins {self.product}"

            
        
