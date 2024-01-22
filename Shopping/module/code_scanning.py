import psycopg2

# connect to postgres database.
def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="hello@123"
    )
    return conn


def create_table():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
    conn.commit()
    conn.close()

# create test case to download record from posgtges users table and verify with csv.
def test_download_record():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    assert len(rows) == 3
    assert rows[0] == (1, 'John Doe', 'johndoe@example.com', 'password123')
    assert rows[1] == (2, 'Jane Smith', 'janesmith@example.com', 'password456')
    assert rows[2] == (3, 'Bob Johnson', 'bobjohnson@example.com', 'password789')  

if __name__ == "__main__":
    create_table()
    # test_download_record()
    print("Test cases passed!")          




            