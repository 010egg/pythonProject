from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    upvotes = db.Column(db.Integer, default=0)
    comments = db.relationship('Comment', backref='article', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>', methods=['GET', 'POST'])
def article(article_id):
    article = Article.query.get_or_404(article_id)
    if request.method == 'POST':
        comment_content = request.form['content']
        new_comment = Comment(content=comment_content, article=article)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('article', article_id=article_id))
    return render_template('article.html', article=article)

@app.route('/create_article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_article = Article(title=title, content=content)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_article.html')

@app.route('/like_comment/<int:comment_id>', methods=['GET']) # 更改为 GET
def like_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    comment.upvotes += 1
    db.session.commit()
    return redirect(url_for('article', article_id=comment.article_id))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

