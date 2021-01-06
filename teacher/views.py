from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from department.models import *
from student.models import Student
from users.models import Users
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def teacher_index(request):
	teacher = Teacher.objects.get(teacher_name=request.user.id)
	dept = department.objects.get(teacher=request.user.is_teacher)
	
	# print (dir(teacher.dept.department_students))
	# print(teacher.dept.department_students)


	context= {'teacher':teacher}
	return render(request,'teacher.html', context)

def logOut(request):
	auth_logout(request)
	return redirect('login')


# def login(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	# else if:
# 	# 	return render(request, 'not_student.html')
# 	if request.user.is_authenticated:
# 		return redirect('home')

# 	else:
# 		if request.method == 'POST':
# 			email = request.POST.get('email')
# 			password = request.POST.get('password')
# 			try:
# 				user = authenticate(request, email=email, password=password)
# 				print ('---',dir(user))	

# 				if user.is_teacher == True and user is not None:
# 					auth_login(request, user)
# 					return redirect('home')
# 				elif user.is_superuser and user is not None:
# 					auth_login(request, user)
# 					return HttpResponseRedirect(reverse('admin:index'))

# 				else:
# 					return redirect('home')
# 				# else:
# 				# 	messages.info(request, 'Username OR password is incorrect')
# 			except:
# 				user = "Something Wrong"
# 		context = {}
# 		return render(request, 'register.html', context)

# @login_required(login_url='login')
# def home(request):
# 	if request.user.is_student:
# 		a= Student.add_to_class(str(request.user), value="ADDED")
# 		print(a)
# 	#print (std)
# 	global sem,sub, batches, user_info
# 	try:
# 		user_info = Student.objects.get(students=request.user)
# 	except:
# 		user_info = "Student Not Available"
# #	print(dir(user_info))
# 	try:
# 		batches = batch_no.objects.get(student=Student.objects.get(students=request.user))
# 	except:
# 		batches = "    \tYour not assigned to any batches"
# 	try:
# 		sem = Semester.objects.get(batchess=batches)
# 	except:
# 		sem = "  Your are Not Assigned To any Semester"

# 	try:
# 		attendence = Attendence.objects.get(student=user_info)
# 	except:
# 		attendence = "NOT AVAILABLE AT THE MOMENT"
# #	d = department.objects.get(batches=batch_no.objects.get(student=Student.objects.get(students=request.user))).first()
# 	context = {'u':user_info, 'b':batches,'sem':sem,'a':attendence}
# 	return render(request, 'home.html', context)


# def courses(request):
# 	try:
# 		sub = subjects.objects.get(semester_subjects=sem)
# 	except:
# 		sub ="NO SUBJECTS"
# 	context = {'sub':sub}
# 	return render(request, 'courses.html',context)

# def show_attendence(request):
# 	try:
# 		attendence = Attendence.objects.get(student=user_info)
# 	except:
# 		attendence = "NOT AVAILABLE AT THE MOMENT"
# 	context = {'a': attendence}
# 	return render(request, 'attendence.html', context)

# def result(request):
# 	pass

# def fee(request):
# 	pass



# def logOut(request):
# 	auth_logout(request)
# 	return redirect('login')