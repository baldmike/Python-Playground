import django
from apps.leagues.models import *

# football_leagues = League.objects.filter(sport='Football')
# for league in football_leagues:
#     print league.name
#     teams = league.teams.all()
#     for team in teams:
#         print '\t', team.location, team.team_name
#         players = team.curr_players.filter(first_name__startswith='D')
#         for player in players:
#             print '\t\t', player.first_name, player.last_name


# #...all baseball leagues 
# baseball_leagues = League.objects.filter(sport = 'Baseball')
# for league in baseball_leagues:
#     print league.name
# print ('*') * 50

# #all womens' leagues
# womens_leagues = League.objects.filter(name__contains='Womens')
# for league in womens_leagues:
#     print league.name
# print ('*') * 50

# #..all leagues where sport is any type of hockey
# hockey_leagues = League.objects.filter(sport__contains='Hockey')
# for league in hockey_leagues:
#     print league.name 
# print ('*') * 50

# #..all leagues where sport is something OTHER THAN football
# not_football_leagues = League.objects.exclude(sport = 'Football')
# for league in not_football_leagues:
#     print league.name
# print ('*') * 50

# #...all leagues that call themselves "conferences"
# conferences = League.objects.filter(name__contains='Conference')
# for league in conferences:
#     print league.name
# print ('*') * 50

# #...all leagues in the Atlantic region
# atlantic_leagues = League.objects.filter(name__contains='Atlantic')
# for league in atlantic_leagues:
#     print league.name
# print ('*') * 50

# #...all teams based in Dallas
# dallas_teams = Team.objects.filter(location='Dallas')
# for team in dallas_teams:
#     print team.location, team.team_name
# print ('*') * 50

# #...all teams named the Raptors
# raptors_teams = Team.objects.filter(team_name='Raptors')
# for team in raptors_teams:
#     print team.location, team.team_name
# print ('*') * 50

# #...all teams whose location includes "City"
# city_teams = Team.objects.filter(location__contains='City')
# for team in city_teams:
#     print team.location, team.team_name
# print ('*') * 50

# #...all teams whose names begin with "T"
# team_with_T = Team.objects.filter(team_name__startswith='T')
# for team in team_with_T:
#     print team.location, team.team_name
# print ('*') * 50

# #...all teams, ordered alphabetically by location
# team_ordered_alphabetically = Team.objects.order_by('location')
# for team in team_ordered_alphabetically:
#     print team.location, team.team_name
# print ('*') * 50

# #...all teams, ordered by team name in reverse alphabetical order
# team_ordered_reverse_alphabetically = Team.objects.order_by('-team_name')
# for team in team_ordered_reverse_alphabetically:
#     print team.team_name
# print ('*') * 50

#...every player with last name "Cooper"
def cooper():
    play_Cooper = Player.objects.filter(last_name="Cooper")
    for player in play_Cooper:
        print player.first_name, player.last_name


# every player with first name "Joshua"
def joshua():
    play_Joshua = Player.objects.filter(first_name='Joshua')
    for player in play_Joshua:
        print player.first_name, player.last_name

# every play with last name "Cooper" except "Joshua"
def cooper_not_joshua():
    play_cooper_not_josh = Player.objects.filter(last_name="Cooper").exclude(first_name='Joshua')
    for player in play_cooper_not_josh:
        print player.first_name, player.last_name

# players with first name "Alexander" or "Wyatt"
def alex_or_wyatt():
    play_alex_or_wyatt = Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt')
    for player in play_alex_or_wyatt:
        print player.first_name, player.last_name

# STARTING SPORTS ORM 2

# all teams in the Atlantic Soccer Conference
def asc_teams():
    league = League.objects.filter(name='Atlantic Soccer Conference')
    for l in league:
        teams = l.teams.all()
        for team in teams:
            print team.team_name

# all current players on the Boston Penguins
def bp_players():
    penguins = Team.objects.filter(team_name='Penguins', location="Boston")
    for team in penguins:
        players = team.curr_players.all()
        for player in players:
            print player.first_name, player.last_name

# all current players in the International Collegiate Baseball Conference
def icbc_players():
    league = League.objects.filter(name='International Collegiate Baseball Conference')
    for l in league:
        teams = l.teams.all()
        for team in teams:
            players = team.curr_players.all()
            for player in players:
                print player.first_name, player.last_name

# all current players in the American Conference of Amateur Football with last name "Lopez"
def acaf_players_lopez():
    league = League.objects.filter(name='American Conference of Amateur Football')
    for l in league:
        teams = l.teams.all()
        for team in teams:
            players = team.curr_players.filter(last_name='Lopez')
            for player in players:
                print player.first_name, player.last_name

# all football players
def football_players():
    league = League.objects.filter(sport='Football')
    for l in league:
        teams = l.teams.all()
        for team in teams:
            players = team.curr_players.all()
            for player in players:
                print player.first_name, player.last_name

# all teams with a current player named 'Sophia'
def teams_with_sophia():
    teams = Player.objects.filter(first_name='Sophia')
    for i in teams:
        team=i.curr_team
        print team




   
    