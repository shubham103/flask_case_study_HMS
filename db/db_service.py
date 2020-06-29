from main import mysql
from datetime import datetime

def isUserExist(userId,password):
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
    res1 = cur.execute("SELECT * from patient where SSN_ID=%s", ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False
        
def createPatient(ssnid,name,age,admission_date, bed, address, city, state):
    cur = mysql.connection.cursor()
    l = []
    res1 = cur.execute("SELECT * from patient where SSN_ID=%s", ssnid)
    if res1 >= 1:
        mysql.connection.commit()
        cur.close()
        error_msg = "Patient already exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l
    else:
        cur.execute("""INSERT INTO patient(ssnid,name,age,admission_date, bed, address, city, state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""", (ssnid,name,age,admission_date, bed, address, city, state))
        mysql.connection.commit()
        res2 = cur.execute("SELECT * from patient where ssnid=%s", ssnid)
        msg = "Customer Successfully Created"
        status = "Active"
        val = cur.fetchall()
        for k, v in val[0].items():
            if k == 'patient_id':
                pid = v
                break
        res2 = cur.execute("""INSERT INTO getPatientStatus(ssnid,name,age,admission_date, bed, address, city, state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (ssnid, name,age,admission_date, bed, address, city, state, pid, status, datetime.today().strftime('%Y-%m-%d')))
        l.append(True)
        l.append("")
        mysql.connection.commit()
        cur.close()
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
    status = "Deactivated"
    msg = "Customer Deleted"
    res2 = cur.execute("UPDATE patientstatus SET Status=%s WHERE ssnid=%s",(status, ssnid))
    
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
    res1 = cur.execute("SELECT * FROM patientstatus")
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
    res1 = cur.execute("SELECT * from patient where patient_id=%s", ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 >= 1:
        return True
    else:
        return False  



def isMedicineAvailable(mname,quantity):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from medicines where ws_med_name=%s", mname)
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
        
        

    
