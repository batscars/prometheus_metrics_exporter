# -*- coding: utf-8 -*-
import os
import sys
import prometheus_client
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask
import time
import logging
import yaml

cpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, cpath)

from exporter import metrics_handler

logging.basicConfig(filename=os.path.join(cpath, "logs", "monitor.log"),
                    filemode="a+",
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    level=logging.DEBUG)

app = Flask(__name__)

metrics_registry = CollectorRegistry(auto_describe=False)

# promethues metrics definition
with open(os.path.join(cpath, "configs", "config.yaml")) as f:
    content = f.read().strip()
metrics_info = yaml.safe_load(content)
local_names = locals()
for k, v in metrics_info.items():
    name = k
    description = v.get("description")
    current_metrics_labels = v.get("labels")
    local_names[name] = Gauge(name, description, current_metrics_labels, registry=metrics_registry)


@app.route("/metrics", methods=["GET"])
def gen_metrics():
    start = time.time()
    for key in metrics_info:
        values = getattr(metrics_handler, key)()
        for it in values:
            current_label_values = it[0:-1]
            local_names[key].labels(*current_label_values).set(it[-1])
            logging.info("metric:{}, labels:{}, value:{}".format(key, it[0:-1], it[-1]))
    end = time.time()
    logging.info("cost_time:{}".format(end - start))
    return Response(prometheus_client.generate_latest(metrics_registry), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)