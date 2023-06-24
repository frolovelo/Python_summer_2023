'''SQL в DataFrame и график Matplotlib'''
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password=input('Введите пароль: '),
    host='127.0.0.1',
    port=input('Введите порт: ')
)

cur = con.cursor()
cur.execute("""select * from book1""")
col = list(map(lambda x: x[0], cur.description))
val = cur.fetchall()
con.close()
df = pd.DataFrame(columns=col, data=val, index=[i for i in range(1, len(val)+1)])
print(df)

df['amount'].plot(grid=True, title="Количество")
plt.show()
df['price'].plot(grid=True, title="Цена")
plt.show()

