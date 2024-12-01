import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='game_db'
    )

def get_players():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    cursor.close()
    connection.close()
    return players

def generate_teams(players):
    # 여기서는 승률과 점수 등을 기반으로 자동 팀 구성을 진행
    team_a = []
    team_b = []
    # 예시로 무작위로 나누는 간단한 코드
    players.sort(key=lambda x: x['rank_score'], reverse=True)
    for i in range(0, len(players), 2):
        if i % 2 == 0:
            team_a.append(players[i])
        else:
            team_b.append(players[i])
    
    return {'players': team_a, 'total_score': sum(p['rank_score'] for p in team_a)}, \
           {'players': team_b, 'total_score': sum(p['rank_score'] for p in team_b)}
