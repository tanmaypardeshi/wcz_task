from apis import api, mysql
from flask_restful import Resource, reqparse


class AddTeam(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Team Name', type=str, required=True,
                                   help='No Team Name provided', location='json')
        self.reqparse.add_argument('Coach Name', type=str, required=True,
                                   help='No Coach Name provided', location='json')
        self.reqparse.add_argument('Captain Name', type=str, required=True,
                                   help='No Captain Name provided', location='json')
        super(AddTeam, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO team(team_name, coach_name, captain_name) values(%s, %s, %s  )",
                           (args['Team Name'], args['Coach Name'], args['Captain Name']))
            mysql.connection.commit()
            return {'status': 'Inserted data successfully'}, 201
        except Exception as e:
            return {'error': e.__str__()}, 500
        finally:
            cursor.close()


class AddMatch(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Home Team', type=dict, required=True,
                                   help='Home Team Not Provided', location='json')
        self.reqparse.add_argument('Away Team', type=dict, required=True,
                                   help='Away Team Not Provided', location='json')
        self.reqparse.add_argument('Winner', type=str, required=True,
                                   help='Winner Team Not Provided', location='json')
        self.reqparse.add_argument('Man of the Match', type=str, required=True,
                                   help='Man of the Match not provided', location='json')
        self.reqparse.add_argument('Date', type=str, required=True,
                                   help='Date of match not provided', location='json')
        super(AddMatch, self).__init__()

    def post(self):
        team1 = self.reqparse.parse_args().pop('Home Team')
        team2 = self.reqparse.parse_args().pop('Away Team')
        args = self.reqparse.parse_args()
        try:
            cursor = mysql.connection.cursor()
            rs = cursor.execute("SELECT team_id from team where team_name=%s", (team1['Team Name'], ))
            if rs > 0:
                team1_id = cursor.fetchall()[0][0]
            rs = cursor.execute("SELECT team_id from team where team_name=%s", (team2['Team Name'],))
            if rs > 0:
                team2_id = cursor.fetchall()[0][0]
            rs = cursor.execute("SELECT team_id from team where team_name=%s", (args['Winner'],))
            if rs > 0:
                winner_id = cursor.fetchall()[0][0]
            rs = cursor.execute("""SELECT AUTO_INCREMENT from information_schema.TABLES where
                                table_schema=%s and table_name=%s""", ('cricket', 'matches'))
            if rs > 0:
                match_id = cursor.fetchall()[0][0]
            cursor.execute("""INSERT INTO matches values(%s, %s, %s, %s, %s, %s)""",
                           (match_id, team1_id, team2_id, winner_id, args['Man of the Match'], args['Date']))
            mysql.connection.commit()
            cursor.execute("INSERT INTO match_details values(%s, %s, %s, %s, %s, %s, %s)",
                           (match_id, team1_id, team1['Fours'], team1['Sixes'], team1['Wickets'],
                            team1['Score'], team1['isFirstInnings']))
            mysql.connection.commit()
            cursor.execute("INSERT INTO match_details values(%s, %s, %s, %s, %s, %s, %s)",
                           (match_id, team2_id, team2['Fours'], team2['Sixes'], team2['Wickets'],
                            team2['Score'], team2['isFirstInnings']))
            mysql.connection.commit()
            return {"status": "Inserted Match Successfully"}, 201
        except Exception as e:
            return {"error": e.__str__()}, 500
        finally:
            cursor.close()


