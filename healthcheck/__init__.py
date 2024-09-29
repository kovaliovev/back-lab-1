from flask import Flask

app = Flask(__name__)

import healthcheck.views
