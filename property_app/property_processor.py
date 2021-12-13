from property_app.models import *
import datetime

def get_property_types(request):
    return{'property_type':PropertyType.objects.order_by('-id')}

def footer_date(request):
    return{'date_footer':datetime.datetime.now()}