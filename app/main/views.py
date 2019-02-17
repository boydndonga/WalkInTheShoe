from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
from flask_login import login_required, current_user
from app.models import Post, User, Comment
from .forms import PostForm, CommentForm


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
    comments = Comment.query.filter_by(post_id=id).all()
    return render_template('main/post.html', post=post, comments=comments)


@main.route('/post/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    post = Post.load_post(id)
    if form.validate_on_submit():
        content = form.content.data

        # Updated review instance
        new_comment = Comment(
            post_id=post.id,
            content=content,
            user_id=current_user)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('.post', id=post.id))

    title = f'{post.body} post'
    return render_template(
        'main/new_comment.html',
        title=title,
        comment_form=form,
        post=post)