# B2B ordering system with ReactJS and Flask

## Versions
NodeJS needs to be installed to run the client with npm and Python needs to be installed to run the Flask server. Applications current versions:
- npm -v is 6.14.8
- python --version is 3.9.2

The following commands can easily be run using the client.bat and server.bat scripts.

# Starting the Client 

## cd client
## npm install
install all the node_modules.

## npm start 
start the client.

# Starting the Server 

## cd server
## python -m venv env 
install the virtual environment

## env\Scripts\activate
Starts the Python virtual environment

## pip install -r requirements.txt 
install the Flask packages 

## flask run 
start the flask server

---
**if using vscode add:**
```
{
    "python.pythonPath": "server\\env\\Scripts\\python.exe"
}