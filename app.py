from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    env = os.getenv("APP_ENV", "BLUE")
    version = os.getenv("APP_VERSION", "1.0")

    return render_template(
        "index.html",
        env=env,
        version=version,
        updated=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)