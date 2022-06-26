from flask import Flask,request,redirect,render_template,flash
from mysqlconnection import connectToMySQL
app=Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('report_card')	 
    query="SELECT * FROM students;"
    result=mysql.query_db(query)
    print(result)
    return render_template("students.html",students=result)

@app.route("/<int:id>")
def card(id):
    mysql = connectToMySQL('report_card')	 
    query0="select * from students where students.id=%(id1)s;"
    data0={
        "id1":int(id),
    }

    result0=mysql.query_db(query0,data0)
    print(result0)
    mysql = connectToMySQL('report_card')	
    query="SELECT * FROM grades JOIN students on students.id=grades.students_id WHERE students.id=%(id)s;"
    data={
        "id":int(id),
    }
    result=mysql.query_db(query,data)
    
    return render_template("card.html",student=result0[0],grades=result)

@app.route("/edit/<id>",methods=["GET","POST"])
def add(id):
    if request.method=="GET":
        return render_template("addgrade.html",id=id)
    mysql = connectToMySQL('report_card')	 
    query="insert into grades (course,mark,date,comment,students_id) values(%(course)s,%(mark)s,%(date)s,%(comment)s,%(id)s);"
    data={
        "course":request.form["course"],
        "mark":request.form["mark"],
        "date":request.form["date"],
        "comment":request.form["comment"],
        "id":id
    }
    result=mysql.query_db(query,data)
    return redirect("/")
    
if __name__==("__main__"):
    app.run(debug=True)