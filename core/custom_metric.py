# -*- coding: utf-8 -*-
"""
Define your customize metrics class here, only need to implement function metrics_values
"""
from core.core_metric import CommonMetrics
from threading import Thread
import time


class TestGaugeMetric(CommonMetrics):
    __slots__ = ("logger", "metrics", "instant_metrics", "continus_metrics")

    @staticmethod
    def gauge_metric_values(metric_name):
        if metric_name == "metrics_00":
            return [(("1", "2"), 1), (("2", "3"), 2)]
        else:
            return [(("1", "2", "3"), 1)]

    @staticmethod
    def counter_metric_values(metric_name):
        return [(("1", "2"), 1)]


m_instance = TestGaugeMetric()


class CounterMetrics(Thread):
    def run(self):
        while True:
            m_instance.inc("metrics_02", [1, 2], 10)
            time.sleep(1)

CounterMetrics().start()
