# -*- coding: UTF-8 -*-
from app.__init__ import app

from flask import render_template

@app.route('/')
def index():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)