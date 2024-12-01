from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    rank_score = db.Column(db.Integer, nullable=False)
    main_position = db.Column(db.String(20), nullable=False)
    secondary_position = db.Column(db.String(20))
    top_skill = db.Column(db.Integer, default=0)
    jungle_skill = db.Column(db.Integer, default=0)
    mid_skill = db.Column(db.Integer, default=0)
    adc_skill = db.Column(db.Integer, default=0)
    support_skill = db.Column(db.Integer, default=0)
    win_count = db.Column(db.Integer, default=0)  # 승리 수
    loss_count = db.Column(db.Integer, default=0)  # 패배 수
    win_rate = db.Column(db.Float)  # 승률
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Team(db.Model):
    __tablename__ = 'teams'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, nullable=False)
    team_name = db.Column(db.String(50), nullable=False)
    total_score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

class TeamPlayer(db.Model):
    __tablename__ = 'team_players'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    
    team = db.relationship('Team', back_populates='players')
    player = db.relationship('Player', back_populates='teams')

class GameResult(db.Model):
    __tablename__ = 'game_results'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, nullable=False)
    winning_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    losing_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    game_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    winning_team = db.relationship('Team', foreign_keys=[winning_team_id])
    losing_team = db.relationship('Team', foreign_keys=[losing_team_id])

# 관계 설정 (선택 사항)
Team.players = db.relationship('TeamPlayer', back_populates='team')
Player.teams = db.relationship('TeamPlayer', back_populates='player')

