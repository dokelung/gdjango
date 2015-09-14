from django.shortcuts import render
from django.contrib.auth.models import User
from lab.models import Collaborator

def get_user_rows(users, col_num=3):
	"""
	example:
		users = [a, b, c, d, e]
		col_num = 3
		return [ [a, b, c], [d, e] ]
	"""
	user_rows = []
	user_row = []

	for user in users:
		user_row.append(user)
		if len(user_row)==col_num:
			user_rows.append(user_row)
			user_row = []
	else:
		if user_row:
			user_rows.append(user_row)

	return user_rows

def show_advisor(request):
	user = User.objects.get(people__status='Professor')
	return render(request, 'advisor.html', locals())

def list_graduate(request, status):
	"""
	list (degree) students
	"""
	users = User.objects.filter(people__status=status)
	user_rows = get_user_rows(users, col_num=3)

	degrees = ['PHD', 'Master']

	return render(request, 'graduate_students.html', locals())

def list_former(request, gyear):
	"""
	list students graduated in gyear
	"""
	users = User.objects.filter(people__gyear=gyear)

	years= []
	for user in User.objects.all():
		try:
			years.append(int(user.people.gyear))
		except:
			pass
	years = list(set(years))
	years.sort()
	years.reverse()

	next_year = int(gyear)+1
	if next_year not in years:
		next_year = gyear+'#'
	pre_year = int(gyear)-1
	if pre_year not in years:
		pre_year= gyear+'#'

	gyear = int(gyear)

	user_rows = get_user_rows(users, col_num=3)		

	return render(request, 'former_students.html', locals())

def list_collaborators(request):
	collaborators = Collaborator.objects.all()
	return render(request, 'collaborators.html', locals())

def list_research_fields(request):
	return render(request, 'research_fields.html', locals())