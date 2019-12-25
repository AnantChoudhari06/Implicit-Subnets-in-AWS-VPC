#!/usr/bin/env python
import json
import boto3
import re

ec2 = boto3.resource('ec2')
client=boto3.client('ec2')
vpcid = raw_input("Please enter a valid VPC ID : ")  #GET THE VPC ID FROM USER
vpc = ec2.Vpc(vpcid)
print("**********************")
subnet_iterator = vpc.subnets.all()                  #ITERATE OVER THE SUBNETS IN THE GIVEN VPC
ListOfSubnets = list(subnet_iterator)  
val = str(ListOfSubnets)
SubnetsinVpc = re.findall("subnet\W\w*",val)         #USING REGEX TO GET THE SUBNETS
print("SUBNETS IN VPC :")
SubnetSet = list(set(SubnetsinVpc))                  #PRINT EACH SUBNET FROM THE SET
for subnet in SubnetSet:
	print(subnet)


print("**********************")



response= client.describe_route_tables(
	Filters=[                                     #USE THIS TO FILTER THE DESCRIBE CALL BY THE PARAMETER PROVIDED
        { 
            'Name': 'vpc-id',                         #FILTERING THE DECRIBE ROUTE TABLE CALL BY 'VPC-ID'
            'Values': [
                vpcid,
            ]
        },
    ],
)
OutputInJson=json.dumps(response)
SubnetsAssociated=re.findall("subnet\W\w*",OutputInJson)              ##USING REGEX TO GET ALL THE SUBNETS IN THE OUTPUT(EXPLICITLY ASSOCIATED)
print("LIST OF EXPLICITLY ASSOCIATED SUBNETS:")
SubnetSet = list(set(SubnetsAssociated)) 
for subnet in SubnetSet:
	print(subnet)
print("**********************")
ImplicitSubnet = list(set(SubnetsinVpc)-set(SubnetsAssociated))       #Subtracting the subnets in list and Associated subnets which gives Implicit subnets
if not ImplicitSubnet:
  print("NO IMPLICIT SUBNETS FOUND")
else:
  print("LIST OF IMPLICITLY ASSOCIATED SUBNETS:")
  ImplicitList = list(set(ImplicitSubnet)) 
  for i in ImplicitList:
     print(i)
