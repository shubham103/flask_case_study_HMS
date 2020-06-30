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
    res1 = cur.execute("SELECT * from patient where ws_ssn=%s", ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False
        
def createPatient(ssnid,name,age,admission_date, bed, address, city, state):
    cur = mysql.connection.cursor()
    l = []
    res1 = cur.execute("SELECT * from patient where ws_ssn=%s", ssnid)
    if res1 >= 1:
        mysql.connection.commit()
        cur.close()
        error_msg = "Patient already exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l
    else:
        cur.execute("""INSERT INTO patient(`ws_ssn`, `ws_pat_id`, `ws_pat_name`, `ws_age`, `ws_doj`, `ws_rtype`, `ws_adrs`, `ws_city`, `ws_state`, 'status') VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (ssnid,name,age,admission_date, bed, address, city, state, status))
        mysql.connection.commit()
        res2 = cur.execute("SELECT * from patient where ws_ssn=%s", ssnid)
        msg = "Customer Successfully Created"
        status = "Active"
        val = cur.fetchall()
        for k, v in val[0].items():
            if k == 'ws_pat_id':
                pid = v
                break
        res2 = cur.execute("""INSERT INTO patient(`ws_ssn`, `ws_pat_id`, `ws_pat_name`, `ws_age`, `ws_doj`, `ws_rtype`, `ws_adrs`, `ws_city`, `ws_state`, 'status') VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (ssnid, name,age,admission_date, bed, address, city, state, pid, status, datetime.today().strftime('%Y-%m-%d')))
        l.append(True)
        l.append("")
        mysql.connection.commit()
        cur.close()
        return l
        
        
def getPatientSsnidDetails(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from patient where ws_ssn=%s", ssnid)
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
    res1 = cur.execute("DELETE FROM patient where ws_ssn=%s", ssnid)
    status = "Deactivated"
    msg = "Customer Deleted"
    res2 = cur.execute("UPDATE patient SET status=%s WHERE ws_ssn=%s",(status, ssnid))
    
    mysql.connection.commit()
    cur.close()
    l=[]
    if res1 >= 1:
        l.append(True)
        l.append("")
        return l
    else:
        error_msg = "No Customer exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l     
        
        
def getPatientStatus(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM patient")
    res2 = cur.fetchall()
    res3 = cur.execute("SELECT status from patient where ws_ssn=%s",ssnid)
    mysql.connection.commit()
    cur.close()
    l = []
    if res1 >= 1:
        l.append(True)
        l.append(res2)
        l.append(res3)
        return l
    else:
        error_msg = "No Patient exist"
        l.append(False)
        l.append(error_msg)
        return l

def patient(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from patient where ws_ssn=%s", ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False  



def isMedicineAvailable(mname,quantity):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from medicinemaster where ws_med_name=%s", mname)
    res2 = cur.execute("SELECT ws_qty from medicines where ws_med_name=%s", mname)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        if res2 <= ws_qty:
            return True
        else:
            return False
    else:
        return False
        
        
def issueMedicine(ssnid, mname, quantity):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM medicineissued where ws_med_name=%s", mname)
    l=[]
    if res1 >= 1:
        """
        val = cur.fetchall()  # val is a tuple
        for k, v in val[0].items():
            if k == 'Balance':
                bal = v
                break
                """
        bal = cur.execute("SELECT ws_qty FROM medicineissued where ws_med_name=%s", mname)
        if bal>=int(quantity):
            cur.execute("Update medicineissued SET ws_qty=ws_qty-%s where ws_med_name=%s", (int(quantity), mname))
            total_amount = cur.execute("SELECT ws_amount FROM medicinemaster WHERE ws_med_name=%s",mname)
            cur.execute("Update patient SET fee=%s*%s where ws_ssn=%s", (int(quantity), int(total_amount), ssnid))
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
        error_msg = "No Customer exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l

def getPatientMedicinesDetails(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM medicineissued where ws_pat_id= %s", ssnid)
    l = []
    if res1 >= 1:
        res2 = cur.fetchall()
        mysql.connection.commit()
        l.append(True)
        l.append(res2)
        cur.close()
        return l
    else:
        error_msg = "No Customer exist"
        l.append(False)
        l.append(error_msg)
        cur.close()
        return l
    
    
 def getMedicinesDetails(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM medicinemaster where ws_med_id=%s ",ssnid)
    res2 = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    l = []
    if res1 >= 1:
        
        
        l.append(True)
        l.append(res2)
        
        return l
    else:
        error_msg = "No Medicine exist"
        l.append(False)
        l.append(error_msg)
        
        return l
    
    
def getDiagnosticsDetails():
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM diagnosticsmaster ")
    res2 = cur.fetchall()
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
    
    
def isDiagnosticsAvailable(dname,amount):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from diagnosticsmaster where ws_test_name=%s", dname)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False
    

    
def addDiagnostics(ssnid, dname, amount):
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT ws_test_id from diagnostics where ws_pat_id=%s", ssnid)
    if res3 >= 1:
        """
        msg = "Customer Successfully Updated"
        status = "Active"
        val = cur.fetchall()
        for k, v in val[0].items():
            if k == 'ws_pat_id':
                cid = v
                break
        """
        res1 = cur.execute("INSERT INTO diagnosticsmaster SET ws_test_name=%s, ws_test_amount = %s where ws_test_id=%s", (dname, damount, res3))
        mysql.connection.commit()
        res2 = cur.execute("Update patient SET fee = fee + %s where ws_ssn=%s", (cid, ssnid))
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

    
    
    
def dischargePatient(ssnid):
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT * from patient where ws_ssn=%s", ssnid)
    if res3 >= 1:
        msg = "Customer Successfully Discharged"
        status = "Discharged"
        val = cur.fetchall()
        
        for k, v in val[0].items():
            if k == 'ws_ssn':
                cid = v
                break
        res1 = cur.execute("Update patient SET status=%s where ws_ssn=%s", (status, ssnid))
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

    
def getSumOfPatientMedicinesDetails(ssnid):
    n=0
    l=[]
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT ws_med_name from medicineissued where ws_pat_id=%s",ssnid)
    val = cur.fetchall()
    
    for k, v in val[0].items():
            if k == 'ws_pat_id':
                l.append('ws_med_name')
    res1 = 0            
    for i in l:
        price= cur.execute("SELECT ws_amount from medicinemaster where ws_med_name = %s",i)
        qty_for_patient= cur.execute("SELECT ws_qty from medicineissued where ws_med_name = %s",i)
        res1 = qty_for_patient * price
    #res1 = cur.execute("SELECT SUM(fee) from patient where ws_ssn=%s", ssnid)
    if res1 >= 1:
        mysql.connection.commit()
        cur.close()
        return res1
    else:
        error_msg="Patient is not found"
        l.append(False)
        l.append(error_msg)
        return l
    
 
def getSumOfPatientDiagnosticsDetails(ssnid):
    n=0
    l=[]
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT ws_test_id from diagnostics where ws_pat_id=%s",ssnid)
    val = cur.fetchall()
    
    for k, v in val[0].items():
            if k == 'ws_pat_id':
                l.append('ws_test_id')
    res1 = 0            
    for i in l:
        price= cur.execute("SELECT ws_test_amount from diagnosticsmaster where ws_test_id = %s",i)
        
        res1 = res1 + price
    #res1 = cur.execute("SELECT SUM(fee) from patient where ws_ssn=%s", ssnid)
    if res1 >= 1:
        mysql.connection.commit()
        cur.close()
        return res1
    else:
        error_msg="Patient is not found"
        l.append(False)
        l.append(error_msg)
        return l
    
    
