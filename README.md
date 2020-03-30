##### Description
prometheus Gauge type metrics exporter template, written in python+flask+prometheus client

##### Develop Steps
1. Modify configs/config.yaml
1. Define metrics in core/custom_metric.py, just rewrite metrics_values function
2. Initialize metric instance in core/metrics_instance.py
3. Generate supervisor configuration file
