from django.shortcuts import render
from .models import Audit


def team(request):
    if request.method == 'POST':
        official_names = request.POST.get('official-name')
        country = request.POST.get('country')
        assessor_name = request.POST.get('assessor')
        assessor_email = request.POST.get('assessor-email')
        call_phone_number = request.POST.get('call-phone-number')
        agent_listen = request.POST.get('agent-listen')
        parameter = request.POST.get('parameter')
        feedback = request.POST.get('feedback')
        reason = request.POST.get('reason')
        call_link = request.POST.get('call-link')

        form = Audit(
            official_names=official_names,
            country=country,
            assessor_name=assessor_name,
            assessor_email=assessor_email,
            phone_number=call_phone_number,
            agent_listened=agent_listen,
            parameter_not_fairly_scored=parameter,
            feedback_received=feedback,
            reason_for_appeal=reason,
            call_link=call_link
        )

        form.save()

    return render(request, 'Appeal/Appealform.html')

def loginpage(request):
    return render(request, 'loginpage/loginpage.html')

def Signuppage(request):
    return render(request, 'Signuppage/Signup.html')

def Resetpage(request):
    return render(request, 'Resetpage/Reset.html')


def Appeal_table(request):
    audits = Audit.objects.all()
    context= {'Appeal_data':Appeal_table}

    return render(request, 'Appeal/Appeal_table.html', context)
