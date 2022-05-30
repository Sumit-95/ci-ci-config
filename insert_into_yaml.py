import yaml
import string
import requests
import json
import time
import sys
import ast
Name = sys.argv[1]
hpa_yaml = """
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: ${sys.argv[4]}-service
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ${sys.argv[4]}-service
  minReplicas: 1
  maxReplicas: 3
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 75
"""
hpa = yaml.safe_load(hpa_yaml)
with open('hpa.yaml', 'w') as file:
    yaml.dump(hpa, file)
print(open('hpa.yaml').read())