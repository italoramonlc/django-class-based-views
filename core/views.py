
from django.views.generic import RedirectView





class HomeRedirectView(RedirectView):
    pattern_name = "projects:list_projects"