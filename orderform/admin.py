from django.contrib import admin
from orderform.models import order
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path
# Register your models here.

class orderAdmin(admin.ModelAdmin):
    list_display = ('id','cName','cSpot','cPhone','cDate',
             'c1T100', 'c1T100_slice', 'c1T100_thickless', 'c1T120', 'c1T120_slice', 'c1T120_thickless',
             'c1T130', 'c1T130_slice', 'c1T130_thickless', 'c1T140', 'c1T140_slice', 'c1T140_thickless',
             'c2M50', 'c2M50_slice')
    list_filter = ('cDate', 'cSpot')
    search_fields = ('cDate', 'cSpot')
    change_list_template = "add_button.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('export/', self.set_export),
        ]
        return my_urls + urls

    def set_export(self, request):
        if request.method == "POST":
            date = request.POST['date']
            dateList = date.split('/')
            red = '/export/' + dateList[0] + dateList[1] + dateList[2]
            return redirect(red)
        return redirect("../")

admin.site.register(order, orderAdmin)
