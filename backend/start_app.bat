@echo off

echo Starting Backend...
start cmd /k "cd backend && venv\Scripts\activate && uvicorn main:app --reload"

timeout /t 5

echo Starting Frontend...
start cmd /k "cd frontend && npm run dev"

timeout /t 5

start http://localhost:5173

echo App Started Successfully!