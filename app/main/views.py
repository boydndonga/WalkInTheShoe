from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
from flask_login import login_required, current_user
from app.models import Post, User
from .forms import PostForm


@main.route('/')
def index():
    posts = Post.get_posts()
    return render_template('index.html', posts=posts)


@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(
            body=form.body.data,
            author=current_user._get_current_object())
        new_post.save_post()
        return redirect(url_for('.index'))
    return render_template('main/new_post.html', post_form=form)


@main.route('/post/<int:id>')
def post(id):
    post = Post.load_post(id)
    # projects = Project.query.filter_by(post_id=id).all()
    return render_template('main/post.html', post=post)


# @main.route('/post/comment/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):
#     form = Commentform()
#     movie = get_movie(id)
#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data

#         # Updated review instance
#         new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)

#         # save review method
#         new_review.save_review()
#         return redirect(url_for('.movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_review.html',title = title, review_form=form, movie=movie)

