from flask import Flask, render_template, request, redirect, url_for
from models import db, Player
import random

app = Flask(__name__)

# 데이터베이스 연결 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:kjjk3415%21@127.0.0.1/game_balance_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', team_a=None, team_b=None)

@app.route('/generate_teams', methods=['POST'])
def generate_teams():
    # 입력된 플레이어 이름 가져오기
    player_names = request.form.get('players', '')
    player_names = [name.strip() for name in player_names.split(',')]

    # 데이터베이스에서 플레이어 정보 조회
    players = Player.query.filter(Player.name.in_(player_names)).all()

    if len(players) != 10:
        return "10명의 플레이어를 입력해야 합니다.", 400

    # 플레이어 리스트를 랜덤하게 섞고 팀 나누기
    random.shuffle(players)
    team_a = {
        'players': players[:5],
        'total_score': sum(player.rank_score for player in players[:5])
    }
    team_b = {
        'players': players[5:],
        'total_score': sum(player.rank_score for player in players[5:])
    }

    # 결과를 템플릿으로 전달
    return render_template('index.html', team_a=team_a, team_b=team_b)

if __name__ == '__main__':
    app.run(debug=True)
