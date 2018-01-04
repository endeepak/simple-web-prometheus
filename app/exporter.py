#!/usr/bin/python

import time
from prometheus_client import start_http_server
from prometheus_client.core import CounterMetricFamily, REGISTRY

PORT = 8080

class SimpleCountCollector(object):
  def __init__(self):
    self.http_requests_total = 0

  def collect(self):
    self.http_requests_total = self.http_requests_total + 1
    yield CounterMetricFamily('http_requests_total', 'Total HTTP requests', value = self.http_requests_total)

if __name__ == "__main__":
  print("Stating on port", PORT)
  start_http_server(PORT)
  REGISTRY.register(SimpleCountCollector())
  while True: time.sleep(1)