class GetAllMatches(Resource):
    def get(self):
        try:
            message = ''
            home_team = ''
            away_team = ''
            winner_team = ''
            all_matches = []
            objects = {}
            cursor = mysql.connection.cursor()
            get_match = cursor.execute("SELECT * FROM matches order by date_played desc")
            if get_match > 0:
                matches = cursor.fetchall()

            for i in range(get_match):
                rs = cursor.execute("SELECT team_name from team where team_id=%s", (matches[i][1],))
                if rs > 0:
                    home_team = cursor.fetchall()
                rs = cursor.execute("SELECT team_name from team where team_id=%s", (matches[i][2],))
                if rs > 0:
                    away_team = cursor.fetchall()
                rs = cursor.execute("SELECT team_name from team where team_id=%s", (matches[i][3],))
                if rs > 0:
                    winner_team = cursor.fetchall()
                rs = cursor.execute(
                    "SELECT score, no_of_wickets, isFirstInnings from match_details where match_id=%s and team_id=%s"
                    , (matches[i][0], matches[i][1]))
                if rs > 0:
                    get_match_details1 = cursor.fetchall()
                team1 = {
                    'first': get_match_details1[0][2],
                    'wickets': get_match_details1[0][1],
                    'score': get_match_details1[0][0]
                }
                rs = cursor.execute(
                    "SELECT score, no_of_wickets, isFirstInnings from match_details where match_id=%s and team_id=%s"
                    , (matches[i][0], matches[i][2]))
                if rs > 0:
                    get_match_details2 = cursor.fetchall()
                team2 = {
                    'first': get_match_details2[0][2],
                    'wickets': get_match_details2[0][1],
                    'score': get_match_details2[0][0]
                }
                difference = team1['score'] - team2['score']
                if team1['first'] == 1:
                    if difference > 0:
                        message = f"Team {winner_team[0][0]} won by {difference} runs."
                    else:
                        message = f"Team {winner_team[0][0]} won by {10 - team2['wickets']} wickets."
                else:
                    if difference > 0:
                        message = f"Team {winner_team[0][0]} won by {10 - team1['wickets']} wickets."
                    else:
                        message = f"Team {winner_team[0][0]} won by {difference} runs."
                objects["Match ID"] = matches[i][0]
                objects["Home Team"] = home_team[0][0]
                objects["Away Team"] = away_team[0][0]
                objects["Winner Team"] = winner_team[0][0]
                objects["Winning score/wicket"] = message
                all_matches.append(objects)
                objects = {}
            return all_matches, 200
        except Exception as e:
            return {"error": e.__str__()}, 500
        finally:
            cursor.close()


class GetMatch(Resource):
    def get(self, id):
        try:
            cursor = mysql.connection.cursor()
            rs = cursor.execute("SELECT * from matches where match_id=%s", (id,))
            if rs > 0:
                match = cursor.fetchall()
            match_id = match[0][0]
            rs = cursor.execute("SELECT * from team where team_id=%s", (match[0][1],))
            if rs > 0:
                team1 = get_team_detail(cursor.fetchall(), match_id)
            cursor.execute("SELECT * from team where team_id=%s", (match[0][2],))
            if rs > 0:
                team2 = get_team_detail(cursor.fetchall(), match_id)
            cursor.execute("SELECT team_name from team where team_id=%s", (match[0][3],))
            if rs > 0:
                winner_team = cursor.fetchall()[0][0]
            man_of_the_match = match[0][4]
            date_played = match[0][5]
            return {
                       'Match ID': match_id,
                       'Winner Team': winner_team,
                       'Man Of The Match': man_of_the_match,
                       'Date of Match': str(date_played),
                       'team1': team1,
                       'team2': team2
                   }, 200
        except Exception as e:
            return {
                       "error": e.__str__()
                   }, 500
        finally:
            cursor.close()


def get_team_detail(data, match_id):
    try:
        cursor = mysql.connection.cursor()
        rs = cursor.execute("SELECT COUNT(*) from match_details where team_id=%s", (data[0][0],))
        if rs > 0:
            matches_played = cursor.fetchall()[0][0]
        rs = cursor.execute("""SELECT * from match_details
                        where team_id=%s and match_id=%s""", (data[0][0], match_id))
        if rs > 0:
            data = cursor.fetchall()
        rs = cursor.execute("SELECT team_name from team where team_id=%s", (data[0][1], ))
        if rs > 0:
            team_name = cursor.fetchall()[0][0]
        team = {'Team ID': data[0][1],
                'Team Name': team_name,
                'Coach Name': data[0][2],
                'Captain Name': data[0][3],
                'Matches Played': matches_played,
                'Number of Fours': data[0][2],
                'Number of Sixes': data[0][3],
                'Number of Wickets Lost': data[0][4],
                'Score': data[0][5]
                }
        return team
    except Exception as e:
        return {
            "error": e.__str__()
        }
    finally:
        cursor.close()


api.add_resource(GetAllMatches, "/getallmatches/")
api.add_resource(GetMatch, "/getmatch/<int:id>/")
api.add_resource(AddTeam, '/addteam/')
api.add_resource(AddMatch, '/addmatch/')