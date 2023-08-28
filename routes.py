from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = SQLAlchemy()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form['title']
        app.db.add(Title(title))
        app.db.commit()
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/<title>')
def show(title):
    title = Title.query.get(title)
    if title is None:
        return render_template('404.html'), 404
    return render_template('show.html', title=title)

@app.route('/edit/<title>')
def edit(title):
    title = Title.query.get(title)
    if title is None:
        return render_template('404.html'), 404
    return render_template('edit.html', title=title)

@app.route('/delete/<title>')
def delete(title):
    title = Title.query.get(title)
    if title is None:
        return render_template('404.html'), 404
    app.db.delete(title)
    app.db.commit()
    return redirect(url_for('index'))