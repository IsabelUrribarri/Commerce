Crear un modelo

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()


Naming Your Models

E.g. User , Permission , ContentType , etc. For the model's attributes use snake_case. E.g. first_name , last_name , etc. Always name your models using singular.



class auctionList(models.Model):

    active = models.BooleanField()
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url_image = models.URLField()
    description = models.TextField()