# Implicit-Subnets-in-AWS-VPC
This script lists the Implicitly associated subnets in AWS VPC


A subnet which is not exlicitly associated to a Route Table gets implicitly associated to the Main Route Table.

For example, If a VPC has 4 subnets and 3 are expliclty associated to a Route Table.The 4the subnet if not explicitly associated to any Route Table get Implicitly associated to Main Route Table.

This subnet can not be listed using 'describe-route-table' API call.
[+] https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-route-tables.html


 aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-12344" --query  'RouteTables[*].[Associations[*].SubnetId]' --output text

This command will only list 3 subnets whereas there are 4 subnets in the VPC.

The python script takes in the VPC as the input provides the following in output:
All Subnets in VPC
Explicitly Associated Subnets
Implicitly Associated Subnets

Inputs:
VPC ID ----Enter the VPC ID from a region for which AWS CLI is configured

Output:

Output:

**********************

SUBNETS IN VPC :


**********************

LIST OF EXPLICITLY ASSOCIATED SUBNETS:



**********************

LIST OF IMPLICITLY ASSOCIATED SUBNETS:


 

