from flask import render_template,url_for,flash, request, redirect, Blueprint
from flask_login import  current_user,login_required
from companyblog import db
from companyblog.models import BlogPost
from companyblog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint("blog_posts",__name__)

#CREATE
@blog_posts.route("/create", methods=["GET","POST"])
@login_required
def create_post():
    form = BlogPostForm

    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id
                             )

        db.session.add(blog_post)
        db.session.commit()
        flash("Blog Post Created")

        return redirect(url_for("core.index"))

    return render_template("create_post.html", form=form)


#READ
#UPDATE
#DALETE