# simple-web-prometheus

Simple web exporter for prometheus which exports number of HTTP requests made to this service

### Run

#### Using code (local)

```
# Ensure python 2.x and pip installed
pip install -r app/requirements.txt
python app/exporter.py
```

#### Using docker

```
docker run -p 8080:8080 endeepak/simple-web-prometheus
```

### Metrics

Metrics will available in http://localhost:8080

```sh
$ curl localhost:8080
# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total 6347.0
```
