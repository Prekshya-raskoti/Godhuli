from django.shortcuts import render
# views.py
from apps.team.models import TeamMember

def team_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'pages/team.html', {
        'team_members': team_members
    })


