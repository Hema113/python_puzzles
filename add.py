from flask import Flask,render_template,redirect,request,url_for
app = Flask(__name__)

@app.route('/')
def input_1():
    return render_template('addition1.html')

@app.route('/add', methods = ['POST'])
def user_input():
    input1 = int(request.form['first_input'])
    input2 = int(request.form['second_input'])
    input1 = input1 + input2
    return redirect(url_for('result_display',name = input1))

@app.route('/add/<name>')
def result_display(name):
    return "Result:{}".format(name)

if __name__ == "__main__":
    app.run()
