# home/admin.py

from django.contrib import admin
from apps.team.models import TeamMember

admin.site.register(TeamMember)


