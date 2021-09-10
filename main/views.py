from django.contrib import messages
from django.shortcuts import redirect, render
from .decorators import login_required
from .models import User,Appointment


@login_required
def index(request):
    all_appointments = Appointment.objects.all().order_by('-time')
    context = {
        'all_appointments' : all_appointments
    }
    return render(request, 'index.html', context)

@login_required
def new_appointment(request):
    if request.method == 'GET':
        return render(request,'form.html')
    
    date = request.POST['date']
    time = request.POST['time']
    complain = request.POST['complain']
    bring_user = request.session['user']['id']
    bring_user = User.objects.get(id = bring_user)
    #print(date)
    count_appointment = Appointment.objects.filter(date = date).count()
    print(count_appointment)
    if len(complain)<10:
        messages.error(request,'insufficient character to describe your sick/ill/complain')
        return redirect('/new_appointment')
    if  count_appointment+1 > 3:
        messages.warning(request,'Please select another date')
        return redirect('/new_appointment')

    else:
        appointment = Appointment.objects.create(date = date, time = time, patient_name = bring_user, complain= complain)
        messages.success(request,'appointment created succesfully!')
        return redirect('/')

def delete_appointment(request,id_r):
    id_user = request.session['user']['id']
    appointment = Appointment.objects.get(id = id_r)
    if appointment.patient_name.id == id_user:
        appointment.delete()
        messages.success(request,'Appointment deleted')
        return redirect('/')
    else:
        messages.error(request,"Appointment can't be eliminated")
        return redirect('/')

