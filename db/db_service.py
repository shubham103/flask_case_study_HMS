from main import mysql
from datetime import datetime

def isUserExist(userId, password):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT username,password from userstore where username=%s and password=%s", (userId, password))
    mysql.connection.commit()
    cur.close()
    if res1 == 1:
        return True
    else:
        return False
        
def isPatientSsnidExist(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False
        
def createPatient(ssnid,name,age,admission_date, bed, address, city, state):
    cur = mysql.connection.cursor()
    l = []
    res1 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
    if res1 >= 1:
        mysql.connection.commit()
        cur.close()
        error_msg = "Patient already exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l
    else:
        fee=0
        status = "Active"
        res2=cur.execute("""INSERT INTO patient(ssnid, name, age, admission_date, bed, address, city, state, status,fee) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (ssnid,name,age,datetime.today().strftime('%d-%m-%Y'), bed, address, city, state,status,fee))
        mysql.connection.commit()
        cur.close()
        if res2>0:
            l.append(True)
            l.append("")
            return l
        else:
            l.append(False)
            l.append("Something went wrong")
            return l

def getPatientSsnidDetails(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
    if res1 >= 1:
        res2 = cur.fetchall() #res2 = ({'Customer_ID': 1, 'Account_ID': 10, 'Account_Type': 'S', 'Status': 'Activated', 'Message': 'login', 'Last_Updated': datetime.datetime(2020, 6, 13, 18, 43, 38)},)
        mysql.connection.commit()
        cur.close()
        return res2[0]
    else:
        mysql.connection.commit()
        cur.close()
        return False
        
        
def deletePatient(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("DELETE FROM patient where ssnid=%s", ssnid)
    print("###############################################################",res1)
    mysql.connection.commit()
    cur.close()
    l=[]
    if res1 >= 1:
        l.append(True)
        l.append("")
        return l
    else:
        error_msg = "No Patient exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l     
        
        
def getPatientStatus():
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM patient")
    res2 = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    l = []
    if res1 >= 1:
        l.append(True)
        l.append(res2)
        return l
    else:
        error_msg = "No Patient exist"
        l.append(False)
        l.append(error_msg)
        return l

def patient(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False

def issueMedicines(ssnid, mname, quantity):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM medicinemaster where mname=%s", (mname,))
    l=[]
    if res1 >= 1:
        """
        val = cur.fetchall()  # val is a tuple
        for k, v in val[0].items():
            if k == 'Balance':
                bal = v
                break
                """
        res2 = cur.execute("SELECT quantity,rate FROM medicinemaster where mname=%s", (mname,))
        val = cur.fetchall()
        avail= val[0]['quantity']
        rate = val[0]['rate']
        # for k,v in val[0].items():
        #     if k=='quantity':
        #         bal=v
        #     if k=='rate':
        #         rate=v
        if avail>=int(quantity):
            cur.execute("INSERT INTO medicineissued(ssnid,mname,quantity,rate) VALUES(%s,%s,%s,%s)",(ssnid,mname,quantity,int(quantity)*int(rate)))
            cur.execute("UPDATE medicinemaster SET quantity=quantity-%s where mname=%s", (int(quantity), mname,))
            #total_amount = cur.execute("SELECT rate FROM medicinemaster WHERE mname=%s",(mname,))
            mysql.connection.commit()
            cur.close()
            l.append(True)
            l.append("")
            return l
        else:
            mysql.connection.commit()
            cur.close()
            error_msg = "Insufficient Quantity"
            l.append(False)
            l.append(error_msg)
            return l
    else:
        mysql.connection.commit()
        cur.close()
        error_msg = "Medicine Not Available"
        l.append(False)
        l.append(error_msg)
        return l

def getPatientMedicineDetails(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM medicineissued where ssnid= %s", ssnid)
    l = []
    if res1 >= 1:
        res2 = cur.fetchall()
        mysql.connection.commit()
        l.append(True)
        l.append(res2)
        cur.close()
        return l
    else:
        error_msg = "No Patient exist"
        l.append(False)
        l.append([])
        cur.close()
        return l
    
    
def getMedicineDetails():
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM medicinemaster")
    res2 = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return res2
    else:
        return False
    
    
def getDiagnosticsDetails():
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM diagnosticsmaster")
    res2 = cur.fetchall()
    print("#############################################3",res2)
    mysql.connection.commit()
    cur.close()
    l = []
    if res1 >= 1:
        l.append(True)
        l.append(res2)
        return l
    else:
        error_msg = "No Diagnostics Details exist"
        l.append(False)
        l.append(error_msg)
        return l
    
    
def isDiagnosticsAvailable(dname):
    cur = mysql.connection.cursor()
    res1 = cur.execute("""SELECT * FROM diagnosticsmaster where dname=%s""",(dname,))
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False

def isMedicineAvailable(mname,quantity):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from medicinemaster where mname=%s",(mname,))
    res2 = cur.execute("SELECT quantity from medicinemaster where mname=%s",(mname,))
    res3 = cur.fetchall()
    for k,v in res3[0].items():
        if k=='quantity':
            bal=v
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        if int(bal) >= int(quantity):
            return True
        else:
            return False
    else:
        return False
    
def getPatientDiagnosticsDetails(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM diagnostics where ssnid= %s", ssnid)
    l = []
    if res1 >= 1:
        res2 = cur.fetchall()
        mysql.connection.commit()
        l.append(True)
        l.append(res2)
        cur.close()
        return l
    else:
        error_msg = "No Patient exist"
        l.append(False)
        l.append([])
        cur.close()
        return l
    
def addDiagnostic(ssnid, dname):
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT * from diagnosticsmaster where dname=%s", (dname,))
    if res3 >= 1:
        
        res2 = cur.execute("SELECT amount FROM diagnosticsmaster where dname=%s", (dname,))
        val = cur.fetchall()
        bal = val[0]['amount']
        # for k,v in bal:
        #     if k=='amount':
        #         amount=v

        res1 = cur.execute("INSERT INTO diagnostics(ssnid, dname, amount) VALUES (%s,%s,%s)", (ssnid, dname, bal))
        mysql.connection.commit()
        cur.close()
        l=[]
        if res1 >= 1:
            l.append(True)
            l.append("")
            return l
    else:
        error_msg = "No Diagnostics exist in the hospital"
        l.append(False)
        l.append(error_msg)
        return l

def dischargePatient(ssnid):
    l = []
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
    if res3 >= 1:
        status = "Discharged"
        res1 = cur.execute("Update patient SET status=%s where ssnid=%s", (status, ssnid))
        mysql.connection.commit()
        cur.close()
        if res1 >= 1:
            l.append(True)
            l.append("")
            return l
        else:
            error_msg="Patient not Upadated"
            l.append(False)
            l.append(error_msg)
            return l
    else:
        error_msg = "No Patient exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l

def getSumOfPatientMedicineDetails(ssnid):
    n=0
    l=[]
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT sum(rate) as rate from medicineissued where ssnid=%s",ssnid)
    val = cur.fetchall()
    if res3 >= 1:
        mysql.connection.commit()
        cur.close()
        return val
    else:
        error_msg="Patient is not found"
        l.append(False)
        l.append(error_msg)
        return l
    
 
def getSumOfPatientDiagnosticsDetails(ssnid):
    n=0
    l=[]
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT sum(amount) as amount from diagnostics where ssnid=%s",ssnid)
    val = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if res3>=1:
        return val
    else:
        error_msg="Patient is not found"
        l.append(False)
        l.append(error_msg)
        return l


def updatePatient(ssnid, name, age, admission_date, bed, address, city, state):
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
    if res3 >= 1:
        res1 = cur.execute("Update patient SET name=%s, age = %s, admission_date = %s, bed=%s, address=%s, city=%s, state=%s where ssnid=%s", (name, age, admission_date, bed, address, city, state, ssnid))
        mysql.connection.commit()
        cur.close()
        l=[]
        if res1 >= 1:
            l.append(True)
            l.append("")
            return l
    else:
        error_msg = "No Patient exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l 