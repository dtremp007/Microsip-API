from firebird.driver import connect
import decimal
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/inventory")
def get_items( response: Response, query: str = 'select * from inventory'):
    response.headers["Access-Control-Allow-Origin"] = "*" 
    return queryDatabase(query)


def queryDatabase(query: str) -> dict:
    print(query)

    # Attach to 'employee' database/alias using embedded server connection
    con = connect('C:\\Users\\User\\Documents\\Databases\\examples.fdb', user='sysdba', password='masterkey')

    # Create a Cursor object that operates in the context of Connection con:
    cur = con.cursor()

    # Execute the SELECT statement:
    cur.execute(query)
    

    # Retrieve all rows as a sequence and print that sequence:


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
