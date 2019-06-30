import boto3
import json
import os
from rds_instances import Instances

def get_all_RDS_instances():

#list to store all the instances
    my_instances = []

#get all RDS instances in the region
    rds = boto3.client('rds')
    response = rds.describe_db_instances()

#populate my_instances
    for x in response['DBInstances']:
        my_instances.append(Instances(
            name = x['DBInstanceIdentifier'],
            isAvail = x['DBInstanceStatus'],
            endpoint = x['Endpoint']['Address'],
            port = x['Endpoint']['Port'],
            dbuser = x['MasterUsername'],
            dbname = x['DBName']
        ))
    
    return my_instances

def list_user_choices():
    rds_instances = get_all_RDS_instances()

    index = 0
    for instance in rds_instances:
        print(index, instance.name)
        index +=1

    inp = input("Choose the instance you wish to connect to: ")


# Start of program

def main():
    list_user_choices()

if __name__ == "__main__":
    main()