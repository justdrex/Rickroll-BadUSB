@echo off
cd /d D:\
start /b python -m http.server 8080
timeout /t 2 /nobreak >nul
start http://localhost:8080/rickroll.html