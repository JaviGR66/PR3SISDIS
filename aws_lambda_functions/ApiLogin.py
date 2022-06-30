import sys
import logging
import pymysql
import json
import pymysql.cursors
import boto3


rds_host="database-1-mariadb.cyuon3k4skgo.us-east-1.rds.amazonaws.com"

username="admin"
password="12345678"
dbname="database-1-mariadb"
dbport= 3306

try:
    conn= pymysql.connect (rds_host,user=username, passwd=password, port=dbport,database=dbname,connect_timeout=10)

except pymysql.MySQLError as e:
    print (e)
    sys.exit()


    #Funcion que nos sirve para poder hacer el registro y para crear el login
def lambda_handler(event, context):
    Usuario=(event["queryStringParameters"]["Usuario"])
    Contrasenia=(event["queryStringParameters"]["Contrasenia"])
    op=(event["queryStringParameters"]["op"])

    if op == "login":
        with conn.cursor() as cur:
            cur.execute("Select Estado from Usuarios where Usuario='"+Usuario+"' AND Contrasenia='"+Contrasenia+"'")
            conn.commit()
            row_count=cur.rowcount
            #contador=0
            if not row_count:
                return{
                'statusCode':200,
                'headers':{'Access-Control-Allow-Origin':'*'},
                'body':json.dumps({'accesoConcedido':'false'})
                    }
            else:
                return{
                'statusCode':200,
                'headers':{'Access-Control-Allow-Origin':'*'},
                'body':json.dumps({'accesoConcedido':'true'})
                }
    else:
        FraseRecuperacion=(event["queryStringParameters"]["FraseRecuperacion"])
        Nombre=(event["queryStringParameters"]["Nombre"])
        Apellido1=(event["queryStringParameters"]["Apellido1"])
        Apellido2=(event["queryStringParameters"]["Apellido2"])
        Correo=(event["queryStringParameters"]["Correo"])
        with conn.cursor() as cur:
            cur.execute("Select Usuario from Usuarios where Usuario='"+Usuario+"'")
            conn.commit()

            row_count=cur.rowcount
            if not row_count:
                query= "insert into Usuarios Values('"+Usuario+"','"+Contrasenia+"','"+Nombre+"','"+Apellido1+"','"+Apellido2+"','"+Correo+"','"+FraseRecuperacion+"',0);"
                cur.execute(query)
                conn.commit()
                s3 = boto3.resource("s3")
                s3.Bucket("practica4-javgr-javicelma").put_object(Key=Usuario+"/sample.txt", Body="hi")
                return{
                    'statusCode':200,
                    'headers':{'Access-Control-Allow-Origin':'*'},
                    'body':json.dumps({'Registro':'true'})
                }
            else:
                return{
                    'statusCode':200,
                    'headers':{'Access-Control-Allow-Origin':'*'},
                    'body':json.dumps({'Registro':'false'})
                }
            
           



  
