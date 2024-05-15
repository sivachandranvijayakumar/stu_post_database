from flask import Flask, request, render_template,jsonify,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key="siva123@"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Siva1234@'
app.config['MYSQL_DB'] = 'stu_project_postman'

mysql=MySQL(app)


@app.route("/",methods=["GET","POST"])
def read():
    cur=mysql.connection.cursor()
    cur.execute("select * from detail")
    data=cur.fetchall()
    cur.close()
    return render_template("index.html",data=data)

@app.route("/post/",methods=["GET","POST"])
def add():
    if request.method=="POST":

        data=request.get_json()
        name=data["name"]
        age=data["age"]
        roll_no=data["roll_no"]
        mark1=data["mark1"]
        mark2=data["mark2"]
        mark3=data["mark3"]
        mark4=data["mark4"]
        mark5=data["mark5"]

        cur=mysql.connection.cursor()
        cur.execute("insert into detail (name,age,roll_no,mark1,mark2,mark3,mark4,mark5) values (%s,%s,%s,%s,%s,%s,%s,%s)",(name, age, roll_no, mark1, mark2, mark3, mark4, mark5))
        cur.connection.commit()
        cur.close()
        return redirect(url_for('read'))

@app.route("/put/<int:id>",methods=["PUT"])
def put(id):
    data=request.get_json()
    name=data["name"]
    age=data["age"]
    roll_no=data["roll_no"]
    mark1=data["mark1"]
    mark2=data["mark2"]
    mark3=data["mark3"]
    mark4=data["mark4"]
    mark5=data["mark5"]

    cur=mysql.connection.cursor()
    cur.execute("update detail set name=%s,age=%s,roll_no=%s,mark1=%s,mark2=%s,mark3=%s,mark4=%s,mark5=%s where id=%s",(name, age, roll_no, mark1, mark2, mark3, mark4, mark5,id))
    cur.connection.commit()
    cur.close()
    
    return jsonify({"message": "updated successfully"})


@app.route("/patch/<int:id>",methods=["PATCH"])
def patch(id):
    data=request.get_json()
    name=data["name"]
    age=data["age"]
    roll_no=data["roll_no"]
    mark1=data["mark1"]
    mark2=data["mark2"]
    mark3=data["mark3"]
    mark4=data["mark4"]
    mark5=data["mark5"]

    cur=mysql.connection.cursor()
    cur.execute("update detail set name=%s,age=%s,roll_no=%s,mark1=%s,mark2=%s,mark3=%s,mark4=%s,mark5=%s where id=%s",(name, age, roll_no, mark1, mark2, mark3, mark4, mark5,id))
    cur.connection.commit()
    cur.close()
    
    return jsonify({"message": "updated successfully"})

@app.route("/delete/<int:id>",methods=["DELETE"])
def delete(id):
    cur=mysql.connection.cursor()
    cur.execute("delete from detail where id=%s",(id,))
    cur.connection.commit()
    cur.close()

    return jsonify({"message": "Deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)