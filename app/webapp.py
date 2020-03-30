# -*- coding: utf-8 -*-
import os
import sys
import prometheus_client
from flask import Response, Flask

cpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, cpath)

from core import metrics_registry, m_instance


app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def gen_metrics():
    m_instance.update()
    return Response(prometheus_client.generate_latest(metrics_registry), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)