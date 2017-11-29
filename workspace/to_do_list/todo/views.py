from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Todo

import smtplib
import sys


def index(request):
    todo = Todo.objects.all()[:10]

    context = {
        'todo':todo
    }

    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todo')
    else:
        return render(request, 'add.html')



    mail_username='ephraimavong32@gmail.com'
    mail_password='08133464782'
    from_addr = mail_username
    to_addrs=('ephraimavong32@gmail.com')

    HOST = 'smtp.gmail.com'
    PORT = 25

    # Create SMTP Object
    smtp = smtplib.SMTP()
    print ('connecting ...')

    # show the debug log
    smtp.set_debuglevel(1)

    # connet
    try:
        print (smtp.connect(HOST,PORT))
    except:
        print ('CONNECT ERROR ****')
    # gmail uses ssl
    smtp.starttls()
    # login with username & password
    try:
        print ('loginning ...')
        smtp.login(mail_username,mail_password)
    except:
        print ('LOGIN ERROR ****')
    # fill content with MIMEText's object
    msg =title
    msg['From'] = from_addr
    msg['To'] = ';'.join(to_addrs)
    msg['Subject']='this is test msg'
    print (msg.as_string())
    smtp.sendmail(from_addr,to_addrs,msg.as_string())
    smtp.quit()
