from django.contrib import admin
from .models import Myfood,BookTable,contact,Order,Profile

# Register your models here.


admin.site.register(Myfood)
admin.site.register(BookTable)
admin.site.register(contact)
admin.site.register(Order)
admin.site.register(Profile)