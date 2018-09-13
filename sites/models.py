from django.db import models


# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=128, verbose_name='网站名')
    url = models.CharField(max_length=256, verbose_name='网址')

    contact_type_choices = ((0, 'QQ'),
                            (1, '微信'),
                            (2, '邮箱'),
                            (3, '手机'),
                            (4, '其他'))

    contact_type = models.IntegerField(verbose_name='联系方式', choices=contact_type_choices)
    contact = models.CharField(max_length=32, verbose_name='联系人')
    sort = models.IntegerField(db_index=True, verbose_name='排序', default=0, help_text='升序，默认为0')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '友联'
        verbose_name_plural = '友联管理'

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    content = models.TextField(max_length=1024, verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    published = models.BooleanField(verbose_name='发布状态', default=True)

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告管理'

    def __str__(self):
        return self.title


class Menu(models.Model):
    name = models.CharField(max_length=16, verbose_name='菜单名')
    url = models.CharField(max_length=128, verbose_name='链接')
    sort = models.IntegerField(db_index=True, default=0, verbose_name='排序', help_text='升序')

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = '菜单管理'

    def __str__(self):
        return self.name
