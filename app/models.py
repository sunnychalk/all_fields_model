from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class BaseClass(models.Model):
	some_big_number = models.BigIntegerField()
	bytes_number = models.BinaryField()
	is_true = models.BooleanField()
	name = models.CharField(max_length=256)
	date = models.DateField(auto_now_add=True)
	date_time = models.DateTimeField(auto_now=True)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	duration = models.DurationField()
	email = models.EmailField(max_length=254)
	file = models.FileField(upload_to=None, max_length=100)
	file_path = models.FilePathField(path=None, match=None, recursive=False, max_length=100)
	float_number = models.FloatField()
	photo = models.ImageField(upload_to=None, height_field=100, width_field=100, max_length=100)
	number = models.IntegerField()
	ip_adress = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	is_good = models.NullBooleanField()
	positive_number = models.PositiveIntegerField()
	small_positive_number = models.PositiveSmallIntegerField()
	slug = models.SlugField(max_length=50)
	small_integer = models.SmallIntegerField()
	text = models.TextField()
	time = models.TimeField(auto_now_add=True)
	url = models.URLField(max_length=200)
	uuid = models.UUIDField()



