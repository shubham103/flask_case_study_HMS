from main import app, LoginForm, RegistrationForm, CreateAccountForm, DepositForm, TransferForm, StatementDateForm, \
    StatementNumberForm
from flask import render_template, request, url_for, redirect, flash, session
import os
import json
from functools import wraps
from db import db_service as db
from datetime import datetime

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------------------------------------ login & logout

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'userId' in session:
            return f(*args, **kwargs)
        else:
            flash(" You need to login first.. ", 'danger')
            return redirect(url_for("login"))

    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        userId = request.form['userId']
        password = request.form['password']

        if db.isUserExist(userId, password):

            session['userId'] = userId

            flash('success fully logged in.', 'success')
            return redirect(url_for('index'))

        else:

            flash('please enter correct Id or Password.. and try again !!', 'danger')
            return redirect(url_for('login'))

    else:
        if 'userId' in session:
            return redirect(url_for('index'))

        form = LoginForm()
        return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
	session.clear()
	return redirect(url_for('index'))

#---------------------------------------------------------------------------------customer related

@app.route('/patient_registration', methods=['GET', 'POST'])
@login_required
def patientRegistration():
    if request.method == 'POST':
        ssnid = request.form['ssnid']
        name = request.form['name']
        age = request.form['age']
        admission = request.form['admission']
        bed = request.form['bed']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']

        if db.isPatientSsnidExist(ssnid):
            flash("Patient already exist", 'danger')
            return redirect(url_for("patientRegistration"))

        response = db.patientRegistration(ssnid, name, age, admission, bed, address, city, state)

        if response[0]:
            flash("Patient creation initiated successfully", 'success')
            return redirect(url_for("index"))
        else:
            flash(response[1], 'danger')
            return redirect(url_for("patientRegistration"))


    elif request.method == 'GET':
        form = RegistrationForm()
        return render_template('patientRegistration.html', form=form)


@app.route('/pre_update_patient', methods=['GET', 'POST'])
@login_required
def preUpdatePatient():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']
            if db.isPatientSsnidExist(ssnid):
                patient_data = db.getPatientSsnidDetails(ssnid)
                form = RegistrationForm()
                return render_template("updatePatient.html", pd=patient_data[0], form=form)
            else:
                flash("Patient does not exist", 'danger')
                return redirect(url_for('preUpdatePatient'))

    elif request.method == 'GET':
        return render_template('preUpdatePatient.html')


@app.route('/update_patient', methods=['POST', 'GET'])
@login_required
def updatePatient():
    if request.method == 'POST':
        ssnid = request.form['ssnid']
        name = request.form['name']
        age = request.form['age']
        admission = request.form['admission']
        bed = request.form['bed']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']

        # customerOldData = db.getCustomerSsnidDetils(ssnid)
        # paste the old data in value parameter of form inputs and  make these fields as mandatory in form
        # accountant should update the input field or let the old data written.

        response = db.updatePatient(ssnid, name, age, admission, bed, address, city, state)

        if response[0]:
            flash("Patient updated successfully", 'success')
            return redirect(url_for("index"))
        else:
            flash(response[1], 'danger')
            return redirect(url_for("preUpdatePatient"))
    else:

        return render_template('updatePatient.html')


#Delete Patient
@app.route('/pre_delete_patient', methods=['GET', 'POST'])
@login_required
def preDeletePatient():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']
            if db.isPatientSsnidExist(ssnid):
                patient_data = db.getPatientSsnidDetails(ssnid)
                return render_template('deletePatient.html', pd=patient_data[0])
            else:
                return redirect(url_for('preDeletePatient'))

    elif request.method == 'GET':
        return render_template('preDeletePatient.html')


@app.route('/delete_patient', methods=['POST'])
@login_required
def deletePatient():
    if request.method == 'POST':

        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']

            response = db.deletePatient(ssnid)

            if response[0]:
                flash("Patient deleted successfully", 'success')
                return redirect(url_for("index"))
            else:
                flash(response[1], 'danger')
                return redirect(url_for("preDeletePatient"))


#Patient Status
@app.route('/patient_details', methods=['GET'])
@login_required
def patientDetails():
	patient_data = db.getPatientStatus()
	if patient_data[0]:
		return render_template('patientStatus.html', patientData=patient_data[1])
	else:
		flash(patient_data[1],'danger')
	return redirect(url_for('index'))


#patient details
@app.route('/pre_patient', methods=['GET', 'POST'])
@login_required
def prePatient():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']
            if db.isPatientSsnidExist(ssnid):
                patient_data = db.getPatientSsnidDetails(ssnid)
                return render_template('Patient.html', pd=patient_data[0])
            else:
                return redirect(url_for('prePatient'))

    elif request.method == 'GET':
        return render_template('prePatient.html')


@app.route('/patient', methods=['GET', 'POST'])
@login_required
def patient():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']

            patient_data = patient(ssnid)

            if patient_data[0]:
                return render_template('patient.html', patient_Data=patient_data[1])
            else:
                flash(patient_data[1], 'danger')
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('preDeletePatient.html')


