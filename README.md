# Microsip API
This is an endpoint server for Microsip. It has direct access to the Microsip database (FirebirdSQL).

## Setup
### Run
```
$ python -m uvicorn main:app --host '192.168.8.17' --port 4200 --reload
```
### Make a request
```
fetch("http://0.0.0.0/articulos/<sku>")
```
