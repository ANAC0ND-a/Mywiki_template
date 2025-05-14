from flask import render_template, request, redirect, url_for
from Mywiki import db
from Mywiki.models.article import Article

from Mywiki import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'GET':
        return render_template('add_article.html')
    if request.method == 'POST':
        form_title = request.form.get('title')
        form_content = request.form.get('content')
        form_tags = request.form.get('tags')

        article = Article(
            title=form_title,
            content=form_content,
            tags=form_tags
        )
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/articles')
def article_list():
    articles = Article.query.all()
    return render_template('/article_list.html', articles=articles)