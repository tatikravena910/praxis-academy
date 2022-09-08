from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="project", 
        user="postgres",
        password="postgres12345"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        umur = request.form.get("umur")
        asal = request.form.get("asal")
        pendidikan = request.form.get("pendidikan")
        query = f"insert into datasantri(nama, umur, asal, pendidikan) values('{nama}', '{umur}', '{asal}', '{pendidikan}')" 
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from datasantri"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

@app.route("/delete/<datasantri_id>")
def delete(datasantri_id):
    conn = psycopg2.connect(
        host="localhost",
        database="project",
        user="postgres",
        password="postgres12345"
    )
    curs = conn.cursor()
    query = f"delete from datasantri where id = {datasantri_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")



if __name__ == "__main__":
    app.run()

