from main import app
from flask import render_template, request, url_for, redirect, flash, session
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
            flash(" You need to login first.. ", 'red')
            return redirect(url_for("login"))

    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        userId = request.form['userId']
        password = request.form['password']

        if db.isUserExist(userId, password):

            session['userId'] = userId

            flash('success fully logged in.', 'green')
            return redirect(url_for('index'))

        else:

            flash('please enter correct Id or Password.. and try again !!', 'red')
            return redirect(url_for('login'))

    else:
        if 'userId' in session:
            return redirect(url_for('index'))
        return render_template('login.html')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
	session.clear()
	return redirect(url_for('index'))

#---------------------------------------------------------------------------------customer related

@app.route('/patient_registration', methods=['GET', 'POST'])
@login_required
def createPatient():
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
            flash("Patient already exist", 'red')
            return redirect(url_for("createPatient"))

        response = db.createPatient(ssnid, name, age, admission, bed, address, city, state)

        if response[0]:
            flash("Patient creation initiated successfully", 'green')
            return redirect(url_for("index"))
        else:
            flash(response[1], 'red')
            return redirect(url_for("createPatient"))


    elif request.method == 'GET':
        return render_template('createPatient.html')


@app.route('/pre_update_patient', methods=['GET', 'POST'])
@login_required
def preUpdatePatient():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']
            if db.isPatientSsnidExist(ssnid):
                patient_data = db.getPatientSsnidDetails(ssnid)
                return render_template("updatePatient.html", data=patient_data[0], flag=True)
            else:
                flash("Patient does not exist", 'red')
                return redirect(url_for('preUpdatePatient'))

    elif request.method == 'GET':
        return render_template('updatePatient.html', flag=False)


@app.route('/update_patient', methods=['POST'])
@login_required
def updatePatient():
    if request.method == 'POST':
        ssnid = request.form['ssnid']
        name = request.form['name']
        age = request.form['age']
        admission_date = request.form['admission']
        bed = request.form['bed']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']

        response = db.updatePatient(ssnid, name, age, admission_date, bed, address, city, state)

        if response[0]:
            flash("Patient updated successfully", 'green')
            return redirect(url_for("index"))
        else:
            flash(response[1], 'red')
            return redirect(url_for("preUpdatePatient"))


#Delete Patient
@app.route('/pre_delete_patient', methods=['GET', 'POST'])
@login_required
def preDeletePatient():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']
            if db.isPatientSsnidExist(ssnid):
                patient_data = db.getPatientSsnidDetails(ssnid)
                return render_template('deletePatient.html', data=patient_data[0], flag=True)
            else:
                flash("Patient does not exist", 'red')
                return redirect(url_for('preDeletePatient'))

    elif request.method == 'GET':
        return render_template('deletePatient.html', flag=False)


@app.route('/delete_patient', methods=['POST'])
@login_required
def deletePatient():
    if request.method == 'POST':

        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']

            response = db.deletePatient(ssnid)

            if response[0]:
                flash("Patient deleted successfully", 'green')
                return redirect(url_for("index"))
            else:
                flash(response[1], 'red')
                return redirect(url_for("preDeletePatient"))


#Patient Status
@app.route('/view_all_patients', methods=['GET'])
@login_required
def viewAllPatients():
	patient_data = db.getPatientStatus()
	if patient_data[0]:
		return render_template('viewAllPatients.html', data=patient_data[1])
	else:
		flash(patient_data[1],'red')
	return redirect(url_for('index'))


#patient details
@app.route('/search_patient', methods=['GET', 'POST'])
@login_required
def searchPatient():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']
            if db.isPatientSsnidExist(ssnid):
                patient_data = db.getPatientSsnidDetails(ssnid)
                return render_template('searchPatient.html', data=patient_data[0], flag=True)
            else:
                return redirect(url_for('searchPatient'))

    elif request.method == 'GET':
        return render_template('searchPatient.html', flag=False)

#--------------------------------------------------Pharmacy

