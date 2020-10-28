from apis import api, mysql
from flask_restful import Resource, reqparse


# ADD A NEW TEAM API. ENDPOINT - http://localhost:5000/addteam/
class AddTeam(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('team_name', type=str, required=True,
                                   help='No team_name provided', location='json')
        self.reqparse.add_argument('coach_name', type=str, required=True,
                                   help='No coach_name provided', location='json')
        self.reqparse.add_argument('captain_name', type=str, required=True,
                                   help='No captain_name provided', location='json')
        super(AddTeam, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO team(team_name, coach_name, captain_name) values(%s, %s, %s  )",
                           (args['team_name'], args['coach_name'], args['captain_name']))
            mysql.connection.commit()
            cursor.close()
            return {'status': 'Inserted data successfully'}, 201
        except Exception as e:
            cursor.close()
            return {'error': e.__str__()}, 500
        finally:
            cursor.close()


# API TO ADD A NEW MATCH TO THE DATABASE. ENDPOINT - http://localhost:5000/addmatch/

class AddMatch(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('home_team', type=dict, required=True,
                                   help='home_team Not Provided', location='json')
        self.reqparse.add_argument('away_team', type=dict, required=True,
                                   help='away_team Not Provided', location='json')
        self.reqparse.add_argument('winner', type=str, required=True,
                                   help='winner Team Not Provided', location='json')
        self.reqparse.add_argument('man_of_the_match', type=str, required=True,
                                   help='man_of_the_match not provided', location='json')
        self.reqparse.add_argument('date', type=str, required=True,
                                   help='Date of match not provided', location='json')
        super(AddMatch, self).__init__()

    def post(self):
        team1 = self.reqparse.parse_args().pop('home_team')
        team2 = self.reqparse.parse_args().pop('away_team')
        args = self.reqparse.parse_args()
        try:
            cursor = mysql.connection.cursor()
            rs = cursor.execute("SELECT team_id from team where team_name=%s", (team1['team_name'],))
            if rs > 0:
                team1_id = cursor.fetchall()[0][0]
            rs = cursor.execute("SELECT team_id from team where team_name=%s", (team2['team_name'],))
            if rs > 0:
                team2_id = cursor.fetchall()[0][0]
            rs = cursor.execute("SELECT team_id from team where team_name=%s", (args['winner'],))
            if rs > 0:
                winner_id = cursor.fetchall()[0][0]
            cursor.execute("""INSERT INTO matches(home_team, away_team, winner_team, man_of_the_match,
            date_played) values(%s, %s, %s, %s, %s)""", (team1_id, team2_id, winner_id,
                                                         args['man_of_the_match'], args['date']))
            mysql.connection.commit()
            rs = cursor.execute("SELECT LAST_INSERT_ID()")
            if rs > 0:
                match_id = cursor.fetchall()[0][0]
            cursor.execute("INSERT INTO match_details values(%s, %s, %s, %s, %s, %s, %s)",
                           (match_id, team1_id, team1['fours'], team1['sixes'], team1['wickets'],
                            team1['score'], team1['isFirstInnings']))
            mysql.connection.commit()
            cursor.execute("INSERT INTO match_details values(%s, %s, %s, %s, %s, %s, %s)",
                           (match_id, team2_id, team2['fours'], team2['sixes'], team2['wickets'],
                            team2['score'], team2['isFirstInnings']))
            mysql.connection.commit()
            cursor.close()
            return {"status": "Inserted Match Successfully"}, 201
        except Exception as e:
            cursor.close()
            return {"error": e.__str__()}, 500
        finally:
            cursor.close()


# API TO GET ALL TEAMS FROM THE DATABASE. ENDPOINT - http://localhost:5000/getteams/

class GetAllTeams(Resource):
    def get(self):
        try:
            team_list = []
            objects = {}
            cursor = mysql.connection.cursor()
            rs = cursor.execute("SELECT * FROM team")
            if rs > 0:
                teams = cursor.fetchall()
            for team in teams:
                objects['team_name'] = team[1]
                objects['coach_name'] = team[2]
                objects['captain_name'] = team[3]
                team_list.append(objects)
                objects = {}
            cursor.close()
            return {
                       'team_list': team_list
                   }, 200
        except Exception as e:
            cursor.close()
            return {
                'error': e.__str__()
            }
        finally:
            cursor.close()


# API TO GET ALL MATCHES FROM THE DATABASE. ENDPOINT - http://localhost:5000/getallmatches/

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
                objects["match_id"] = matches[i][0]
                objects["home_team"] = home_team[0][0]
                objects["away_team"] = away_team[0][0]
                objects["winner"] = winner_team[0][0]
                objects["message"] = message
                objects["date_played"] = str(matches[i][5])
                all_matches.append(objects)
                objects = {}
            cursor.close()
            return all_matches, 200
        except Exception as e:
            cursor.close()
            return {"error": e.__str__()}, 500
        finally:
            cursor.close()


# API TO GET A SINGLE MATCH FROM THE DATABASE. ENDPOINT - http://localhost:5000/getmatch/<int:id>/


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
            cursor.close()
            return {
                       'match_id': match_id,
                       'winner': winner_team,
                       'man_of_the_match': man_of_the_match,
                       'date': str(date_played),
                       'team1': team1,
                       'team2': team2
                   }, 200

        except Exception as e:
            cursor.close()
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
        rs = cursor.execute("SELECT team_name, captain_name, coach_name from team where team_id=%s", (data[0][1],))
        if rs > 0:
            team_data = cursor.fetchall()
            team_name = team_data[0][0]
            captain_name = team_data[0][1]
            coach_name = team_data[0][2]
        team = {'team_id': data[0][1],
                'team_name': team_name,
                'coach_name': coach_name,
                'captain_name': captain_name,
                'matches_played': matches_played,
                'fours': data[0][2],
                'sixes': data[0][3],
                'wickets': data[0][4],
                'score': data[0][5]
                }
        cursor.close()
        return team
    except Exception as e:
        cursor.close()
        return {
            "error": e.__str__()
        }
    finally:
        cursor.close()


api.add_resource(GetAllMatches, "/getallmatches/")
api.add_resource(GetMatch, "/getmatch/<int:id>/")
api.add_resource(AddTeam, '/addteam/')
api.add_resource(AddMatch, '/addmatch/')
api.add_resource(GetAllTeams, '/getteams/')
