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
    job_post = JobPost(title=form.title.data, company=form.company.data, user_id=current_user.id)
    db.session.add(job_post)
    db.session.commit()
    flash('Job has been created')
    print('Job has been created')
    return redirect(url_for('core.index'))
  return render_template('create_job.html', form=form)


