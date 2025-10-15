@echo off
echo ========================================
echo    QUICK START - Livestream App
echo ========================================
echo.
echo Installing minimal dependencies...
cd backend
pip install Flask Flask-CORS
echo.
echo Starting backend server...
start "Backend" cmd /k "python simple_app.py"
echo.
echo Waiting 3 seconds...
timeout /t 3 /nobreak >nul
echo.
echo Starting frontend...
cd ..\frontend
start "Frontend" cmd /k "npm install && npm start"
echo.
echo ========================================
echo ✅ DONE! 
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo ========================================
pause