import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('''
        create table if not exists users (
            id integer primary key,
            name text,age integer, city text
        )
''')
cur.execute("insert into users (name, age, city) values ('Alice', 30, 'New York')")
cur.execute("insert into users (name, age, city) values ('Bob', 25, 'Los Angeles')")
cur.execute("insert into users (name, age, city) values ('Charlie', 35, 'Chicago')")
conn.commit()
print("Data inserted successfully.")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, City: {row[3]}")
conn.close()