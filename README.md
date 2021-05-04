# B2B ordering system with ReactJS and Flask

# Video Walkthrough

<p align="center">
    <a href="https://youtu.be/QR2c3D1hUAM" target="_blank"><img src="http://img.youtube.com/vi/QR2c3D1hUAM/0.jpg" 
    alt="CA4006 Assignment" width="300" height="240" border="10" /></a>

</p>

## Versions
NodeJS needs to be installed to run the client with npm and Python needs to be installed to run the Flask server. Applications current versions:
1. **npm -v** - 6.14.8
2. **python --version** - 3.9.2

The following commands can easily be run using the client.bat and server.bat scripts.

# Starting the Client 

1. **cd client**
2. **npm install** - install all the node_modules.

3. **npm start** - start the client.

# Starting the Server

1. **cd server**
2. **python -m venv env**  - install the Python virtual environment

3. **env\Scripts\activate** - Starts the environment

4. **pip install -r requirements.txt**  - install the Flask packages 

5. **flask run**  - start the flask server

---
**if using vscode add:**
```
{
    "python.pythonPath": "server\\env\\Scripts\\python.exe"
}
