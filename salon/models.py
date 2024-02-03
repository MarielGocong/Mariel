from django.db import models


class HairServices(models.Model):
    hairservice_name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.hairservice_name

class NailServices(models.Model):
    nailservice_name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.nailservice_name

class CustomerBook(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(blank=True)
    customer_picture = models.ImageField(upload_to='customer_picture/', blank=True)
    hair_service = models.ForeignKey(HairServices, on_delete=models.SET_NULL, null=True)
    nails_service = models.ForeignKey(NailServices, on_delete=models.SET_NULL, null=True)
    time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    package_name = models.CharField(max_length=50, null=True)
    hairservice = models.ForeignKey(HairServices, on_delete=models.SET_NULL, null=True)
    nailservice = models.ForeignKey(NailServices, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.package_name


