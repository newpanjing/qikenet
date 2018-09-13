from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from sites.models import Menu
from qikenet import api
from device.models import Device
from device.models import Firmware
from device.models import Profile


def home(request):
    return render(request, 'index.html')


def device(request):
    return render(request, 'device.html')


def device_detail(request, name):
    devices = Device.objects.filter(type=name).order_by('sort').all()

    return render(request, 'device_detail.html', {
        'name': name,
        'devices': devices
    })


def beta(request):
    profiles = Profile.objects.order_by("sort").all()
    return render(request, 'beta.html', {
        'profiles': profiles
    })


def history(request):
    releases = api.get_releases()
    return render(request, 'history.html', {
        'releases': releases
    })


def firmware(request, id):
    # 查询固件
    firmwares = Firmware.objects.filter(identifier=id).all()
    device = None

    if len(firmwares) != 0:
        device = firmwares[0].device

    return render(request, 'firmware.html', {
        'id': id,
        'firmwares': firmwares,
        'device': device
    })


def firmware_detail(request, device, id):
    firmware = Firmware.objects.filter(id=id).get()
    return render(request, 'firmware_detail.html', {
        'id': id,
        'device': device,
        'firmware': firmware
    })


def device_query(request):
    model = request.GET['model']
    rs = api.get_model(model)
    if rs:
        return HttpResponseRedirect("/firmware/{}".format(rs["identifier"]))
    else:
        return render(request, 'device.html', {
            'error': True
        })
