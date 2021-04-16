echo ON
where python || echo Python is not installed
cd server
python -m venv env
call env\Scripts\activate.bat
set FLASK_APP=app.py
set FLASK_ENV=development
pip install -r requirements.txt 
flask run
pause