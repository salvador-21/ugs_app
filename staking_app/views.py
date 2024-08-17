from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.utils import timezone
import datetime,time
import uuid
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.utils.crypto import get_random_string
from django.core import serializers
from django.core.serializers import serialize
import json
from django.db.models import Sum,Count
from django.utils import timezone

from django_minify_html.middleware import MinifyHtmlMiddleware
from django.http import HttpRequest, HttpResponse

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from django.template.loader import render_to_string
from django.http import HttpResponse
from decimal import Decimal
from django.urls import reverse
from datetime import datetime


def index(request):

    return render(request,'staking/index.html')