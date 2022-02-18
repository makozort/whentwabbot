import sqlite3



conn = sqlite3.connect(f"./serverdata.db")  
cur = conn.cursor()



cur.execute("SELECT * FROM users;")
result = cur.fetchall()
print("Listing servers....")
total = 0
for x in result:
  servername = (str(x).strip("()'',"))
  print (servername)
  total += total                   # loop through all of one type of data
print (total)







