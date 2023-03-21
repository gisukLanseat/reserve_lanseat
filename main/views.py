from django.shortcuts import render, redirect
from .models import reservation
from django.utils import timezone
from . import seat
from django.http import Http404

a= [
    [
        ['', '', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved', 'not_reserved'], 
        ['', 'not_reserved', '', '', '', '', '', '', '', '', '', '', ''], 
        ['221323', '', '', '', '', '', '', '', '', '', '', '', '']
        ], 
        [['', '', '', '', '', '', '', '', '', '', '', '', ''], 
        ['', '', '', '', '', '', '', '', '', '', '', '', ''], 
        ['20', '', '', '', '', '', '', '', '', '', '', '', '']
    ]
]

# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST.get("student_number") != "" and len(request.POST.get("student_number")) == 6:
            return redirect('main:start', int(request.POST.get("student_number")), request.POST.get("room"))
        else:
            error_msg = []
            if request.POST.get("student_number") == "":
                error_msg.append("학번을 입력하세요")
            if len(request.POST.get("student_number")) != 4:
                error_msg.append("학번을 정확히 입력하세요(예: 221323)")
            context = {'seats':seat.seats.keys, "error_msg":error_msg}
            return render(request, "main/main.html", context)
    context = {'seats':seat.seats.keys}
    return render(request, "main/main.html", context)

def get_reserved(room_id):
    r = reservation.objects.filter(date=timezone.now().date())
    reserved = []
    ids = []
    for a in seat.seats[room_id]:
        reserved.append([])
        ids.append([])
        for b in a:
            if r.filter(seat=room_id + b):
                reserved[-1].append(r.get(seat=room_id + b).student)
                ids[-1].append(str(r.get(seat=room_id + b).id))
            else:
                if (b == ""):
                    reserved[-1].append("")
                    ids[-1].append("")
                else:
                    reserved[-1].append("not_reserved")
                    ids[-1].append("")
    return [reserved, ids]

def start(request, number, room_id):
    
    reserved = get_reserved(room_id)
    print(reserved)
    context = {'student':str(number), 'seats':seat.seats[room_id], 'reserved':reserved[0], "room":room_id}
    return render(request, "main/reserve.html", context)

def reserve(request, number, room_id):
    if request.method == "POST":
        if not reservation.objects.filter(student=number).filter(date=timezone.now().date()) and not reservation.objects.filter(seat=request.POST.get("seat")).filter(date=timezone.now().date()):
            r = reservation(seat=request.POST.get("seat"), date=timezone.now().date(), student=number)
            r.save()
            return redirect('main:dashboard')
        else:
            error_msg = []
            if reservation.objects.filter(student=number).filter(date=timezone.now().date()):
                instance = reservation.objects.filter(student=number).filter(date=timezone.now().date()).filter(seat=request.POST.get("seat"))
                if instance:
                    instance[0].delete()
                else:
                    error_msg.append("이미 예약하셨습니다. 취소하려면 본인이 예약한 좌석을 선택하고 예약하기를 눌러주세요")
            else:
                error_msg.append("이미 예약된 좌석입니다.")
            reserved = get_reserved(room_id)
            return redirect('main:start', number, room_id)

def dashBoard(request):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            return redirect("common:login")
    else:
        return redirect("common:login")
    r = reservation.objects.filter(date=timezone.now().date())
    reserved = {}
    ids = {}
    for x in seat.seats:
        p = get_reserved(x)
        reserved[x] = p[0]
        ids[x] = p[1]
    context = {'seats':seat.seats, 'reserved':reserved, 'ids':ids}
    return render(request, "main/dashboard.html", context)

def cancel(request, id):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            return redirect("common:login")
    else:
        return redirect("common:login")
    r = reservation.objects.get(id=id)
    r.delete()
    return redirect("main:dashboard")
