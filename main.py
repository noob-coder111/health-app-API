
import boto3
# from pydantic.main import BaseModel
import jsons
# from pydantic import BaseModel
# from typing import List
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





TABLE_NAME2 = "Doctor"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME2)

@app.get('/Personal details//{Doctor}')
def Record(Name):
  
    respons2 = table.scan(
                        TableName=TABLE_NAME2,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("Name").eq(Name)
                        )
    item = respons2['Items']
    print(item)
    return item


@app.put('/Personal details///{Doctor}')
def EnterRecord(ID:str, Name:str, Phone:str, Email:str, Password:str, Gender:str, Age:str, Experience:str, Designation:str):
    table = dynamodb.Table('Doctor')
    response = table.put_item(
       Item={
            'ID':ID,
            'Name':Name,
            'Phone':Phone,
            'Email':Email,
            'Password':Password,
            'Gender':Gender,
            'Age':Age,
            'Experience':Experience,
            'Designation':Designation
            }
    )
    return "Data added successfully"

TABLE_NAME3 = "Patient"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME3)

@app.get('/Personal details////{Patient}')
def Record2(Name):
  
    respons2 = table.scan(
                        TableName=TABLE_NAME3,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("Name").eq(Name)
                        )
    item2 = respons2['Items']
    print(item2)
    return item2


@app.put('/Personal details/////{Patient}')
def EnterRecord2(ID:str, Name:str, Phone:str, Email:str, Password:str, Gender:str, Age:str, Complaints:str, Previous_Ailments:str):
    table = dynamodb.Table('Patient')
    response = table.put_item(
       Item={
            'ID':ID,
            'Name':Name,
            'Phone':Phone,
            'Email':Email,
            'Password':Password,
            'Gender':Gender,
            'Age':Age,
            'Complaints':Complaints,
            'Previous_Ailments':Previous_Ailments
            }
    )
    return "Data added successfully"
