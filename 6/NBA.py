import re
def nba_cup(result_sheet, to_find):
    '''
    a team marks 3 if it is a win
    a team marks 1 if it is a draw
    a team marks 0 if it is a loss.
    Team Name:W=nb of wins;D=nb of draws;L=nb of losses;Scored=nb;Conceded=nb;Points=nb
    '''
    if not to_find in result_sheet:
        return "{}:This team didn't play!".format(to_find)
    if to_find == '':
        return ''

    games = result_sheet.split(',')
    matching = [s for s in games if to_find in s]
    teamsum = 0
    oppsum = 0
    wins = 0
    losses = 0
    draws = 0
    for game in matching:
        points = [int(s) for s in game.split() if s.isdigit()]
        if len(points) < 2:
            return "Error(float number):{}".format(game)
        newg = game.replace(' ','')
        s = to_find.replace(' ','') + '([0-9]*)'
        regex = re.compile(s)
        score_team_1 = int(regex.findall(newg)[0])
        score_team_2 = [num for num in points if num != score_team_1][0]
        teamsum += score_team_1
        oppsum += score_team_2
        if score_team_1 > score_team_2:
            wins += 1
        elif score_team_1 < score_team_2:
            losses += 1
        else:
            draws += 1


    totalp = (wins * 3) + (draws * 1)


    return '{}:W={};D={};L={};Scored={};Conceded={};Points={}'.format(to_find,wins,draws,losses,teamsum,oppsum,totalp)


if __name__ == '__main__':
    r = ("Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,"
     "Los Angeles Lakers 111 Minnesota Timberwolves 112,Phoenix Suns 95 Dallas Mavericks 111,Portland Trail Blazers 112 New Orleans Pelicans 94,"
     "Sacramento Kings 104 Los Angeles Clippers 111,Houston Rockets 85 Denver Nuggets 105,Memphis Grizzlies 76 Cleveland Cavaliers 106,"
     "Milwaukee Bucks 97 New York Knicks 122,Oklahoma City Thunder 112 San Antonio Spurs 106,Boston Celtics 112 Philadelphia 76ers 95,"
     "Brooklyn Nets 100 Chicago Bulls 115,Detroit Pistons 92 Utah Jazz 87,Miami Heat 104 Charlotte Hornets 94,"
     "Toronto Raptors 106 Indiana Pacers 99,Orlando Magic 87 Washington Wizards 88,Golden State Warriors 111 New Orleans Pelicans 95,"
     "Atlanta Hawks 94 Detroit Pistons 106,Chicago Bulls 97 Cleveland Cavaliers 95,"
     "San Antonio Spurs 111 Houston Rockets 86,Chicago Bulls 103 Dallas Mavericks 102,Minnesota Timberwolves 112 Milwaukee Bucks 108,"
     "New Orleans Pelicans 93 Miami Heat 90,Boston Celtics 81 Philadelphia 76ers 65,Detroit Pistons 115 Atlanta Hawks 87,"
     "Toronto Raptors 92 Washington Wizards 82,Orlando Magic 86 Memphis Grizzlies 76,Los Angeles Clippers 115 Portland Trail Blazers 109,"
     "Los Angeles Lakers 97 Golden State Warriors 136,Utah Jazz 98 Denver Nuggets 78,Boston Celtics 99 New York Knicks 85,"
     "Indiana Pacers 98 Charlotte Hornets 86,Dallas Mavericks 87 Phoenix Suns 99,Atlanta Hawks 81 Memphis Grizzlies 82,"
     "Miami Heat 110 Washington Wizards 105,Detroit Pistons 94 Charlotte Hornets 99,Orlando Magic 110 New Orleans Pelicans 107,"
     "Los Angeles Clippers 130 Golden State Warriors 95,Utah Jazz 102 Oklahoma City Thunder 113,San Antonio Spurs 84 Phoenix Suns 104,"
     "Chicago Bulls 103 Indiana Pacers 94,Milwaukee Bucks 106 Minnesota Timberwolves 88,Los Angeles Lakers 104 Portland Trail Blazers 102,"
     "Houston Rockets 120 New Orleans Pelicans 100,Boston Celtics 111 Brooklyn Nets 105,Charlotte Hornets 94 Chicago Bulls 86,"
     "Cleveland Cavaliers 103 Dallas Mavericks 97")

    r0="New York Knicks 101.12 Atlanta Hawks 112"

    print(nba_cup(r, "Los Angeles Clippers"))
    print(nba_cup(r,'Boston Celts'))
    print(nba_cup(r0,'Atlanta Hawks'))
