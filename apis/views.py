from apis import api, mysql
from flask_restful import Resource


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
                cursor.execute("SELECT team_name from team where team_id=%s", (matches[i][1],))
                home_team = cursor.fetchall()
                cursor.execute("SELECT team_name from team where team_id=%s", (matches[i][2],))
                away_team = cursor.fetchall()
                cursor.execute("SELECT team_name from team where team_id=%s", (matches[i][3],))
                winner_team = cursor.fetchall()
                cursor.execute(
                    "SELECT score, no_of_wickets, isFirstInnings from match_details where match_id=%s and team_id=%s"
                    , (matches[i][0], matches[i][1]))
                get_match_details1 = cursor.fetchall()
                team1 = {
                    'first': get_match_details1[0][2],
                    'wickets': get_match_details1[0][1],
                    'score': get_match_details1[0][0]
                }
                cursor.execute(
                    "SELECT score, no_of_wickets, isFirstInnings from match_details where match_id=%s and team_id=%s"
                    , (matches[i][0], matches[i][2]))
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
            cursor.execute("SELECT * from team where team_id=%s", (match[0][1],))
            team1 = get_team_detail(cursor.fetchall(), match_id)
            cursor.execute("SELECT * from team where team_id=%s", (match[0][2],))
            team2 = get_team_detail(cursor.fetchall(), match_id)
            cursor.execute("SELECT team_name from team where team_id=%s", (match[0][3],))
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
        cursor.execute("SELECT COUNT(*) from match_details where team_id=%s", (data[0][0], ))
        matches_played = cursor.fetchall()[0][0]
        cursor.execute("""SELECT * from match_details
                        where team_id=%s and match_id=%s""", (data[0][0], match_id))
        data = cursor.fetchall()
        team = {'Team ID': data[0][0],
                'Team Name': data[0][1],
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


api.add_resource(GetAllMatches, "/getallmatches")
api.add_resource(GetMatch, "/getmatch/<int:id>")
