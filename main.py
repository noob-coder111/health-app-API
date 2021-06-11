
import boto3
from pydantic.main import BaseModel
import json
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from boto3.dynamodb.conditions import Key,Attr
# from fastapi.routing import APIRoute, APIRouter

app=FastAPI(prefix="/health")


TABLE_NAME = "resultTable"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="ap-south-1",
                                        aws_access_key_id="AKIAWHB3NDZVSH6FQQ4I",
                                        aws_secret_access_key="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"
                                 )

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME)

@app.get('/{Doctor}/{Patient}')
def Records(Query,Name):
  
    response = table.scan(
                        TableName=TABLE_NAME,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr(Query).eq(Name)
                        )
    items = response['Items']
    print(items)
    return items

    dynamodb_client = boto3.client('dynamodb', region_name="ap-south-1",
                                        aws_access_key_id="AKIAWHB3NDZVSH6FQQ4I",
                                        aws_secret_access_key="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"
      
                                 )



TABLE_NAME2 = "resultTable2"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME)

@app.get('/Personal details/{Doctor}/{Patient}')
def Record(Name):
  
    respons = table.scan(
                        TableName=TABLE_NAME2,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("Name").eq(Name)
                        )
    item = respons['Items']
    print(item)
    return item


@app.put('/Personal details/{Doctor}/{Patient}')
def EnterRecord(ID:str, Name:str, Age:str, Patient:str, Doctor:str):
    table = dynamodb.Table('resultTable2')
    response = table.put_item(
       Item={
            'ID':ID,
            'Name':Name,
            'Age':Age,
            'Patient':Patient,
            'Doctor':Doctor
            }
    )
    return "Data added successfully"


