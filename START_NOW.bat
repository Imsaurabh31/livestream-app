@echo off
cd backend
pip install Flask Flask-CORS
start python fast_app.py
cd ..\frontend
timeout /t 2 /nobreak >nul
start npm start