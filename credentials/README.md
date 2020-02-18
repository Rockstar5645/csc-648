# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.


1. Server URL: http://ec2-18-144-94-29.us-west-1.compute.amazonaws.com/
2. SSH username: ubuntu
3. SSH password or key.
    <br> The ssh key,team6_ssh.pem, is uploaded to the credentials folder.
4. Database URL or IP and port used.
    <br><strong> database-1.cyuyicx0dvny.us-west-1.rds.amazonaws.com port 3306</strong> 
5. Database username: admin
6. Database password: Applepie9%
7. Database name: DB_Six
8. Instructions on how to use the above information.
- On pem key directory type: sudo ssh -i team6_ssh.pem ubuntu@ec2-18-144-94-29.us-west-1.compute.amazonaws.com
- For DB: mysql -h database-1.cyuyicx0dvny.us-west-1.rds.amazonaws.com -u admin -p 
- Enter DB password


# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.
