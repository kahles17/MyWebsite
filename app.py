from json import dumps
from flask import Flask,render_template,request
from sympy import symbols,Symbol,latex
def add_to_output(latex,index,output):
    output[str(index)]=latex
def sympy_calc(output):
    Untc,R10k,Rntc,Uref,Uadc= symbols("U_{NTC},R_{10k},R_{NTC},U_{ref},U_{ADC}")
    dUadc = Symbol("\Delta U_{ADC}")
    dRntc = Symbol("\Delta U_{NTC}")
    dUref = Symbol("\Delta U_{ref}")
    dR10k = Symbol("\Delta R_{10k}")
    add_to_output(latex(Rntc),0,output)
    add_to_output(latex(dUref),1,output)
    add_to_output(latex(dR10k),2,output)
def calc(a,b,c):
    output = {}
    sympy_calc(output)
    return dumps(output)
app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")
@app.route("/api/")
def calculation():
    a = int(request.args.get("A"))
    b = int(request.args.get("B"))
    c = int(request.args.get("C"))
    tex = calc(a,b,c)
    return tex
if __name__ == "__main__":
    app.run()