@app.route('/get_patient_medicine_details', methods=['GET', 'POST'])
@login_required
def getPatientMedicineDetails():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']

            if db.isPatientSsnidExist(ssnid):
                responce1 = db.getPatientSsnidDetails(ssnid)     #Medicine quantity decrese and Patient_Medicine add row
                responce2 = db.getPatientMedicineDetails(ssnid)
                responce3 = db.getMedicineDetails()
                return render_template('getPatientMedicineDetails.html', data1=responce1, data2=responce2, data3=responce3,flag=True)

            else:
                flash("Patient doesnot exist", 'red')
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('getPatientMedicineDetails.html', flag=False)


@app.route('/issue_medicines', methods=['GET', 'POST'])
@login_required
def issueMedicines():
    ssnid = int(request.args.get('ssnid'))
    if request.method == 'POST':
        if 'mname' in request.form and 'quantity' in request.form:
            mname = request.form['mname']
            quantity = request.form['quantity']

            if db.isMedicineAvailable(mname, quantity):

                responce = db.issueMedicines(ssnid, mname, quantity) #Medicine quantity decrese and Patient_Medicine add row

            if responce[0]:
                flash("Successfully Assigned")
                return redirect(url_for('getPatientMedicineDetails'))
            else:
                flash(responce[1], 'red')
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('issueMedicines.html')

#---------------------------------------------------Diagnostics

@app.route('/get_patient_diagnostics_details', methods=['GET', 'POST'])
@login_required
def getPatientDiagnosticsDetails():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid = request.form['ssnid']

            if db.isPatientSsnidExist(ssnid):
                responce1 = db.getPatientSsnidDetails(ssnid)
                responce2 = db.getPatientDiagnosticsDetails(ssnid)
                responce3 = db.getDiagnosticsDetails()
                return render_template('getPatientDiagnosticsDetails.html', data1=responce1, data2=responce2, data3=responce3, flag=True)
            else:
                flash("Patient doesnot exist", 'red')
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('getPatientDiagnosticsDetails.html', flag=False)


@app.route('/add_diagnostic', methods=['GET', 'POST'])
@login_required
def addDiagnostic():
    ssnid = int(request.args.get('ssnid'))
    if request.method == 'POST':
        if 'mname' in request.form and 'quantity' in request.form:
            dname = request.form['mname']
            amount = request.form['amount']

            if not db.isDiagnosticsAvailable(dname, amount):
                responce = db.addDiagnostic(ssnid, dname, amount)

                if responce[0]:
                    flash("Successfully Assigned")
                    return redirect(url_for('getPatientDiagnosticsDetails'))
                else:
                    flash(responce[1], 'red')
                return redirect(url_for('index'))

            else:
                flash("Diagnostic already Available")
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('addDiagnostic.html')

#--------------------------------------------------------------Billing

@app.route('/final_billing', methods=['GET', 'POST'])
@login_required
def finalBilling():
    if request.method == 'POST':
        if 'ssnid' in request.form:
            ssnid=request.form['ssnid']

            if db.isPatientSsnidExist(ssnid):

                responce1 = db.getPatientSsnidDetails(ssnid)
                responce2 = db.getPatientMedicineDetails(ssnid)
                responce3 = db.getPatientDiagnosticsDetails(ssnid)
                responce4 = db.dischargePatient(ssnid)
                responce5 = db.getSumOfPatientMedicineDetails(ssnid)
                responce6 = db.getSumOfPatientDiagnosticsDetails(ssnid)

                for k, v in responce1.items():
                    if k == 'DOJ':
                        doj = v
                    if k == 'DOD':
                        dod = v
                    if k == 'Room_type':
                        roomType = v

                doj = datetime.strptime(doj, '%d-%m-%Y')
                dod = datetime.strptime(dod, '%d-%m-%Y')

                noOfDays = dod-doj

                if roomType == 'Single':
                    billforRoom = (noOfDays.days)*8000
                elif roomType == 'Semi':
                    billforRoom = (noOfDays.days)*4000
                else:
                    billforRoom = (noOfDays.days)*2000

                return render_template('finalBilling.html', data1=responce1, data2=responce2, data3=responce3, data4=noOfDays.days, data5=billforRoom, data6=responce5, data6=responce6, flag=True)

            else:
                flash("Patient does not exist")
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('finalBilling.html')
