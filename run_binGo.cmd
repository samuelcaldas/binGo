@ECHO OFF
REM Este é um arquivo .cmd para executar o aplicativo Flask na porta 80
CD .

FLASK run --host=0.0.0.0 --port=80
pause
