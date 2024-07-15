from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient, Rdv, ordonnance

# Create your views here.

def home(request):
    if request.method == 'POST':
        uesrname = request.POST['uesrname']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=uesrname, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Loggin In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'index.html', {})

def login_user(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')

def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient.html',{'patients':patients})

def view_patients(request, pk):
    if request.user.is_authenticated:
        veiw_patients = Patient.objects.get(id=pk)
        return render(request, 'patients/view_patient.html', {'patient':veiw_patients})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def add_patients(request):
    return render(request, 'patients/add_patient.html', {})

def add_pat(request):
    fn = request.POST['first_name']
    ln = request.POST['last_name']
    ad = request.POST['address']
    ph = request.POST['phone']
    cin = request.POST['cin']
    pat=Patient(first_name=fn, last_name=ln, address=ad, phone=ph, num_cin=cin)
    pat.save()
    return redirect('patients')

def patient_drop(request, id):
    pat=Patient.objects.get(id=id)
    pat.delete()
    return redirect('patients')

def update_pat(request, id):
    pat = Patient.objects.get(id=id)
    return render(request, 'patients/update_pat.html', {'patient':pat})

def update_p(request, id):
    fn = request.POST['first_name']
    ln = request.POST['last_name']
    ad = request.POST['address']
    ph = request.POST['phone']
    cin = request.POST['cin']
    pat = Patient.objects.get(id=id)
    pat.first_name = fn
    pat.last_name = ln
    pat.address = ad
    pat.phone = ph
    pat.num_cin = cin
    pat.save()
    return redirect('patients')

##Patient Part end

# Rdv
def rdv(request):
    rendez_vous = Rdv.objects.all()
    return render(request, 'rdv/rdv.html', {'rendez_vous':rendez_vous})

def view_rdv(request, pk):
    if request.user.is_authenticated:
        view_rdv = Rdv.objects.get(id=pk)
        return render(request, 'rdv/view_rdv.html', {'rdv':view_rdv})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

def add_rdv(request):
    pat=Patient.objects.all()
    return render(request, 'rdv/add_rdv.html', {'patients':pat})

def add_r(request):
    id_p = request.POST['id_pat']
    da = request.POST['date']
    he = request.POST['heure']
    rdv=Rdv(date_rdv=da, heure_rdv=he, id_pat_id=id_p)
    rdv.save()
    return redirect('rdv')

def rdv_drop(request, id):
    rdv=Rdv.objects.get(id=id)
    rdv.delete()
    return redirect('rdv')

def update_rdv(request, id):
    rdv=Rdv.objects.get(id=id)
    return render(request, 'rdv/update_rdv.html', {'rdv':rdv})

def updat_rdv(request, id):
    id_p = request.POST['id_pat']
    da = request.POST['date']
    he = request.POST['heure']
    rdv = Rdv.objects.get(id=id)
    rdv.date_rdv = da
    rdv.heure_rdv = he
    rdv.id_pat_id = id_p
    rdv.save()
    return redirect('rdv')


def ordonnancee(request):
    ordonnances = ordonnance.objects.all()
    return render(request, 'ordonnance/ordonnance.html', {'ordonnances':ordonnances})

def add_ord(request):
    pat=Patient.objects.all()
    return render(request, 'ordonnance/add_ord.html', {'patients':pat})

def add_o(request):
    m=request.POST['medicament']
    d=request.POST['dose']
    da=request.POST['date']
    pat=request.POST['patient_id']
    ordo=ordonnance(medicament=m, dose=d, id_pat_id=pat)
    ordo.save()
    return redirect('ordonnance')


def view_ord(request, id):
    if request.user.is_authenticated:
        view_ord = ordonnance.objects.get(id=id)
        return render(request, 'ordonnance/view_ord.html', {'ord':view_ord})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

def delete_ord(request, id):
    o=ordonnance.objects.get(id=id)
    o.delete()
    return redirect('ordonnance')