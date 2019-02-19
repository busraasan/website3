from django.contrib import admin

from .models import Member, SubTeam, TeamLeader, TeamAdvisor, MembersPage, TechTeamLeader

models = [Member, SubTeam, TeamLeader, TeamAdvisor, MembersPage, TechTeamLeader]
admin.site.register(models)
