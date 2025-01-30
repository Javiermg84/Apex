@echo off
call venv\scripts\activate
pytest -s -v -m "regression" --html .\reports\test_report_regression.html
pause