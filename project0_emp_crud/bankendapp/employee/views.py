from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from dbconfig import database
import json


def index(request):
    return JsonResponse({'data':'Backend is Ready with Database'})


def getAllEmployees(request):
    conn=database.connectDatabase()
    #print("\n Connection Succeed at ", conn)

    cur=conn.cursor()
    query="SELECT empid,fullname,gender,location,emailid,projectleader,projectcost FROM Employee"
    cur.execute(query)

    emprec=dict()
    for empid,fullname,gender,location,emailid,projectleader,projectcost in cur.fetchall():
        emprec[empid]={'empid':empid,'fullname':fullname,'gender':gender,'location':location,'projectleader':projectleader,'projectcost':projectcost}

    return JsonResponse({'employees':emprec},json_dumps_params={'indent': 2})

def insertEmpRecord(request):
    print(request.POST)
    return JsonResponse({'msg':'Employee Record Received'})