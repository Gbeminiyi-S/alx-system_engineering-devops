#!/usr/bin/python3
"""
Get the total number of active hosts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi("54.146.81.195")
    response = api_instance.get_host_totals()

    print(response)
