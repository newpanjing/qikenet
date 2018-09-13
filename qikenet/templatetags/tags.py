from sites.models import Menu
from sites.models import Link
from sites.models import Notice
from django import template
import datetime

register = template.Library()  # 这一句必须这样写


@register.simple_tag
def common_data():
    menus = Menu.objects.all().order_by('sort')
    links = Link.objects.all().order_by('sort')
    notice = Notice.objects.filter(published=True).last()

    return {
        'menus': menus,
        'links': links,
        'notice': notice
    }


@register.filter
def utc_date(text):
    date = datetime.datetime.strptime(text, '%Y-%m-%dT%H:%M:%SZ')
    return date

