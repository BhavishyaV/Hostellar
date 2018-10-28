from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Room
from StudentProfile.models import Profile
from .forms import BlockForm,FloorForm, RoomForm

def block_select(request):
    form = BlockForm(request.POST or None)
    if form.is_valid():
        text = form.cleaned_data['block']
        room =Room.objects.get(id=1)
        return HttpResponseRedirect(room.get_absolute_url() + text + '/')
    context={
        "form":form
    }
    return render(request,'rooms/selectBlock.html',context)

def floor_select(request,block):
    form = FloorForm(request.POST or None)
    if form.is_valid():
        text = str(form.cleaned_data['floor'])
        room =Room.objects.get(id=1)
        return HttpResponseRedirect(room.get_absolute_url() + block + '/' + text + '/')
    context={
        "form":form
    }
    return render(request,'rooms/selectFloor.html',context)

def room_select(request,block,floor):
    student =Profile.objects.get(student=request.user)
    rooms=Room.objects.filter(block=block,floor=floor).order_by('room_no')
    form = RoomForm(request.POST or None)
    if form.is_valid():
        rno = form.cleaned_data['room_no']
        selected_room= Room.objects.get(block=block,room_no=rno)
        selected_room.availability=0
        selected_room.save()
        #curr_room = Room.objects.get(id=student.roomID_id)
        #curr_room.availability=1
        #curr_room.save()
        student.roomID = selected_room
        student.save()
        if (selected_room.occupancy == 1):
            return HttpResponseRedirect(student.get_absolute_url())
        else:
            return HttpResponseRedirect('/roommate')
    context={
        'form':form,
        'rooms':rooms,
        'blk':block,
        'floor':floor,
    }
    return render(request,'rooms/FloorPlan.html',context)



def details(request,id):
    room = Room.objects.get(id=id)
    context = {
        'room': room,
    }
    return render(request,'rooms/details.html',context)
   