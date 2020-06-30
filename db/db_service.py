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
        res2=cur.execute("""INSERT INTO patient(ssnid, name, age, admission_date, bed, address, city, state, status,fee) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (ssnid,name,age,datetime.today().strftime('%Y-%m-%d'), bed, address, city, state,status,fee))
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
        error_msg = "No Customer exist with %s ID" % ssnid
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



def isMedicineAvailable(mname,quantity):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from medicinemaster where med_name=%s", mname)
    res2 = cur.execute("SELECT qty from medicines where med_name=%s", mname)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        if res2 <= qty:
            return True
        else:
            return False
    else:
        return False
        
        
def issueMedicine(ssnid, mname, quantity):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM medicineissued where med_name=%s", mname)
    l=[]
    if res1 >= 1:
        """
        val = cur.fetchall()  # val is a tuple
        for k, v in val[0].items():
            if k == 'Balance':
                bal = v
                break
                """
        bal = cur.execute("SELECT qty FROM medicineissued where med_name=%s", mname)
        if bal>=int(quantity):
            cur.execute("Update medicineissued SET qty=qty-%s where med_name=%s", (int(quantity), mname))
            total_amount = cur.execute("SELECT amount FROM medicinemaster WHERE med_name=%s",mname)
            cur.execute("Update patient SET fee=%s*%s where ssnid=%s", (int(quantity), int(total_amount), ssnid))
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
    res1 = cur.execute("SELECT * FROM medicineissued where pat_id= %s", ssnid)
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
    res1 = cur.execute("SELECT * FROM medicinemaster where med_id=%s ",ssnid)
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
    res1 = cur.execute("SELECT * from diagnosticsmaster where test_name=%s", dname)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False
    

    
def addDiagnostics(ssnid, dname, amount):
    cur = mysql.connection.cursor()
    res3 = cur.execute("SELECT test_id from diagnostics where pat_id=%s", ssnid)
    if res3 >= 1:
        """
        msg = "Customer Successfully Updated"
        status = "Active"
        val = cur.fetchall()
        for k, v in val[0].items():
            if k == 'pat_id':
                cid = v
                break
        """
        res1 = cur.execute("INSERT INTO diagnosticsmaster SET test_name=%s, test_amount = %s where test_id=%s", (dname, damount, res3))
        mysql.connection.commit()
        res2 = cur.execute("Update patient SET fee = fee + %s where ssnid=%s", (cid, ssnid))
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
    res3 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
    if res3 >= 1:
        msg = "Customer Successfully Discharged"
        status = "Discharged"
        val = cur.fetchall()
        
        for k, v in val[0].items():
            if k == 'ssn':
                cid = v
                break
        res1 = cur.execute("Update patient SET status=%s where ssnid=%s", (status, ssnid))
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
    res3 = cur.execute("SELECT med_name from medicineissued where pat_id=%s",ssnid)
    val = cur.fetchall()
    
    for k, v in val[0].items():
            if k == 'pat_id':
                l.append('med_name')
    res1 = 0            
    for i in l:
        price= cur.execute("SELECT amount from medicinemaster where med_name = %s",i)
        qty_for_patient= cur.execute("SELECT qty from medicineissued where med_name = %s",i)
        res1 = qty_for_patient * price
    #res1 = cur.execute("SELECT SUM(fee) from patient where ssnid=%s", ssnid)
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
    res3 = cur.execute("SELECT test_id from diagnostics where pat_id=%s",ssnid)
    val = cur.fetchall()
    
    for k, v in val[0].items():
            if k == 'pat_id':
                l.append('test_id')
    res1 = 0            
    for i in l:
        price= cur.execute("SELECT test_amount from diagnosticsmaster where test_id = %s",i)
        
        res1 = res1 + price
    #res1 = cur.execute("SELECT SUM(fee) from patient where ssnid=%s", ssnid)
    if res1 >= 1:
        mysql.connection.commit()
        cur.close()
        return res1
    else:
        error_msg="Patient is not found"
        l.append(False)
        l.append(error_msg)
        return l
    
    
