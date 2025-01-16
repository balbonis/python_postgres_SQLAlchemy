from flask import Flask
app = Flask(__name__)
#####################DB connection option using SQLAlchemy#######################
from sqlalchemy import create_engine, text

# Define database connection parameters
DB_USERNAME = "postgres"
DB_PASSWORD = "Bongo6969"
DB_HOST = "localhost" # or your database host
DB_PORT = "5432" # default PostgreSQL port
DB_NAME = "MyFlaskDB"


# Create the database URL
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def connect_to_database_and_fetch_emails():
    try:  
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            print ("Connection is successful! \n")      
            global message 
            global emailids
            query = text("Select useremail from userslist;")
            result = connection.execute(query)
            for row in result:
                print (row[0])
                message = "<strong>Connected via SQLAlchemy</strong>"
                emailids = str(row[0])
                message = message + " " + "Created by: " + emailids

        connection.close() 

    except Exception as e:
        print ("Unable to connect to Database \n")
        print (f"Error: {e} \n")
      
    
#####################DB connection option using SQLAlchemy#######################



connect_to_database_and_fetch_emails()


@app.route("/")
def home():
    return message