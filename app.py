from flask import Flask, render_template, request, flash

app = Flask(__name__) #create a class 
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("Quel est ton nom ?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    if request.method == 'POST':
        flash("Bonjour " + str(request.form['name_input']) + ", ravi de te voir !")
    return render_template("index.html")