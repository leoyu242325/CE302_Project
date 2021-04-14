import socket
import json
import mysql.connector

bind_ip = "0.0.0.0"
bind_port = 9998

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(1)

print "[*] Listening on %s:%d " % (bind_ip,bind_port)

while True:
    client,addr = server.accept()
    print 'Connected by ', addr

    while True:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="logistic"
        )
        mycursor = mydb.cursor()
        data = client.recv(1024)
        result = json.loads(data)

        if result[0] == "edit":
            a=result[1]
            b=result[2]
            c=result[3]
            d=result[4]
            e=result[5]
            f=result[6]
            g=result[7]
            h=result[8]
            aa= str(g)
            print('Order Information Changed: Order No ', aa)
            sql="UPDATE orders SET Name = %s, Phone_Number = %s, Email_Address = %s, Address = %s, Quantity = %s, Weight = %s WHERE order_item_no = %s"
            val=(a,b,c,d,e,f,h,)
            mycursor.execute(sql, val)
            mydb.commit() 

        elif result[0] == "delete":

            print('Order Cancelled: order No ',result[1])
            sql="DELETE FROM orders WHERE order_item_no = %s"
            val= (result[2],)
            mycursor.execute(sql, val)

            sql1="DELETE FROM delivery WHERE order_item_no = %s"
            val1= (result[2],)
            mycursor.execute(sql1, val1)
            mydb.commit()  

        mydb.close()
        result =""
        data =""
        break
