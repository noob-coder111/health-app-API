
import boto3
# from pydantic.main import BaseModel
import jsons
from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI,Query,Request
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
class ItemDoctor(BaseModel):
    ID:str
    DoctorName:str
    Phone:Optional[str] = Query(None, max_length=10, min_length=10)
    Email:str
    Password:str
    Gender:str
    Age:str
    Experience:str
    Designation:str

class ItemPatient(BaseModel):
    ID:str
    PatientName:str
    Phone:Optional[str] = Query(None, max_length=10, min_length=10)
    Email:str
    Password:str
    Gender:str
    Age:str
    Complaints:str
    Previous_Ailments:str



TABLE_NAME="resultTable"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="ap-south-1",
                                        aws_access_key_id="AKIAWHB3NDZVSH6FQQ4I",
                                        aws_secret_access_key="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"
                                 )

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME)


@app.get('/{Patient}')
def Records(Patient:str):
    response = table.scan(
                        TableName=TABLE_NAME,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("Patient").eq(Patient)
                        )
    items = response['Items']
    print(items)
    return items




@app.get('/all/')
def AllRecords():
    response = table.scan(TableName=TABLE_NAME)
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items']) 
    return data



TABLE_NAME2="Doctor"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb',region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME2)

# #here is the error, it isn"t taking reference for class data
# @app.post('/personaldetails/',response_model=Item)
# def EnterRecord(item=Item,Phone:str= Query(None,max_length=10, min_length=10)):
#     table = dynamodb.Table('Doctor')

#     return item

@app.put("/personaldetails/adddoctor")
async def create_item(item:ItemDoctor):

    table = dynamodb.Table('Doctor')

    table.put_item(
    Item={
            'ID':item.ID,
            'DoctorName':item.DoctorName,
            'Phone':item.Phone,
            'Email':item.Email,
            'Password':item.Password,
            'Gender':item.Gender,
            'Age':item.Age,
            'Experience':item.Experience,
            'Designation':item.Designation

    }
    )       
    return "Data added successfully"
    
@app.get('/personaldetails/{DoctorName}')
def Record(DoctorName:str):
  
    respons2 = table.scan(
                        TableName=TABLE_NAME2,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("DoctorName").eq(DoctorName)
                        )
    item = respons2['Items']
    print(item)
    return item


TABLE_NAME3="Patient"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table(TABLE_NAME3)


@app.put('/personaldetails/addpatient')
def EnterRecord2(item:ItemPatient):
    table = dynamodb.Table('Patient')
    response = table.put_item(
       Item={
            'ID':item.ID,
            'PatientName':item.PatientName,
            'Phone':item.Phone,
            'Email':item.Email,
            'Password':item.Password,
            'Gender':item.Gender,
            'Age':item.Age,
            'Complaints':item.Complaints,
            'Previous_Ailments':item.Previous_Ailments
            }
    )
    
    return "Data added successfully"



@app.get('/personaldetails/{PatientName}/')
def Record2(PatientName:str):
  
    respons2 = table.scan(
                        TableName=TABLE_NAME3,
                        #KeyConditionExpression=Key("").eq("1"),
                        FilterExpression=Attr("PatientName").eq(PatientName)
                        )
    item2 = respons2['Items']
    print(item2)
    return item2
