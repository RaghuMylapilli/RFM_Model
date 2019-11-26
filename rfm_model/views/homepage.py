from django.views import View
from rfm_model.models import customerData
from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render,redirect
from datafile.analysis import *
from datafile.dataSet import *


class homePageViews(View):
    def get(self, request):
        return render(
            request,
            template_name='rfm_model/homePage.html', )

def customersupportViews(request):
    return render(request,
                  template_name='rfm_model/customersupport.html')


def analysis(request):
    champ = champions.objects.all()
    loyal = loyalCustomers.objects.all()
    potential = potentialLoyalist.objects.all()
    recent = recentCustomers.objects.all()
    promise = promising.objects.all()
    attention = customersNeedAttention.objects.all()
    sleep = aboutToSleep.objects.all()
    risk = atRisk.objects.all()
    cantlose = cantLoseThem.objects.all()
    hibernate = hibernating.objects.all()
    loss = lost.objects.all()
    return render(request,template_name='rfm_model/analysis.html',
                  context={'champ':champ,'loyal':loyal,'potential':potential,
                          'recent':recent,'promise':promise,'attention':attention,
                           'sleep':sleep,'risk':risk,'cantlose':cantlose,'hibernate':hibernate,'loss':loss})


def logoutPageViews(request):
    auth.logout(request)
    return redirect('/')

class viewPage(View):
    def get(self,request):
        champions.objects.all().delete()
        loyalCustomers.objects.all().delete()
        potentialLoyalist.objects.all().delete()
        recentCustomers.objects.all().delete()
        promising.objects.all().delete()
        customersNeedAttention.objects.all().delete()
        aboutToSleep.objects.all().delete()
        atRisk.objects.all().delete()
        cantLoseThem.objects.all().delete()
        hibernating.objects.all().delete()
        lost.objects.all().delete()
        populate_customer_data()
        return render(
            request,
            template_name='rfm_model/uploadpage.html'  )

    def post(self,request):
        file_name = request.POST['datafile']
        print(file_name)
        dataDetails = customerData.objects.all()
        customer_data = customerData.objects.all()
        generateReport(customer_data)
        return render(
            request,
            template_name='rfm_model/viewpage.html',
            context={'dataDetails':dataDetails})





