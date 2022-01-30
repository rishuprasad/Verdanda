from flask import Flask, render_template, send_file, request, Response, redirect
import json
import os
from uuid import uuid4

import pyodbc 
import pandas as pd

import json
# import psycopg2

from decimal import Decimal

server_details = """Driver={SQL Server};
                      Server=DESKTOP-CEMA4M6;
                      Database=PimcoDB;
                      Trusted_Connection=yes;"""

os.system("mkdir -p files")

app = Flask(__name__)

userId = 0
first_name = ""
last_name = ""



class fakefloat(float):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)

def defaultencode(o):
    if isinstance(o, Decimal):
        # Subclass float with custom repr?
        return fakefloat(o)
    raise TypeError(repr(o) + " is not JSON serializable")

def connect_db():
    connection = pyodbc.connect(server_details)
    return connection.cursor()

def query_db(query, args=(), one=False):
    cur = connect_db()
    cur.execute(query)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r


@app.route("/")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/growth")
def growth():
    return render_template("growth.html")

@app.route("/adjust")
def adjust():
    return render_template("adjust.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/saves_account", methods=["post"])
def new_stuff():
    # add functionality for making sure all spaces are filled

    print(int("123123"))
    print(type(request.form["emer_fund"]))

    emer_fund = (request.form["emer_fund"])
    retirement = (request.form["retirement"])
    trad_ira = (request.form["trad_ira"])
    roth_ira = (request.form["roth_ira"])
    savings = (request.form["savings"])
    stock_prof = (request.form["stock_prof"])

    password = (request.form["password"])
    last_name = (request.form["last_name"])
    first_name = (request.form["first_name"])
    email = (request.form["email"])

    # # stuff.append(num)

    print(emer_fund)

    insert_user_users = """
        INSERT INTO PimcoDB.dbo.tbl_users 
        (user_id, emer_fund, retirement, trad_ira, roth_ira, stock_prof, savings) 
        VALUES 
        (?, ?, ?, ?, ?, ?, ?)
        """

    # how can you make sure each person is distinct

    insert_user_names = """
        INSERT INTO PimcoDB.dbo.tbl_names 
        (first_name, last_name, email, password) 
        VALUES 
        (?, ?, ?, ?)
        """

    select_user_id = """
        select USER_ID from PimcoDB.dbo.tbl_names
        where first_name='{}' and last_name='{}'
        """

    select_user = """
        SELECT * FROM PimcoDB.dbo.tbl_users
        WHERE user_id = {}
    """

    cursor = connect_db()
    cursor.execute(insert_user_names, (first_name, last_name, email, password))
    cursor.execute(select_user_id.format(first_name, last_name))
    user_id = cursor.fetchone()[0]
    # print(type(user_id[0]))
    print("----------------")
    # for i in user_id:
    #     print(i)
    # print(user_id[0])
    print("----------------")
    
    cursor.commit()
    cursor.connection.close()


    cursor = connect_db()
    cursor.execute(insert_user_users, (user_id, emer_fund, retirement, trad_ira, roth_ira, savings, stock_prof))
    cursor.commit()
    cursor.connection.close()


    num = 34
    my_query = query_db(select_user.format(user_id), args=(), one=True)
    
    
    print(my_query)
    json_output = json.dumps(my_query, default=defaultencode)
    print(type(json_output))

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(my_query, f, ensure_ascii=False, indent=4, default=defaultencode)

    return redirect("/dashboard", code=302)

@app.route("/adjust_account", methods=["post"])
def adjust_stuff():
    # add functionality for making sure all spaces are filled

    print(int("123123"))
    print(type(request.form["emer_fund"]))

    emer_fund = (request.form["emer_fund"])
    retirement = (request.form["retirement"])
    trad_ira = (request.form["trad_ira"])
    roth_ira = (request.form["roth_ira"])
    savings = (request.form["savings"])
    stock_prof = (request.form["stock_prof"])

    # # stuff.append(num)

    print(emer_fund)

    insert_user_users = """
        INSERT INTO PimcoDB.dbo.tbl_users 
        (user_id, emer_fund, retirement, trad_ira, roth_ira, stock_prof, savings) 
        VALUES 
        (?, ?, ?, ?, ?, ?, ?)
        """

    # how can you make sure each person is distinct

    delete_user = """
        DELETE FROM PimcoDB.dbo.tbl_users 
        WHERE user_id = {}
        """

    select_user_id = """
        select USER_ID from PimcoDB.dbo.tbl_names
        where first_name='{}' and last_name='{}'
        """

    select_user = """
        SELECT * FROM PimcoDB.dbo.tbl_users
        WHERE user_id = {}
    """

    cursor = connect_db()
    cursor.execute(delete_user.format(user_id))    
    cursor.commit()
    cursor.connection.close()


    cursor = connect_db()
    cursor.execute(insert_user_users, (user_id, emer_fund, retirement, trad_ira, roth_ira, savings, stock_prof))
    cursor.commit()
    cursor.connection.close()


    num = 34
    my_query = query_db(select_user.format(user_id), args=(), one=True)
    
    
    print(my_query)
    json_output = json.dumps(my_query, default=defaultencode)
    print(type(json_output))

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(my_query, f, ensure_ascii=False, indent=4, default=defaultencode)

    return redirect("/dashboard", code=302)


@app.route("/update_table", methods=["post"])
def update_table():
    # MethodInfo WritableMethod
    # MethodInfo ReadOnlyMethod
    # Flags = BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static

    # WritableMethod = Request.Form.GetType().GetMethod("MakeReadWrite", Flags)
    # ReadOnlyMethod = Request.Form.GetType().GetMethod("MakeReadOnly", Flags)

    # FormField = Request.GetType().GetField("_form", Flags)

    # WritableMethod.Invoke(Request.Form, null)

    # Request.Form["emer_fund"] = "100"
    # Response.form["emer_fund"] = 100000
    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(port=5000)