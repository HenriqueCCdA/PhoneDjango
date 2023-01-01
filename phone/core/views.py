from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import DestroyAPIView

from phone.core.models import Phone
from phone.core.forms import PhoneForm

from phone.core.serialiazers import PhoneSerializers


class ListPhones(ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class=PhoneSerializers


class DeletePhone(DestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class=PhoneSerializers


def home(request):

    form = PhoneForm()

    phones = Phone.objects.all()

    context = {'form': form, 'phones': phones}

    if request.method == 'POST':

        form = PhoneForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        context['form'] = form

        return render(request, 'show_phone.html', context)

    return render(request, 'show_phone.html', context)


def delete(request, pk):
    phone = Phone.objects.get(pk=pk)
    phone.delete()
    return HttpResponseRedirect('/')