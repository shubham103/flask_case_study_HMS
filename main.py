from flask import Flask,render_template,request,url_for,redirect,flash,session



app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

	if request.method=='GET':
		return render_template('login.html')

	else:
		session['userId']=12345
		return redirect(url_for('index'))


@app.route('/create_patient')
def createPatient():
	return render_template('createPatient.html')

@app.route('/update_patient')
def updatePatient():
	return render_template('updatePatient.html',flag=True,data={'a':1, 'bed_room':'singleRoom', 'date':'12-03-2020'})

@app.route('/delete_patient')
def deletePatient():
	return render_template('deletePatient.html', flag=True, data={'a':1})


@app.route('/view_all_patient')
def viewAllPatient():
	return render_template('viewAllPatients.html', flag=False, response=[{'a':1},{'a':1},{'a':1}])


@app.route('/view_patient')
def viewPatient():
	return render_template('searchForAPatient.html', flag=True, data={'a':1})

@app.route('/search_patient')
def searchPatient():
	return render_template('searchPatient.html', flag=True, data={'a':1})


@app.route('/issue_medicine')
def issueMedicine():
	return render_template('issueMedicines.html', flag=True, data={'a':1})

@app.route('/add_diagnostic')
def addDiagnostic():
	return render_template('addDiagnostic.html', flag=True, data={'a':1})

@app.route('/add_diagnostic2')
def addDiagnostic2():
	return render_template('addDiagnostic.html', flag=True, data={'a':1})

@app.route('/issue_medicine2')
def issueMedicine2():
	return render_template('issueMedicines.html', flag=True, data={'a':1})

@app.route('/billing')
def billing():
	return render_template('finalBilling.html', flag=True, data={'a':1})


@app.route('/get_patient_medicine_details')
def igetMedicine():
	return render_template('getPatientMedicineDetails.html', flag=True, data={'a':1})


@app.route('/get_patient_dignostic_details')
def igetdiagnostic():
	return render_template('getPatientDiagnosticDetails.html', flag=True, data={'a':1})
