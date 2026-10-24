from django.db import models ,transaction

# Create your models here.

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)
    def __str__(self) :
        return str(self.current_balance)
    class Meta :
        db_table = "currentbalance"

class TrackingHistory(models.Model):
    description = models.TextField(max_length=200)
    amount= models.FloatField()
    current_balance = models.ForeignKey(CurrentBalance , on_delete=models.CASCADE )
    expense_type = models.CharField(choices=(("Debit","Debit"),("Credit","Credit")),max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self , *args , **kwargs):
        with transaction.atomic():
            balance , _ = CurrentBalance.objects.get_or_create(id = 1)

            self.current_balance = balance

            if self.pk is None:
                balance.current_balance += float(self.amount)
                balance.save()

            super().save(*args, **kwargs)

    def __str__(self):
        return f"The amount is {self.amount} for {self.description} expense type is {self.expense_type}"
    class Meta :
        db_table = 'trackinghistory'