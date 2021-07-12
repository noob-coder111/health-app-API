
import boto3
# from pydantic.main import BaseModel
import jsons
# from pydantic import BaseModel
# from typing import List
from fastapi import FastAPI
from boto3.dynamodb.conditions import Key,Attr
# from fastapi.routing import APIRoute, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app=FastAPI(prefix="/health")


TABLE_NAME="resultTable"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="ap-south-1",
                                        aws_access_key_id="AKIAWHB3NDZVSH6FQQ4I",
                                        aws_secret_access_key="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"
                                 )

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME)

@app.get('/all')
def AllRecords():
    response = table.scan(TableName=TABLE_NAME)
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items']) 
    return data


@app.get('//{Doctor}/{Patient}')
def Records(Occupation,Name):
  
    response = table.scan(
                        TableName=TABLE_NAME,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr(Occupation).eq(Name)
                        )
    items = response['Items']
    print(items)
    return items

    dynamodb_client = boto3.client('dynamodb', region_name="ap-south-1",
                                        aws_access_key_id="AKIAWHB3NDZVSH6FQQ4I",
                                        aws_secret_access_key="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"
      
                                 )





TABLE_NAME2="Doctor"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb',region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME2)

@app.get('/Personal_details/{DoctorName}')
def Record(DoctorName):
  
    respons2 = table.scan(
                        TableName=TABLE_NAME2,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("Name").eq(DoctorName)
                        )
    item = respons2['Items']
    print(item)
    return item


@app.post('/Personal_details/{DoctorName}')
def EnterRecord(ID:str,DoctorName:str,Phone:str,Email:str,Password:str,Gender:str,Age:str,Experience:str,Designation:str):
    table = dynamodb.Table('Doctor')
    response = table.put_item(
       Item={
            'ID':ID,
            'Name':DoctorName,
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

TABLE_NAME3="Patient"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME3)

@app.get('/Personal_details//{PatientName}')
def Record2(PatientName):
  
    respons2 = table.scan(
                        TableName=TABLE_NAME3,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("Name").eq(PatientName)
                        )
    item2 = respons2['Items']
    print(item2)
    return item2


@app.post('/Personal_details//{PatientName}')
def EnterRecord2(ID:str, PatientName:str, Phone:str, Email:str, Password:str, Gender:str, Age:str, Complaints:str, Previous_Ailments:str):
    table = dynamodb.Table('Patient')
    response = table.put_item(
       Item={
            'ID':ID,
            'Name':PatientName,
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
