from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task
import socket

hostname = socket.gethostname()
client_ip = socket.gethostbyname(hostname)

def delete_todo(request, todo_id):
  print(todo_id)
  Task.objects.get(id=todo_id).delete()
  return HttpResponseRedirect('/')

def delete_task(title):
  for obj in Task.objects.all():
    if obj.title == title:
      obj.delete()

def clean_list(): # rewrite it
  obj_string = []
  for obj in Task.objects.all():
    if obj.title == "":
      obj.delete()
  for obj in Task.objects.all():
    if str(obj) == '':
      obj.delete()

    if not str(obj) in obj_string:
      obj_string.append(str(obj))
  Task.objects.all().delete()

  for task_str in obj_string:
    Task(title=task_str).save()

def return_task_objects(cip):
  client_tasks = []
  for task in Task.objects.all():
    if task.ip == str(cip):
      client_tasks.append(task)
  return client_tasks

def delete_all_tasks(cip):
  for task in Task.objects.all():
    if task.ip == cip:
      task.delete()

# Create your views here.
def index(request):
  global client_ip

  if request.method == 'POST':
    if request.POST.get('task_title').lower().strip() == "--delete all--":
      delete_all_tasks(client_ip)
    elif request.POST.get('task_title').lower().strip() == '':
      pass
    else:
      task_title = request.POST.get('task_title')
      Task(ip=client_ip, title=task_title).save()

  client_tasks = return_task_objects(client_ip) # client specific tasks

  return render(request, 'index.html', context = {'tasks': client_tasks})
