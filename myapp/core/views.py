# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import JobPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
  page = request.args.get('page', 1, type=int)
  job_posts = JobPost.query.order_by(JobPost.date.desc()).paginate(page=page, per_page=20)
  return render_template('index.html', job_posts=job_posts)

@core.route('/info')
def info():
  return render_template('info.html')