from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Supplier, ContactPerson
from .forms import SupplierForm, ContactForm
from users.models import Profile


##############################################
@login_required
def supplierslist(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render (request, 'suppliers/supplierslist.html', context)


@login_required
def addSupplier(request):
    form = SupplierForm()
    form1 = ContactForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
        return HttpResponseRedirect(request.path_info)
    else:                   
        context = {'form': form}
        return render(request, 'suppliers/add_supplier.html', context)

@login_required
def supplierdetail(request, pk):
    profile = Profile.objects.all()
    context = {'profile':profile}
    form1 = ContactForm()
    supplier = Supplier.objects.filter(id=pk)
    supplier_name = Supplier.objects.get(id=pk)
    contact_person = ContactPerson.objects.filter(company__supplier_name=supplier_name)
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            newform = form1.save(commit=False)
            newform.user = request.user
            newform.company = supplier_name
            newform.save()
        return HttpResponseRedirect(request.path_info)
    context={
        'supplier': supplier, 
        'form1':form1,
        'contact_person': contact_person
    }
    return render(request, 'suppliers/supplier.html', context)

@login_required
def deleteContact(request, pk):
    contact = contactperson.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('supplierdetail')
    context = {'contact':contact, 'month':month}
    return render(request, 'incomes/deleteincome.html', context)

@login_required
def updatesupplier(request, pk):
    supplier = Supplier.objects.filter(id=pk)
    supplier_name = Supplier.objects.get(id=pk)
    contact = ContactPerson.objects.filter(company__supplier_name=supplier_name)
    supplier_form = SupplierForm(instance=supplier_name)
    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST, instance=supplier_name)
        if supplier_form.is_valid():
            supplier_form.save()
            messages.success(request, f'{supplier_name} was updated successfully')
            return HttpResponseRedirect(request.path_info)
    context = {
                'supplier_name':supplier_name, 
                'supplier':supplier,
                'supplier_form':supplier_form,
                }
    return render(request, 'suppliers/update_supplier.html', context)


#############################################################################


