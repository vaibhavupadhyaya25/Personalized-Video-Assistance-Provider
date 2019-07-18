import boto3
from botocore.client import Config
import csv


ACCESS_KEY_ID = '***'
ACCESS_SECRET_KEY = '****'
BUCKET_NAME = 'redditdatamajor'
FILE_NAME = 'RedditRealtimeDat.csv';


# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)



# file fetch
def cloud_fetch(domain_name):
    filename_mayur = "C:/Users/india/AppData/Local/Programs/Python/Python37/" + domain_name + ".csv"
#s3.Bucket(BUCKET_NAME).download_file(FILE_NAME, 'C:/Users/india/AppData/Local/Programs/Python/Python37/RedditRealtimeDat.csv');
    s3.Bucket(BUCKET_NAME).download_file(FILE_NAME,filename_mayur );

    data = open(FILE_NAME, 'rb')


    print ("File sucessfully fetched from amazon s3 cloud")
    print ("Processing file...")

    loc = (filename_mayur)

    fields = []
    rows = []
    with open(loc, 'r') as csvfile: 
    # creating a csv reader object 
        csvreader = csv.reader(csvfile)

        for row in csvreader: 
            rows.append(row)
    
    print ("Hey, here are some real world recommendations based on your domain")

#print ("Title", rows[1][3])
#abc = (rows[i][3])
#    s=""
#    count=0
#    for c in abc:
#        if(c==','):
#            break
#        if(c=='/'):
#            count=count+1
#        if(count==2 and c!='/'):
#            s+=c

# logic for /r removal to be added here

    i=1

    while(i<10):
        print (i, end =" ") 
        print (rows[i][3])
        print ("  It got " + rows[i][1] + " comments and " + rows[i][2] + " Upvotes!" )
        print("-----------------------------------------------------------------------------------------------------")
    #print(rows[i][1]),
    #print (" comments and "),
    #print(rows[i][2]),
    #print (" Upvotes!")
    #print(rows[i][4])
        i=i+1    
    


        
    
      

    
