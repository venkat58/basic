from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/login' , methods = ['POST'])
def login():
    uname = request.form['uname']
    pwd = request.form['pass']
    if uname == 'venkat' and pwd == 'veeru':
        return 'welcome to application %s' %uname

@app.route('/login',methods = ['GET'])  
def get_login():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="venkat" and passwrd=="veeru":  
          return "Welcome %s" %uname  

@app.route('/')  
def message():  
      return render_template('login.html')  

if __name__ == "__main__":
    app.run() #debug = True

''' In the above application, we can also check the URL which also contains the data sent with the request to the server.
 This is an important difference between the GET requests and the POST requests as 
the data sent to the server is not shown in the URL on the browser in the POST requests.'''