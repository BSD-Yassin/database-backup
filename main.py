import mysql.connector
from configparser import ConfigParser
import datetime
from logging import Logger

class MysqlConnect():
    def __init__(self):
        
        # simple class instanciation
        self.config = ConfigParser()
        self.creds = self.get_creds()
        self.logger = self.get_log()
        self.cnx = self.connect_db()
        self.relative_date, self.relative_month = self.get_conditions() 

    def get_creds(self):
        
        # Reads the credentials in the secrets.ini and stores them in the instance for later use
        creds = self.config.read('config/secrets.ini')
        creds = self.config['AUTH']
        return creds

    def get_conditions(self):
        
        # Reads the conditions in the secrets.ini and calculates them 
        conditions = self.config.read('config/secrets.ini')
        conditions = self.config['SETTINGS']
        
        # calculates the time from n months ago from now, can be changed for another interval (the function just uses the current date and substract the amount by days)
        relative_date = datetime.date.today() -datetime.timedelta(days=int(conditions['intervalfor_restauration']))
        relative_months = relative_date.month
        return relative_date, relative_months

    def get_log(self):

        # Creates a logger for any error or warning to throw
        logger = Logger("config/logs.ini")
        return logger

    def connect_db(self):
        try:
            # Uses the credentials to prompt for connection, if the credentials are ok and the port is open, the sql connector gets in the database
            config = {
            'user':self.creds['user'],        
            'password':self.creds['password'],
            'host':self.creds['ip'],
            'port':self.creds['port'],
            'database':self.creds['database']
            }
            cnx = mysql.connector.connect(**config)
            return cnx
        except:
            pass

    def get_values(self):
        # This only returns the value without any edition to it
        cursor = self.cnx.cursor()

        # change these values to the actual data, you can make a loop or dictionary or even a json
        data = "data"
        table = "table"
        date = ""
        relative_date = self.relative_date 
        
        # the f"" is ok, but some would use % and then the value, it's up to anyone
        query = {f"SELECT {data} FROM table"
                f"WHERE date > {relative_date} "}
        
        cursor.close()
        self.cnx.close()
        
    def move_values(self):
        # more or less the main objective, to move from one to another

        # Queries in SQL language
        cursor= self.cnx.cursor()


if __name__ == "__main__":

    # After defining everything, you can then use it here, any method output here will be done if the main will be ran
    instance = MysqlConnect()
    print(instance.__dict__)