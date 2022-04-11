from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import JobPost
from myapp.job_posts.forms import JobPostForm

job_posts = Blueprint('job_posts', __name__)

@job_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_job():
  form = JobPostForm()
  if form.validate_on_submit():
    job_post = JobPost(
      title=form.title.data,
      company=form.company.data,
      user_id=current_user.id,
      language=form.language.data,
      pay=form.pay.data,
      framework=form.framework.data,
      database=form.database.data
    )
    db.session.add(job_post)
    db.session.commit()
    flash('Job has been created')
    print('Job has been created')
    return redirect(url_for('core.index'))
  return render_template('create_job.html', form=form)


@job_posts.route('/<int:job_post_id>')
def job_post(job_post_id):
  job_post = JobPost.query.get_or_404(job_post_id)
  return render_template('job_post.html', title=job_post.title, date=job_post.date, job=job_post)

@job_posts.route('/<int:job_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(job_post_id):
  job_post = JobPost.query.get_or_404(job_post_id)

  if job_post.author != current_user:
    abort(403)

  form = JobPostForm()

  if form.validate_on_submit():
    job_post.title = form.title.data
    job_post.company = form.company.data
    job_post.pay = form.pay.data
    job_post.language = form.language.data
    job_post.framework = form.framework.data
    job_post.database = form.database.data
    db.session.commit()
    flash('Job has been updated')
    return redirect(url_for('job_posts.job_post', job_post_id=job_post.id))

  elif request.method == 'GET':
    form.title.data = job_post.title
    form.company.data = job_post.company
    form.pay.data = job_post.pay
    form.language.data = job_post.language
    form.framework.data = job_post.framework
    form.database.data = job_post.database

  return render_template('create_job.html', title='Updating', form=form)

@job_posts.route('/<int:job_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_job(job_post_id):
  job_post = JobPost.query.get_or_404(job_post_id)
  if job_post.author != current_user:
    abort(403)

  db.session.delete(job_post)
  db.session.commit()
  flash('Job post has been deleted')
  return redirect(url_for('core.index'))
