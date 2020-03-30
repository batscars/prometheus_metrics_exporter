# -*- coding: utf-8 -*-
"""
Define your customize metrics class here, only need to implement function metrics_values
"""
from core.core_metric import GaugeMetrics


class TestGaugeMetric(GaugeMetrics):
    __slots__ = ("logger", "metrics")

    @staticmethod
    def metrics_values(metric_name):
        if metric_name == "metrics_00":
            return [(("1", "2"), 1), (("2", "3"), 2)]
        else:
            return [(("1", "2", "3"), 1)]

m_instance = TestGaugeMetric()
