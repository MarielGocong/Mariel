from django.shortcuts import render, redirect
from .models import CustomerBook, NailServices, HairServices,Package
from .forms import CustomerForm, NailUpdateForm, HairUpdateForm, PackageForm

def homePage(request):
    customer = CustomerBook.objects.all()
    package = Package.objects.all()
    hair = HairServices.objects.all()
    nail = NailServices.objects.all()

    total_customer = customer.count()
    total_package = package.count()
    total_hair = hair.count()
    total_nail = nail.count()

    context = {
        'customer':customer,
        'package':package,
        'hair':hair,
        'nail':nail,
        'total_customer':total_customer,
        'total_package':total_package,
        'total_hair':total_hair,
        'total_nail':total_nail,
    }
    return render(request, 'pages/homepage.html', context)



def viewPackageInfo(request, pk):
    package = Package.objects.get(id=pk)

    context = {
        'package': package,
    }
    return render(request, 'pages/view_package.html', context)


def viewHairInfo(request, pk):
    hair = HairServices.objects.get(id=pk)
    hairservice = HairServices.objects.all()

    context = {
        'hair': hair,
        'hairservice': hairservice
    }
    return render(request, 'pages/view_hairservice.html', context)


def viewNailInfo(request, pk):
    nail = NailServices.objects.get(id=pk)
    nailservice = NailServices.objects.all()

    context = {
        'nail': nail,
        'nailservice': nailservice
    }
    return render(request, 'pages/view_nailservice.html', context)

def addHairService(request):
    form = HairUpdateForm()
    if request.method == 'POST':
        form = HairUpdateForm(request.POST)
        form.save()
        return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/add_hairservice.html', context)


def addNailService(request):
    form = NailUpdateForm()
    if request.method == 'POST':
        form = NailUpdateForm(request.POST)
        form.save()
        return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/add_nailservice.html', context)


def addPackage(request):
    form = PackageForm()
    if request.method == 'POST':
        form = PackageForm(request.POST)
        form.save()
        return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/add_package.html', context)

def updatePackage(request, package_id):
    package = Package.objects.get(pk=package_id)
    form = PackageForm(request.POST or None, instance=package)
    if form.is_valid():
        form.save()
        return redirect('homePage') 

    return render(request, 'pages/update_package.html',
     {'package': package, 'form':form})

def updateCustomer(request,pk):
    customer = CustomerBook.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/add_customer.html', context)

def updateNailService(request, pk):
    nail = NailServices.objects.get(id=pk)
    form = NailUpdateForm(instance=nail)

    if request.method == 'POST':
        form = NailUpdateForm(request.POST, instance=nail)
        if form.is_valid():
            form.save()
            return redirect('homePage')

    context = {'form':form}
    return render(request, 'pages/update_nailservice.html', context)

def deletePackage(request, pk):
    package = Package.objects.get(id=pk)
    package.delete()
    return redirect('homePage')


def deleteHairService(request, pk):
    hair = HairServices.objects.get(id=pk)
    hair.delete()
    return redirect('homePage')


def deleteNailService(request, pk):
    nail = NailServices.objects.get(id=pk)
    nail.delete()
    return redirect('homePage')


def viewCustomer(request, pk):
    customer = CustomerBook.objects.get(id=pk)

    context = {
        'customer': customer,
    }
    return render(request, 'pages/view_customer.html', context)

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/add_customer.html', context)

def deleteBook(request, customer_id):
    customer = CustomerBook.objects.get(pk=customer_id)
    customer.delete()
    return redirect('homePage')

def updateHairService(request, pk):
    hair = HairServices.objects.get(id=pk)
    form = HairUpdateForm(instance=hair)

    if request.method == 'POST':
        form = HairServices(request.POST, instance=hair)
        if form.is_valid():
            form.save()
            return redirect('homePage')

    context = {'form':form}
    return render(request, 'pages/update_hairservice.html', context)




def aboutPage(request):
    return render(request, 'pages/aboutpage.html')



