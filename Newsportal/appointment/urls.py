from django.urls import path
from .views import AppointmentView

urlpatterns = (
     path('appoint/', AppointmentView.as_view(template_name='templates/appoint.html'),
          name='appointment')
 )