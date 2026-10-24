from django.contrib import admin
from .models import *
# Register your models here.

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display =["description" , "amount" , "current_balance" , "expense_type"]

    search_fields = ["amount" , "description"]

    ordering = ["amount"]

    list_filter = ["expense_type" , "amount"]

    ## Adding new Field
    list_display.append("Object_Value")
    def Object_Value(self ,obj):
        if abs(float(obj.amount)) > 50000.0 :
            return "Expensive"
        else :
            return "Cheap"

    ## Adding custom Action 
    """
     @admin.action(description = "Set the Expense_type to Credit")
        def Set_Credit(self , request , queryset):
            queryset.update(expense_type = "Credit")
        actions = ["Set_Credit"]
    """
   
admin.site.register(TrackingHistory , TrackingHistoryAdmin)
