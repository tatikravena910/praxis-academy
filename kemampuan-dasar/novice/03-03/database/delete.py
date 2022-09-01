try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh", 
        user="postgres",
        password="postgres12345")

    curs = conn.cursor()
    
    nama = "anggang"
    query = f"delete from siswa where nama='{nama}'"

    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception as e:
    print (e)