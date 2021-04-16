echo ON
cd server
python -m venv env
call server\env\Scripts\activate.bat
set FLASK_APP=app.py
set FLASK_ENV=development
pip install -r requirements.txt 
flask run
pause