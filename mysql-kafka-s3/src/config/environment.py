from collections import namedtuple
import os

class EnvironmentVariable:

    def __init__(self):
        kafka_topic_list = []
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_FACT_SALE'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_EMP'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_CUST'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_PROD'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_DATE'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_LOC'))
        
        self.kafka_topic=namedtuple("kafka_topic",kafka_topic_list)(*kafka_topic_list)
        
        
        bootstrap_server  = os.getenv('KAFKA_BOOTSTRAP_SERVER')
        api_key = os.getenv('KAFKA_CLOUD_API_KEY')
        api_secret = os.getenv('KAFKA_CLOUD_API_SECRET')
        
        self.kafka_cloud = (namedtuple("kafka_cloud",["bootstrap_server","api_key","api_secret"])
        (bootstrap_server=bootstrap_server,api_key=api_key,api_secret=api_secret))


        mysql_user_name= os.getenv("MYSQL_USER_NAME")
        mysql_password = os.getenv("MYSQL_PASSWORD")
        mysql_uri = os.getenv("MYSQL_URI")
        
        self.mysql = (namedtuple("mysql",["uri","user_name","password"])
        (uri=mysql_uri,user_name=mysql_user_name,password=mysql_password))


        access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        bucket_name = os.getenv("BUCKET_NAME")
        
        self.aws = (namedtuple("aws",["access_key_id","secret_access_key","bucket_name"])
        (access_key_id=access_key_id,secret_access_key=secret_access_key,bucket_name=bucket_name))
        



