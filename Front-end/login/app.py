from flask import Flask,render_template,request
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static') 
# app = Flask("login")
client = MongoClient("mongodb://127.0.0.1:27017")
db = client["login"]
collection = db["authentication"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/studentAdmin")
def studentAdmin():
    return render_template("studentAdmin.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/addDB", methods=["POST"])
def addDB():
    user = request.form.get("username")
    passwd = request.form.get("password")
    output=collection.find({"name": user},{"password": 1})
    collection.insert_one({"name": user, "password": passwd})
    return render_template("createdSuccessfully.html")

@app.route("/updateDB",methods=["POST"])
def updateDB():
    user = request.form.get("username")
    oldpasswd = request.form.get("oldpassword")
    passwd = request.form.get("password")
    output=collection.find({"name": user})
    for i in output: 
        output = i['password']
        userOutput = i["name"]
    if output == oldpasswd and user == userOutput:
        collection.find_one_and_update({"name": user},{'$set': {"password": passwd}})
        return render_template("updatesuccessful.html")
    else:
        return render_template("failupdate.html")




@app.route("/decision", methods=["POST"])
def decision():
    user = request.form.get("username")
    passwd = request.form.get("password")
    output=collection.find({"name": user},{"password": 1})
    for i in output: 
        output = i['password']
    if output == passwd:
        return render_template("success.html")
    else:
        return render_template("fail.html")
 

@app.route("/delete")
def remove():
    return render_template ("delete.html")

@app.route("/removeDB",methods=["POST"])
def removedb():
    user = request.form.get("username")
    passwd = request.form.get("password")
    output=collection.find({"name": user})
    for i in output: 
        output = i['password']
        userOutput = i['name']
    if output == passwd and user == userOutput:
        collection.delete_one({"name": user})
        return render_template("delsuccess.html")
    else:
        return render_template("fail.html")

@app.route("/query")
def query():
    return render_template ("query.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        return render_template('videostream.html')
    return render_template('query.html')

@app.route("/indexlogin")
def indexlogin():
    return render_template("indexlogin.html")

if __name__ == "__main__":
    app.run(debug=True)
# app.run(port=80,debug=True)