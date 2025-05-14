from Mywiki import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True) # システムで使う番号
    title = db.Column(db.String(30), nullable=False) # 記事タイトル
    content = db.Column(db.String(400), nullable=False) # 本文
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now) # 作成日時
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now) # 最終編集日時
    tags = db.Column(db.String(20))
    version = db.Column(db.Integer, default=1)
