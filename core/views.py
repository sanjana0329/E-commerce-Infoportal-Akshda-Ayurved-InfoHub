from django.db.models import Value
from accounts.forms import SignUpForm
from accounts.models import CustomUser
from accounts.models import USER_TYPES
from core.forms import *
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required,permission_required
from django.core import files
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models import Q 
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView,
    DetailView,
    View,
    ListView,
    DetailView,
)
from django.http import (
    JsonResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    HttpResponse
)
from http.client import HTTPResponse
from django.shortcuts import (
    render,redirect
)
import os
from templates import *
from django.contrib.auth import update_session_auth_hash
from accounts.models import *
from .forms import *
from django.http import FileResponse, Http404
from django.views.decorators.http import require_POST

from io import BytesIO
from django.db.models.functions import Upper,Replace
from django.db.models import Prefetch
from django.db.models import OuterRef, Subquery
from .decorators import *
from core.email_send_config import send_admin_mail, send_user_mail
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

User = get_user_model()

TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"

# FOR HOME/DASHBOARD 
@method_decorator(has_permissions_mixin, name='dispatch')
class MyProfileView(View):
    template_name = './core/myprofile.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name,context=context)

    def post(self, request):
        ...
        

