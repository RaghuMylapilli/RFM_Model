from django.db import models

# Create your models here.
class customerData(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=120,null=True)
    recency = models.IntegerField(null=True)
    frequency = models.IntegerField(null=True)
    monetary = models.IntegerField(null=True)

class champions(models.Model):
    Champions = models.IntegerField(null=True)

class loyalCustomers(models.Model):
    Loyal_Customers = models.IntegerField(null=True)

class potentialLoyalist(models.Model):
    Potential_Loyalist = models.IntegerField(null=True)

class recentCustomers(models.Model):
    Recent_Customers = models.IntegerField(null=True)

class promising(models.Model):
    Promising = models.IntegerField(null=True)

class customersNeedAttention(models.Model):
    Customers_Needing_Attention = models.IntegerField(null=True)

class aboutToSleep(models.Model):
    About_to_Sleep = models.IntegerField(null=True)

class atRisk(models.Model):
    At_Risk = models.IntegerField(null=True)

class cantLoseThem(models.Model):
    Cant_Lose_Them = models.IntegerField(null=True)

class hibernating(models.Model):
    Hibernating = models.IntegerField(null=True)

class lost(models.Model):
    Lost = models.IntegerField(null=True)

