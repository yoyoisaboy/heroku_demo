# -*- coding: UTF-8 -*-
from app.__init__ import app

@app.route('/')
def index():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()