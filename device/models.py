from django.db import models


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=32, verbose_name='设备名')
    device_no = models.CharField(max_length=32, verbose_name='型号')
    type_choices = (('iPhone', 'iPhone'),
                    ('iPad', 'iPad'),
                    ('iPod', 'iPod'),
                    ('AppleTV', 'AppleTV'),
                    ('AppleWatch', 'AppleWatch'),
                    ('iTunes', 'iTunes'))
    type = models.CharField(db_index=True, max_length=16, verbose_name='类型', choices=type_choices)
    sort = models.IntegerField(db_index=True, verbose_name='排序', default=0, help_text='升序，从小到大')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备管理'

    def __str__(self):
        return self.name


class Firmware(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, verbose_name='设备', blank=True, null=True)
    identifier = models.CharField(max_length=32, verbose_name='型号', null=True, db_index=True)
    version = models.CharField(max_length=32, verbose_name='版本号', null=True)
    sha1_sum = models.CharField(max_length=128, verbose_name='sha1sum', null=True)
    file_size = models.BigIntegerField(verbose_name='文件大小', help_text='字节', default=0)
    url = models.CharField(max_length=512, verbose_name='下载地址', null=True)
    release_date = models.DateTimeField(verbose_name='发布时间', null=True)
    upload_date = models.DateTimeField(verbose_name='上传时间', null=True)
    signed = models.NullBooleanField(verbose_name='签名', default=True, null=True)
    create_date = models.DateTimeField(verbose_name='创建时间', blank=True, null=True, auto_now_add=True)
    build_id = models.CharField(max_length=32, verbose_name='BuildId', null=True)
    md5_sum = models.CharField(max_length=32, verbose_name='md5sum', null=True)

    class Meta:
        db_table = 'device_firmware'
        verbose_name = '固件'
        verbose_name_plural = '固件管理'

    def __str__(self):
        return '{}-{}'.format(self.device.name, self.version)


class Profile(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    file = models.FileField(verbose_name='描述文件')
    sort = models.IntegerField(verbose_name='排序', default=0, help_text='升序，从小到大')
    update_date = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '描述文件'
        verbose_name_plural = '描述文件管理'

    def __str__(self):
        return self.name
