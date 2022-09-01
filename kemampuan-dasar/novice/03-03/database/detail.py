try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh", 
        user="postgres",
        password="postgres12345")

except Exception as e:
    print (e)

curs = conn.cursor()
query = f"select * from siswa where umur=22"
curs.execute(query)
data = curs.fetchone()
if not data:
    print ("gak ada")
else:
    print("nama:", data[0], "umur:", data[1])