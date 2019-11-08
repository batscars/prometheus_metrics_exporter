FROM python:3.7.3-alpine
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
EXPOSE 5555
COPY . /metrics_exporter
WORKDIR /metrics_exporter
CMD ["supervisord", "-c", "supervisor/supervisord.conf"]