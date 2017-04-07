#!/usr/bin/python
import time,requests,socket,json,argparse
import graphitesend
import datetime
from opsgenie import OpsGenie
from opsgenie.alert.requests import *
from opsgenie.config import Configuration
from opsgenie.errors import OpsGenieError

#Send data to graphite
def send_data_graphite(schema, backend_addr, backend_port, value): 
	 g=graphitesend.init(graphite_server=backend_addr, graphite_port=backend_port, lowercase_metric_names=True, system_name='', prefix='')
	 g.send(schema+"."+"count_closed",value)
	 g.send(schema+"."+"count_open",value)

#Variables declarations
config = Configuration(apikey="150ccb97-29c9-4e01-9a63-3825948b83a2")
client = OpsGenie(config)
customer="customer_meilleursagents"
count_closed=0
count_open=0

#Parsing arguments
parser = argparse.ArgumentParser(description='Querry datas from Opsgenie and send thel to graphite.', add_help=True)
parser.add_argument('-b', help='backend to send your data, default is graphite', default="graphite")
parser.add_argument('-s', help='schema to stored your data in graphite\n for example: customer.app.env.servername', default="test.test.prod.opsgenie")
parser.add_argument('-H', help='host of your backend, default is loaclhost', default="localhost")
parser.add_argument('-P', type=int, help='port of your backend, default is graphite port', default=2003)

#Querry infos from opsgeinie
try:
	list_alerts_response = client.alert.list_alerts(ListAlertsRequest())
	for alert in list_alerts_response.alerts:
		request = GetAlertRequest(id=alert.id)
		get_alert_response = client.alert.get_alert(request)
		if customer in  get_alert_response.tags:
			if get_alert_response.system_data.has_key('closedBy'):
				count_closed+=get_alert_response.count
			else:
				count_open+=get_alert_response.count
except OpsGenieError as err:
	print "[ERROR]", err.message
