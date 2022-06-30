import sys
import logging
import pymysql
import json
import pymysql.cursors
import boto3
import collections
from datetime import datetime
import time

rds_host="database-1-mariadb.cyuon3k4skgo.us-east-1.rds.amazonaws.com"

username="admin"
password="12345678"
dbname="database-1-mariadb"
dbport= 3306

try:
    conn= pymysql.connect (rds_host,user=username, passwd=password, db=dbname, port= dbport, connect_timeout=5)

except pymysql.MySQLError as e:
    print (e)
    sys.exit()

def consultas(vid,tag,usuario):
    with conn.cursor() as cur:
        consulta="Select * from Videos WHERE "
        if vid:
            consulta +="Vidname='"+vid+"' and "
        if tag:
            consulta +="Tag='"+tag+"' and "
        if usuario:
            consulta +="Usuario='"+usuario+"' and "
        if not tag and not vid and not usuario:
            consulta += "1 LIMIT 10;"
        else:
            consulta+= "1;"
        cur.execute(consulta)
        rows = cur.fetchall()
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['Usuario'] = row[0]
            d['Tag'] = row[1]
            d['Vidname'] = row[2]
            d['Size'] = row[3]
            d['Ruta'] = row[4]
            d['FechaSubido'] = row[5].strftime("%Y %m %d")
            d['Extension'] = row[6]
            objects_list.append(d)
        return objects_list
    

def lambda_handler(event , context):
    op=(event["queryStringParameters"]["op"])
    if op == "get":
        user=(event["queryStringParameters"]["Usuario"])
        tag=(event["queryStringParameters"]["Tag"])
        videoName=(event["queryStringParameters"]["Vidname"])
        objects_list=[]
        objects_list= consultas(videoName,tag,user)
        return{
            'statusCode':200,
            'headers':{'Access-Control-Allow-Origin':'*'},
            'body':json.dumps(objects_list)
            }
    elif op== "post":
        import datetime
        user=(event["queryStringParameters"]["Usuario"])
        tag=(event["queryStringParameters"]["Tag"])
        vidname=(event["queryStringParameters"]["Vidname"])
        size=(event["queryStringParameters"]["Size"])
        extension=(event["queryStringParameters"]["Extension"])
        fechaSubido= datetime.datetime.now()

        with conn.cursor() as cur:
            #name es la variable resultante de unir el nombre del video con su extension
            name=vidname+extension
            #name1 nos sirve para poder guardarlo en la BBDD
            name1="/"+name
            #namebuket nos sirve para poder
            namebuket="/"+name
            h3="practica4-javgr-javicelma/"
            h4=h3+name
            ruta="https://practica4-javgr-javicelma.s3.amazonaws.com/"+user
            Ruta=ruta+name1

            consulta="Insert into Videos (Usuario,Tag,Vidname,Size,Ruta,FechaSubido,Extension) values('"+user+"','" +tag+"','"+vidname+"','"+size+"','"+Ruta+"',%s,'"+extension+"')"
            cur.execute(consulta,fechaSubido)
            conn.commit()

            return{
                'statusCode':200,
                'headers':{'Access-Control-Allow-Origin':'*'},
                'body':json.dumps({'videoSubido':'true'})
                }


    elif op== "delete":
        user=(event["queryStringParameters"]["Usuario"])
        vidname=(event["queryStringParameters"]["Vidname"])
        extension=(event["queryStringParameters"]["Extension"])
        with conn.cursor() as cur:
            query="DELETE FROM Videos WHERE Vidname='"+vidname+"' AND Usuario= '"+user+"';"
            cur.execute(query)
            conn.commit()
        #frase es el fichero qeu esta subido en el S
        frase=vidname+extension
        s3 = boto3.resource("s3")
        obj = s3.Object("practica4-javgr-javicelma",user+"/"+frase)
        obj.delete()

        return {

            'statusCode': 200,
            'headers':{'Access-Control-Allow-Origin':'*'},
            'body': json.dumps("delete ok")
        }
             

