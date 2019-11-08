##### Description
prometheus Gauge type metrics exporter template, written in python+flask+prometheus client

##### Develop Steps
1. Define metrics
2. Write cal metrics functions
3. Generate supervisor configuration file

###### Define metrics
modify configs/config.yaml, define metrics name, descrtiption and label names

###### Write cal metrics functions
modify exporter/metrics_handler.py, metrics cal functions are named the same as metrics names defined in last step,
metrics cal function returns tuple lists, which tuple including label values and metrics value.

###### Generate supervisor configuration file
run tools/gen_supervisor_conf.py should provide path_prefix, project_name, and port
