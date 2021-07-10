





def create_faculty(request):
    return render(request, 'administrator/create-faculty.html')



def create_student(request):
    return render(request, 'administrator/create-student.html')



def edit_institute_profile(request):
    # TODO: update institute profile
    return render(request, 'administrator/edit-institute-profile.html')


def dashboard(request):
    return render(request, 'administrator/dashboard.html', context=context)


def logout(request):
    return redirect('administrator:login')
