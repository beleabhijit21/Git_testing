from django.shortcuts import render
from .forms import OrderForm

# Create your views here.
def addOrder_view(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form.save()
    template_name = 'CRUD_APP/add.html'
    context = {'form':form}
    return render ( request,template_name,context )