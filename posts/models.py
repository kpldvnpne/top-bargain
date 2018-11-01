from django.db import models

from accounts.models import UserAccount

class PostModel(models.Model):
	username = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	productName = models.TextField(max_length=80)
	price = models.IntegerField()
	postDate = models.DateTimeField(auto_now_add=True)
	location = models.CharField(max_length=100)
	image = models.ImageField(upload_to='TopBargain/static/products/images/', max_length=200,
								default='TopBargain/static/default/no_product_image.png')

	def __str__(self):
		return self.productName
