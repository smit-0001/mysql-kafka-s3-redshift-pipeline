## Part 2 -Structure 

### What does the Source code contain ! ?

```markdown
- src/entity --> we define the structure type (schema) of the data.

- src/utils --> we define functions to read , write and query df from redshift.

- src/config/
  - environment.py --> to set up envirnments variables which we defined in our .env file
  - spark-manager.py --> configurations for spark-session

- src/pipeline/
  - s3_to_redshift.py --> function which does the main task "transfer_data_from_s3_to_redshift" is written here.
```

> Create .env file and set required environment variables
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
REDSHIFT_USER_NAME=""
REDSHIFT_PASSWORD=""
TEMP_BUCKET_NAME=""
REDSHIFT_JDBC_URL="jdbc:redshift://<hostname>:5439/<database>?user=<user_name>&password=<password>&ssl=true&sslfactory=com.amazon.redshift.ssl.NonValidatingFactory"
```
