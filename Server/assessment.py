import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from Model.DataFrames import Applicant_Data

bp = Blueprint('assess', __name__, url_prefix='/assess')


@bp.route('/register', methods=('GET', 'POST'))
def assess_reg():
    if request.method == 'POST':
        notice = None
        custom_id = request.form['custom_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        lgi = Applicant_Data.lifeguard_instructor(custom_id)
        existing_email = Applicant_Data.search_by_email(email)
        if not lgi:
            notice = ''
            flash(notice)
            return render_template('assess/new_hire_reg.html', notice='Custom_ID is not registered as an LGI')
        if existing_email:
            notice = ''
            flash(notice)
            return render_template('assess/new_hire_reg.html', error='Email Address is already registered')

        if not first_name:
            notice = 'First name is required'
        elif not last_name:
            notice = 'Last name is required'
        elif not email:
            notice = 'Email is required'

        if notice is None:
            notice = ''
            flash(notice)
            Applicant_Data.new_applicant(first_name, last_name, email)
            return render_template('assess/new_hire_reg.htm',
                                   notice=first_name + ' ' + last_name + ' has been successfully registered')

        else:
            flash(notice)

    return render_template('assess/new_hire_reg.html')


@bp.route('/section_one', methods=('GET', 'POST'))
def section_one():
    if request.method == 'POST':
        notice = None
        custom_id = request.form['sec1_custom_id']
        points = request.form['sec1_points']
        first_name = request.form['sec1_first_name']
        last_name = request.form['last_name']

        if 0 > points > 15:
            notice = ''
            flash(notice)
            return render_template('assess/section_one.html', notice='Points must range from 0 to 15.')

        if Applicant_Data.no_custom_id(custom_id):
            notice = ''
            flash(notice)
            return render_template('assess/section_one.html', notice='Custom_ID does not exist.')
        elif Applicant_Data.match(custom_id, first_name, last_name):
            notice = ''
            flash(notice)
            return render_template('assess/section_one.html', notice='Custom_ID does not match existing credentials.')
        else:
            flash(notice)
            Applicant_Data.sectionOne(custom_id, points)
            return render_template('assess/section_one.html', notice='Points added to ' + first_name)
