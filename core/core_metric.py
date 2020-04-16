# -*- coding: utf-8 -*-
import os
import time
from core import get_logger
from prometheus_client.core import CollectorRegistry
from prometheus_client import Gauge
import yaml

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
metrics_registry = CollectorRegistry(auto_describe=False)


class GaugeMetrics(object):
    __slots__ = ("logger", "metrics")
    def __init__(self, config=os.getenv("CONFIG", os.path.join(root, "configs", "config.yaml"))):
        with open(config) as f:
            content = f.read().strip()
        metrics_info = yaml.safe_load(content)
        name = metrics_info.get("name", "prometheus_exporter")
        metrics_defs = metrics_info.get("metrics", [])

        self.logger = get_logger(os.path.join(root, "logs", "{}.log".format(name)), name)
        self.metrics = dict()
        for item in metrics_defs:
            metric_name = item.get("name")
            metric_desc = item.get("description")
            metric_labels = item.get("labels")
            self.metrics[metric_name] = Gauge(metric_name, metric_desc, metric_labels, registry=metrics_registry)

    def update(self):
        self._update_metrics()

    def _update_metrics(self):
        for k, v in self.metrics.items():
            t0 = time.time()
            for item in self.metrics_values(k):
                if not item:
                    continue
                labels, value = item[0], item[1]
                v.labels(*labels).set(value)
                self.logger.info("metric:{}, labels:{}, value:{}".format(k, labels, value))
            self.logger.info("metric:{}, cost_time:{}".format(k, time.time() - t0))

    @staticmethod
    def metrics_values(metric_name):
        """在子类中重写改函数，该函数功能为获取metrics值
        :param metric_name:
        :return:
        """
        labels = []
        value = 1
        return [(labels, value)]

    def __str__(self):
        _str = ""
        for key in self.__slots__:
            _str += "{}={}|".format(key, getattr(self, key))
        return _str
