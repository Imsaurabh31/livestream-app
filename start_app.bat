@echo off
echo ========================================
echo    Livestream App Startup Script
echo ========================================
echo.
echo This will start both backend and frontend servers.
echo Make sure MongoDB is running before proceeding.
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul

echo.
echo Starting Backend Server...
start "Backend Server" cmd /k "cd backend && python app.py"

echo Waiting for backend to initialize...
timeout /t 5 /nobreak >nul

echo.
echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd frontend && npm start"

echo.
echo ========================================
echo Both servers are starting up!
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo The frontend will open automatically in your browser.
echo ========================================
pause