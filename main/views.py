from types import NoneType
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from .forms import MainForm
from .models import Person
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.template.loader import render_to_string

def index(reguest):
    form = MainForm()
    return render(reguest, 'main/page.html', {'title': 'Tesla X', 'form': form})


def send(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            from_email = 'catcat1221@rambler.ru'
            to_email = form.cleaned_data.get('email')
            person = Person.objects.get(email=to_email)
            current_site = get_current_site(request)
            mail_subject = _('Tesla X Активация')
            uid = person.id
            message = render_to_string('main/mail.html', {
                'domain': current_site.domain,
                'uid': uid,
                'token': 'fdv353xQERV4542tfdgdfhDFadgfdH5436fgfm'
            })
            try:
                send_mail(mail_subject, message, from_email, [to_email])
            except:
                return redirect('main:confirm', uid, 'somehash')
            return redirect('main:confirm', uid)
    else:
        form = MainForm()

    return render(request, 'main/send.html', {'title': 'Tesla X', 'form': form})


def confirm(request, personID, hash=False):
    if hash:
        return redirect('main:success')

    try:
        person = Person.objects.get(id=personID)
    except:
        return redirect('main:index')

    email = person.email

    return render(request, 'main/confirm.html', {'email': email})


def success(request):
    return render(request, 'main/success.html',  {'title': 'Tesla X'})