#!../venv/bin/python
from app import webapp

webapp.run('127.0.0.1', 5000, debug=False)

# webapp.run('0.0.0.0',5000)
