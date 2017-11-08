from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.args
      #return render_template("result.html",result = result)
      omar = ''
      for key, value in result.items():
      	omar += value + ' '
      return omar

@app.route('/hello/<name>')
def hello(name):
	return 'Hello {}'.format(name)

if __name__ == '__main__':
   app.run(debug = True)