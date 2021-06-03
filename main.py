# import boto3
# from pydantic.main import BaseModel
# import json
# from pydantic import BaseModel
# from typing import List
# from fastapi import FastAPI
# from boto3.dynamodb.conditions import Key,Attr


# app=FastAPI()


# TABLE_NAME = "resultTable"

# # Creating the DynamoDB Client
# dynamodb_client = boto3.client('dynamodb', region_name="ap-south-1")

# # Creating the DynamoDB Table Resource
# dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
# table = dynamodb.Table(TABLE_NAME)

# #app.include_router(doctor.router)
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
dynamodb_client = boto3.client('dynamodb', region_name="ap-south-1")

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
