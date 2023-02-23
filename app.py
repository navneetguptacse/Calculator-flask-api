from flask import Flask,render_template,request,jsonify
import math
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operations():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops=='add'):
            res = "The sum of {} and {} is = {}".format(num1,num2,(num1+num2))
        if(ops=='subtract'):
            res = "The subtraction of {} and {} is = {}".format(num1,num2,(num1-num2))
        if(ops=='multiply'):
            res = "The multiplication of {} and {} is = {}".format(num1,num2,(num1*num2))
        if(ops=='divide'):
            res = "The division of {} and {} is = {}".format(num1,num2,(num1/num2))
        if(ops=='log'):
            res = "The log of {} with base {} is = {}".format(num1,num2,round(math.log(num1,num2),4))
        if(ops=='mod'):
            res = "The modulo of {} mod {} is = {}".format(num1,num2,(num1 % num2))
        return render_template('results.html',result = res)

if __name__=="__main__":
    app.run(host="0.0.0.0")
