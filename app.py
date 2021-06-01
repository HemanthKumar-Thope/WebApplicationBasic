from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ishouldwin!@#123'
app.config['MYSQL_DB'] = 'testDB'


mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success.html", methods=['POST'])
def success():
    if request.method == 'POST':
        details = request.form

        email = details['email_name']
        height = details['Height']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(email, height) VALUES (%s, %s)", (email, height))

        mysql.connection.commit()
        cur.close()

        return 'success'
        return render_template("success.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
