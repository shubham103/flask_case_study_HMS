
from flask import Flask

#----------------------------------------------
#Database
# from flask_mysqldb import MySQL
# from datetime import datetime, date

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'hms'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# mysql = MySQL(app)

app.run(debug=True)
#---------------------------------------------


import routes


