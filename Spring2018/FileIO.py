import os
import sys, csv, sqlite3
from sqlite3 import Error

file_name = "Public_Computer_Access_Locations.csv"
file = 0

def main():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(r"D:\05_Chegg\Others\projects\DataImporter\Dataimport.db") #Create a new SQLite3 DB with the same name
    except Error as e:
        print(e)

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Doping LOCTIONS table if already exists.
    cursor.execute("DROP TABLE IF EXISTS LOCATIONS")  #Dropping and creating locations table, and add in the columns from the CSV.

	#Creating table as per requirement  I have put all fields as NOT NULL you can omit it if not required.
    try:
        conn.execute('''CREATE TABLE LOCATIONS
				 (Lab_name              TEXT    NOT NULL,
                 Phone                  TEXT    NOT NULL,
				 Accessible             TEXT    NOT NULL,
                 Hours                  TEXT    NOT NULL,
                 Tech_Support_Assisted  TEXT    NOT NULL,
                 Organization           TEXT    NOT NULL,
                 Location               TEXT    NOT NULL,
				 Web_address            TEXT    NOT NULL);''')
    except Error as e:
        print('Error')
        print(e)
    print ("Table created successfully");

    try:
        file = open('Public_Computer_Access_Locations.csv', "r") #Open Public_Computer_Access_Locations.csv 
    except FileNotFoundError:
        print("File not found, Going to exit fro the program!.....")
        sys.exit(1)

    with open('Public_Computer_Access_Locations.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row. and use a loop to add in entries from the list (do not enter them by hand)
        for row in reader:	
            cursor.execute("INSERT INTO LOCATIONS VALUES (?, ?, ?, ?, ?, ?, ?, ?)",	row )

    # For printing the entered values in the Sqllite3 Database.
    #cursor.execute ("select * from LOCATIONS")
    #print(cursor.fetchall())
    conn.close() # closes connection to database

if __name__ == '__main__':
    main()
