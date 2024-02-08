from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.template import loader

from Calculator.models import Commodity


def index(request):
    commodity_list = Commodity.objects.order_by("name")
    context = {
        "commodity_list": commodity_list,
    }

    return render(request, "Calculator/index.html", context)


def save_commodities(request):
    if request.method == 'POST':
        commodity_data = request.POST.getlist('commodity_list[]')
        commodity_list = []
        for item in commodity_data:
            name = item['name']
            price = item['price']
            quantity = item['quantity']
            commodity = Commodity(name=name, price=price, quantity=quantity)
            commodity_list.append(commodity)

        Commodity.objects.bulk_update(commodity_list)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
