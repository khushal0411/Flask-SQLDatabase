import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
# create a connection
conn = sqlite3.connect('data1.db',check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS marks (name varchar(20), maths number(3),sci number(3));")


@app.route('/')
def home():
    return "Hello"

@app.route("/add", methods=['POST'])
def predict():
    conn = sqlite3.connect('data1.db', check_same_thread=False)
    #conn.row_factory = sqlite3.Row
    c = conn.cursor()
    name = request.form.get("name")
    maths = request.form.get("maths")
    sci = request.form.get("sci")
    List = [(name,maths,sci)]
    c.executemany("INSERT INTO marks VALUES (?, ?, ?)", List)
    c.execute("SELECT * FROM marks")
    columns = [column[0] for column in c.description]
    result=[]
    for row in c.fetchall():
        result.append(dict(zip(columns,row)))
    conn.commit()
    conn.close()
    return json.dumps(result)
@app.route("/delete", methods=['POST'])
def delete():
    conn = sqlite3.connect('data1.db', check_same_thread=False)
    #conn.row_factory = sqlite3.Row
    c = conn.cursor()
    name = request.form.get("name")
    maths = request.form.get("maths")
    sci = request.form.get("sci")
    List = [(name,maths,sci)]
    c.execute("DELETE FROM marks WHERE name=?",[name])
    c.execute("SELECT * FROM marks")
    columns = [column[0] for column in c.description]
    result=[]
    for row in c.fetchall():
        result.append(dict(zip(columns,row)))
    conn.commit()
    conn.close()
    return json.dumps(result)
@app.route("/update", methods=['POST'])
def update():
    conn = sqlite3.connect('data1.db', check_same_thread=False)
    #conn.row_factory = sqlite3.Row
    c = conn.cursor()
    name = request.form.get("name")
    maths = request.form.get("maths")
    sci = request.form.get("sci")
    List = [(name,maths,sci)]
    c.execute("UPDATE marks set maths=? WHERE name=?",[maths,name])
    c.execute("SELECT * FROM marks")
    columns = [column[0] for column in c.description]
    result=[]
    for row in c.fetchall():
        result.append(dict(zip(columns,row)))
    conn.commit()
    conn.close()
    return json.dumps(result)
customers_sql = """
      CREATE TABLE IF NOT EXISTS customers (
      id integer PRIMARY KEY,
      first_name text NOT NULL,
      last_name text NOT NULL)"""


if __name__ == "__main__":
    app.run(debug=True)