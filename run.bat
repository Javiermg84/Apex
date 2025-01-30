@echo off
call venv\scripts\activate
pytest -s -v -m "regression" --html .\reports\test_report_regression.html
rem pytest -s -v -m "smoke" --html .\reports\test_report_smoke.html
pause