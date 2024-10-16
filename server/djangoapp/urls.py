from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [  # route is a string contains a URL pattern
                 # view refers to the view function
                 # name the URL
                 # path for about view
                 # path for contact us view
                 # path for registration
                 # path for login
                 # path for logout
                 # path for dealer reviews view
                 # path for adding a new review view
     path('register', view=views.registration, name='register'),
     path(route='login', view=views.login_user, name='login'),
     path(route='logout', view=views.logout_request, name='logout'),
     path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
     path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
     path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
     path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
     path(route='add_review', view=views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)