import os
from django.shortcuts import render
from django.http import HttpResponse

def output_setting(value):
    setting = ''
    if isinstance(value, bool):
        return '<select  class= "form-control" ><option>'+str(value)+'</option><option>'+str(not value)+'</option></select>'
    elif isinstance(value, tuple):
        for item in value:
            setting += '<div  class= "checkbox" >'
            setting += '<label>'
            setting += '<input  type= "checkbox"  value= "" checked>'
            setting += item
            setting += '</label>'
            setting += '</div>'
        setting += '<input  type= "text"  class= "form-control"  placeholder= "New Item" >'
        return setting
    else:
        setting += '<input  type= "text"  class= "form-control"  value= "'+str(value)+'" >'
        return setting

def project_settings(request):
    request.session['project'] = 'alcom'
    project = 'alcom'
    exec('import projects.'+project+'.'+project+'.'+'settings'+' as project_settings')
    setting_items = [item for item in dir(project_settings) if item[:2]!='__' and item!='os']
    settings = {}
    for item in setting_items:
        settings[item] = output_setting(eval('project_settings.'+item))
    project_settings_flag = 'class=active'
    return render(request, 'project_settings.html', locals())

def testform(request):
    if 'user_name' in request.GET and request.GET['user_name']!="":
        return HttpResponse("hello, "+request.GET['user_name']) 
    else:
        return render(request, "test.html", locals())




