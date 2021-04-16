@echo ON
where node || echo Node.js not installed
call npm -v
cd client
call npm install
call npm start