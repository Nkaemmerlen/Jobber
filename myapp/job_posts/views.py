from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import JobPost
from myapp.job_posts.forms import JobPostForm

job_posts = Blueprint('job_posts', __name__)