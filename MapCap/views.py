from django.shortcuts import render
from django.http import HttpResponse


def my_map(request):
    key = str('AIzaSyCw6G6AnBOLTw1tcl3n4sxxvIPZTqO2khQ')
    return render(request, 'MapCap/Basic_Map_Page.html',  {
            'key': key,
    })


def normal_profile_map(request):
    key = str('AIzaSyCw6G6AnBOLTw1tcl3n4sxxvIPZTqO2khQ')
    return render(request, 'MapCap/Normal_Profile_Add_Location.html',  {
            'key': key,
    })
