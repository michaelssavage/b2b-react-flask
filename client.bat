@echo ON
where node || echo NodeJS not installed
cd client
call npm install
call npm start