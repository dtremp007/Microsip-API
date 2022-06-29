import database
from firebird.driver import connect
import json
import decimal

f = open('settings.json')
Settings = json.load(f)
f.close()

database = Settings["database"]["path"]
user = Settings["database"]["user"]
password = Settings["database"]["password"]



def queryDatabase(query: str) -> dict:
    print(query)

    # Attach to 'employee' database/alias using embedded server connection
    con = connect(database, user, password)

    # Create a Cursor object that operates in the context of Connection con:
    cur = con.cursor()

    # Execute the SELECT statement:
    cur.execute(query)

    container = {
        "data": []
    }

    for row in cur:
        newObj = {}
        for (value, desc) in zip(row, cur.description):
            if isinstance(value, decimal.Decimal):
                value = float(value)

            newObj[desc[0]] = value

        container["data"].append(newObj)

    return container
