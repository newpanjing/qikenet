import unittest
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'qikenet.settings'
django.setup()

from device.models import Device
from device.models import Firmware
from qikenet import api


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('开始')

    def test_save_device(self):
        devices = api.get_devices()

        for item in devices:
            # 判断类型
            name = str(item['name'])
            type = ''
            if name.find("iPhone") != -1:
                type = 'iPhone'
            elif name.find('iPad') != -1:
                type = 'iPad'
            elif name.find('iPod') != -1:
                type = 'iPod'
            elif name.find('Watch') != -1:
                type = 'AppleWatch'
            elif name.find('iTunes') != -1:
                type = 'iTunes'
            elif name.find('TV') != -1:
                type = 'AppleTV'

            if Device.objects.filter(name=name).exists():
                # print('数据存在')
                continue

            device = Device.objects.create(
                name=name,
                device_no=item['identifier'],
                type=type
            )
            device.save()
            print(device)

    def test_firmware(self):
        devices = Device.objects.all()
        for d in devices:

            firmware = api.get_firmware(d.device_no)
            if firmware is None or firmware.get('firmwares') is None:
                continue

            for f in firmware['firmwares']:

                buildid = f['buildid']
                identifier = f['identifier']

                if Firmware.objects.filter(build_id=buildid, identifier=identifier).exists():
                    # print('identifier={} build_id={} 存在'.format(identifier, buildid))
                    # 更新固件签名状态

                    continue

                db = Firmware.objects.create(
                    device=d,
                    identifier=identifier,
                    version=f['version'],
                    sha1_sum=f['sha1sum'],
                    md5_sum=f['md5sum'],
                    file_size=f['filesize'],
                    url=f['url'],
                    release_date=f['releasedate'],
                    upload_date=f['uploaddate'],
                    build_id=buildid,
                    signed=f['signed'],
                )
                db.save()
                print(f)

    def test_itunes(self):
        platforms = ['windows', 'macOS']
        for p in platforms:
            list = api.get_itunes(p)
            device = Device.objects.filter(device_no=p).get()
            for item in list:
                # 如果存在了，就不保存
                version = item['version']
                if Firmware.objects.filter(identifier=p, version=version).exists():
                    print('{}={} 存在'.format(p, version))
                    continue

                firmware = Firmware.objects.create(
                    device=device,
                    identifier=p,
                    version=version,
                    url=item['url'],
                    release_date=item['releasedate'],
                    upload_date=item['uploaddate'],
                )
                firmware.save()

                print(firmware)

        pass


if __name__ == '__main__':
    unittest.main()
