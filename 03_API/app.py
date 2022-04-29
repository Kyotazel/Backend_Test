from flask import Flask, request, make_response, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "product_api"

mysql = MySQL(app)

@app.route("/api/products", methods=["POST", "GET"])
def products():
    try:
        myCursor = mysql.connection.cursor()
        if request.method == "POST":
            id = request.json["id"]
            name = request.json["name"]
            price = request.json["price"]
            quantity = request.json["quantity"]

            myCursor.execute("INSERT INTO products (id, name, price, quantity) VALUES (%s,%s,%s,%s)", (id, name, price, quantity))
            mysql.connection.commit()

            myCursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            row_header = [x[0] for x in myCursor.description]
            resutls = myCursor.fetchall()

            result_data = []
            for result in resutls:
                result_data.append(dict(zip(row_header, result)))

            data = {
                "code" : 200,
                "status" : "OK",
                "data" : result_data
            }
        if request.method == "GET":
            myCursor.execute("SELECT * FROM products")
            row_header = [x[0] for x in myCursor.description]
            results = myCursor.fetchall()

            result_data = []
            for result in results:
                result_data.append(dict(zip(row_header, result)))

            data = {
                "code" : 200,
                "status" : "OK",
                "data" : result_data
            }

    except Exception as e:
        return make_response(jsonify({"error" : str(e)}), 400)
    return make_response(jsonify(data), 200)
        

@app.route("/api/products/<id>", methods=["GET", "PUT", "DELETE"])
def products_id(id):
    try:
        myCursor = mysql.connection.cursor()
        if request.method == "GET":
            myCursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            row_header = [x[0] for x in myCursor.description]
            results = myCursor.fetchall()

            result_data = []
            for result in results:
                result_data.append(dict(zip(row_header, result)))

            data = {
                "code" : 200,
                "status" : "OK",
                "data" : result_data
            }
        if request.method == "PUT":

            name = request.json["name"]
            price = request.json["price"]
            quantity = request.json["quantity"]

            myCursor.execute("UPDATE products SET name = %s, price = %s, quantity = %s WHERE id = %s", (name,price,quantity,id))
            mysql.connection.commit()

            myCursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            row_header = [x[0] for x in myCursor.description]
            results = myCursor.fetchall()

            result_data = []
            for result in results:
                result_data.append(dict(zip(row_header, result)))

            data = {
                "code" : 200,
                "status" : "OK",
                "data" : result_data
            }
        if request.method == "DELETE":
            myCursor.execute("DELETE FROM products WHERE id = %s", (id,))
            mysql.connection.commit()

            data = {
                "code" : 200,
                "status" : "OK"
            }

    except Exception as e:
        return make_response(jsonify({"error" : str(e)}), 400)
    return make_response(jsonify(data), 200)

app.run(debug=True)