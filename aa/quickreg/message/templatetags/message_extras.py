from django import template
from users.models import CustomUser

register = template.Library()

@register.filter
def EMPLID_to_FnLn(value):
    f_name = CustomUser.objects.get(EMPLID = value).first_name
    l_name = CustomUser.objects.get(EMPLID = value).last_name
    return l_name + ', ' + f_name
