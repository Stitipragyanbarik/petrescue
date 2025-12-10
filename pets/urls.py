from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('report/', views.report_pet, name='report_pet'),
    path('match/<uuid:token>/approve/', views.match_approve, name='match_approve'),
    path('match/<uuid:token>/reject/', views.match_reject, name='match_reject'),
    path('contact/<int:cr_id>/', views.contact_request_view, name='contact_request'),
    path('contact/<int:cr_id>/owner/', views.contact_owner_view, name='contact_owner'),
    path('contact/inbox/', views.owner_inbox, name='owner_inbox'),
    path('image-check/', views.image_check, name='image_check'),
]
