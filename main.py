from flask import Flask, render_template, request
app = Flask(__name__)
import pypyodbc

@app.route('/')
def student():
   #return render_template('student.html')
   conn = pypyodbc.connect(
    			 r'DRIVER={ODBC Driver 11 for SQL Server};'
   				 r'SERVER=omarsgalal.database.windows.net;'
   				 r'DATABASE=WareHubDB;'
   				 r'UID=omarsgalal;'
   				 r'PWD=123456Omar'
    			 )
   return 'omar'

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      #return render_template("result.html",result = result)
      omar = dict(result)
      return str(omar['Age'][0])


@app.route('/hello/<name>')
def hello(name):
	return 'Hello {}'.format(name)

if __name__ == '__main__':
   app.run(debug = True)