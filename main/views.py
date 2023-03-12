from django.shortcuts import render, redirect
from .models import reservation
from django.utils import timezone
from . import seat

# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST.get("student_number") != "" and len(request.POST.get("student_number")) == 6:
            return redirect('main:start', int(request.POST.get("student_number")), request.POST.get("room"))
        else:
            error_msg = []
            if request.POST.get("student_number") == "":
                error_msg.append("학번을 입력하세요")
            if len(request.POST.get("student_number")) != 6:
                error_msg.append("학번을 정확히 입력하세요(예: 221323)")
            context = {'seats':seat.seats.keys, "error_msg":error_msg}
            return render(request, "main/main.html", context)
    context = {'seats':seat.seats.keys}
    return render(request, "main/main.html", context)

def start(request, number, room_id):
    r = reservation.objects.filter(date=timezone.now().date())
    reserved = []
    for a in seat.seats[room_id]:
        reserved.append([])
        for b in a:
            reserved[-1].append(r.filter(seat=room_id + b))
    context = {'student':str(number), 'seats':seat.seats[room_id], 'reserved':reserved, "room":room_id}
    return render(request, "main/reserve.html", context)

def reserve(request, number):
    if request.method == "POST":
        if not reservation.objects.filter(student=number).filter(date=timezone.now().date()) and not reservation.objects.filter(seat=request.POST.get("seat")).filter(date=timezone.now().date()):
            print(number)
            r = reservation(seat=request.POST.get("seat"), date=timezone.now().date(), student=number)
            r.save()
            return redirect('main:main')
        else:
            error_msg = []
            if reservation.objects.filter(student=number).filter(date=timezone.now().date()):
                error_msg.append("이미 예약하셨습니다.")
            else:
                error_msg.append("이미 예약된 좌석입니다.")
            context = {'student':number, "error_msg":error_msg}
            return render(request, "main/reserve.html", context)

def dashBoard(request):
    r = reservation.objects.filter(date=timezone.now().date())
    reserved = {}
    for a in seat.seats.keys:
        reserved[a] = []
        for b in seat.seats[a]:
            for c in b:
                reserved[a].append(r.filter(seat=a + c))
    context = {'student':str(number), 'seats':seat.seats[room_id], 'reserved':reserved}
