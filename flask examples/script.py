from flask import Flask, redirect , url_for

app = Flask(__name__) #creating the Flask class object  

''' url binding example'''

@app.route('/home/<name>/<int:age>') #decorator drfines the   
def home(name, age):
    return f"hello, this is our first flask website <h1>{name} </h1>" ;  

@app.route('/user/<name>')
def user(name):
    if name== 'student':
        return redirect(url_for('student'))
    elif name== 'admin':
        return redirect(url_for('admin'))
    elif name== 'teacher':
        return redirect(url_for('teacher'))
    else :
        return 'unknown'

@app.route('/student')
def student():
    return 'loogied in user is student'

@app.route('/admin')
def admin():
    return 'loogied in user is admin'

@app.route('/teacher')
def teacher():
    return 'loogied in user is teacher'

if __name__ =='__main__':  
    app.run()  