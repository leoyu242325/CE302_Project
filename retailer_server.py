import socket
import json
import mysql.connector

bind_ip = "0.0.0.0"
bind_port = 9999

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
            database="retailer"
        )
        mycursor = mydb.cursor()
        data = client.recv(1024)
        result = json.loads(data)

        print(result)

        if result[0] == "edit":
            b=result[1]
            c=result[2]
            a=result[3]
            aa= str(a)
            print('Delivery Information Changed: Tracking No ', aa)
            sql="UPDATE delivery_form SET delivery_price = %s, estimated_date = %s WHERE tracking_no = %s"
            val=(b,c,a,)
            mycursor.execute(sql, val)
            mydb.commit() 

        elif result[0] == "delete":

            print('Delivery Cancelled: Tracking No ',result[1])
            sql="DELETE FROM delivery_form WHERE order_item_no = %s"
            val= (result[2],)
            mycursor.execute(sql, val)
            mydb.commit()  

        mydb.close()
        result =""
        data =""
        break