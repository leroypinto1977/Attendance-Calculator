from django.shortcuts import render

from .models import Attendance, StudentCourses

import json

# Create your views here.

def attendance(request):
  username = "Leroy"
  student = StudentCourses.objects.get(username = username)
  subjects = ["subject1", "subject2", "subject3", "subject4", "subject5", "subject6", "subject7", "subject8", "subject9", "subject10", "subject11", "subject12", "subject13", "subject14", "subject15", "subject16", "subject17", "subject18", "subject19", "subject20"]
  subjects_list = []
  subjects_percentage = []
  total_classes = []
  no_of_class_absent = []
  no_of_class_present = []

  for i in subjects:
    if getattr(student, i):
      subject = getattr(student,i)
      subjects_list.append(subject)
      total = len(Attendance.objects.filter(username = username, subject = subject))
      total_classes.append(total)
      present = len(Attendance.objects.filter(username = username, subject = subject, class_attended = "1"))
      no_of_class_present.append(present)
      absent = len(Attendance.objects.filter(username = username, subject = subject, class_attended = "0"))
      no_of_class_absent.append(absent)
      if total != 0:
        percentage = round((present/total) * 100, 2)
      else: 
        percentage = 0
      subjects_percentage.append(percentage)

  subjects_list_json = json.dumps(subjects_list)
  total_json = json.dumps(total_classes)
  present_json = json.dumps(no_of_class_present)
  absent_json = json.dumps(no_of_class_absent)
  subjects_percentage_json = json.dumps(subjects_percentage)

  return render(request, "home/attendance.html", {"subjects_list_json": subjects_list_json, "total_json": total_json, "present_json": present_json, "absent_json": absent_json, "subjects_percentage_json": subjects_percentage_json})

def course_details(request):
  global number_of_subs
  if request.method == "POST":
    first_name = request.POST["firstname"]
    course = request.POST["course"]
    number_of_subs = request.POST["no_of_subs"]

    new_user = StudentCourses(username = first_name, course = course, number_of_subjects = number_of_subs)
    new_user.save()
      
    return render(request, "home/subjects.html", {"number_of_subs": number_of_subs})

    subject_variables = {}

    # Assuming you have a for loop to iterate and assign values
    for i in range(1, number_of_subs + 1):
        subject_name = f"subject_{i}";  # Dynamic variable name
        subject_value = request.POST[subject_name];  # Replace with your logic to get the value
        
        # Assign the value to the dynamic variable name in the dictionary
        subject_variables[subject_name] = subject_value;

    # Now, you can access the values using the dynamic variable names
    print(subject_variables["subject_1"])  # Access the value of subject_1
    print(subject_variables["subject_2"])
    



    # month = datetime.now().month
    # year = datetime.now().year
    # months = {
    #   1: "January",
    #   2: "February",
    #   3: "March",
    #   4: "April",
    #   5: "May",
    #   6: "June",
    #   7: "July",
    #   8: "August",
    #   9: "September",
    #   1: "January",
    #   2: "February",
    #   3: "March",
    #   4: "April",
    #   5: "May",
    #   6: "June",
    #   7: "July",
    #   8: "August",
    #   9: "September",
    #   10: "October",
    #   11: "November",
    #   12: "December"
    # }
    # if request.method == "POST":
    #   username = request.POST["reg_number"]
    #   eggtk_qn = int(request.POST["eggtk_qn"])
    #   tk_price = eggtk_qn * 200
    #   eggtk_month = int(request.POST["eggtk_month"])
    #   eggtk_month_str = months[eggtk_month]
    #   eggtk_year = request.POST["eggtk_year"]
    #   token = TokenOrder(username = username, quantity = eggtk_qn, tk_name = "egg", tk_year = eggtk_year, tk_month = eggtk_month_str, tk_price = tk_price)
    #   token.save()

    #   return render(request, "admin/admin2_eggToken.html", {"month": month, "year": year})

    # return render(request, "admin/admin2_eggToken.html", {"month": month, "year": year})

    # token = TokenOrder(username = username_c, quantity = 1, tk_name = "paneer", tk_number = tk_number, tk_date = pntk_new_obj, tk_year = token_year, tk_month = token_month_str, tk_price = 60)
    # token.save()

  return render(request, "home/course_details.html", {})

def subject_details(request):
  if request.method == "POST":
    # first_name = request.POST["firstname"]
    # course = request.POST["course"]
    # number_of_subs = request.POST["no_of_subs"]

    # new_user = StudentCourses(username = first_name, course = course, number_of_subjects = number_of_subs)
    # new_user.save()
      
    # return render(request, "attendance_calc/subjects.html", {"number_of_subs": number_of_subs})

    username = "Leroy"
    order = StudentCourses.objects.filter(username = username).last()
    number_sub = order.number_of_subjects
    subject_variables = {}

    # Assuming you have a for loop to iterate and assign values
    for i in range(1, number_sub + 1):
      subject_name = f"subject{i}"  # Dynamic variable name
      subject_value = request.POST[subject_name]  # Replace with your logic to get the value
      
      # Assign the value to the dynamic variable name in the dictionary
      setattr(order, subject_name, subject_value)
      order.save()

    # # Now, you can access the values using the dynamic variable names
    # print(subject_variables["subject_1"])  # Access the value of subject_1
    # print(subject_variables["subject_2"])
    
  return render(request, "home/course_details.html", {})


def enter_attendance(request):
  global subjects_list
  username = "Leroy"
  student = StudentCourses.objects.get(username = username)
  subjects = ["subject1", "subject2", "subject3", "subject4", "subject5", "subject6", "subject7", "subject8", "subject9", "subject10", "subject11", "subject12", "subject13", "subject14", "subject15", "subject16", "subject17", "subject18", "subject19", "subject20"]
  subjects_list = []
  

  for i in subjects:
    if getattr(student, i):
      subjects_list.append(getattr(student,i))

  subjects_json = json.dumps(subjects_list)

  if request.method == "POST":
    subject = request.POST.get("subject_drop")
    attendance = request.POST.get("radio", None)
    if attendance == "present":
      attendance_num = 1
    else: 
      attendance_num = 0

    order = Attendance(username = username, subject = subject, class_attended = attendance_num)
    order.save()

    return render(request, "home/enter_attendance.html", {"subjects_json": subjects_json})
  
  return render(request, "home/enter_attendance.html", {"subjects_json": subjects_json})

def settings(request):
  subjects_list = creating_subject_list()
  no_of_subs = len(subjects_list)
  return render(request, "home/settings.html", {"no_of_subs": no_of_subs})


def creating_subject_list():
  username = "Leroy"
  student = StudentCourses.objects.get(username = username)
  subjects = ["subject1", "subject2", "subject3", "subject4", "subject5", "subject6", "subject7", "subject8", "subject9", "subject10", "subject11", "subject12", "subject13", "subject14", "subject15", "subject16", "subject17", "subject18", "subject19", "subject20"]
  subjects_list = []
  
  for i in subjects:
    if getattr(student, i):
      subjects_list.append(getattr(student,i))

  return subjects_list