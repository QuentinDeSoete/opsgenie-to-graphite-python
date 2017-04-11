#!/usr/bin/python
import time,requests,socket,json,argparse
import graphitesend
import datetime
from opsgenie import OpsGenie
from opsgenie.alert.requests import *
from opsgenie.config import Configuration
from opsgenie.errors import OpsGenieError

#Send data to graphite
def send_data_graphite(schema, backend_addr, backend_port, value, key_name): 
	 g=graphitesend.init(graphite_server=backend_addr, graphite_port=backend_port, lowercase_metric_names=True, system_name='', prefix='')
	 g.send(schema+"."+key_name,value)

#Variables declarations
customer=""
count_closed=0
count_open=0

#Parsing arguments
parser = argparse.ArgumentParser(description='Querry datas from Opsgenie and send thel to graphite.', add_help=True)
parser.add_argument('-k', help='your opsgenie apikey', required=True)
parser.add_argument('-b', help='backend to send your data, default is graphite', default="graphite")
parser.add_argument('-s', help='schema to stored your data in graphite\n for example: customer.app.env.servername', default="test.test.prod.host.opsgenie")
parser.add_argument('-H', help='host of your backend, default is loaclhost', default="localhost")
parser.add_argument('-P', type=int, help='port of your backend, default is graphite port', default=2003)
parser.add_argument('-c', help='customer you want to querry',required=True)

#Feeding variables
args = parser.parse_args()
config = Configuration(apikey=args.k)
client = OpsGenie(config)
backend=args.b
schema=args.s
backend_addr=args.H
backend_port=args.P
customer=args.c


#Querry infos from opsgeinie
try:
	list_alerts_response = client.alert.list_alerts(ListAlertsRequest())
	for alert in list_alerts_response.alerts:
		request = GetAlertRequest(id=alert.id)
		get_alert_response = client.alert.get_alert(request)
		if customer in  get_alert_response.tags:
			if "closedBy" in get_alert_response.system_data:
				count_closed+=get_alert_response.count
			else:
				count_open+=1
except OpsGenieError as err:
	print ("[ERROR]"), err.message

if backend == "graphite":
	send_data_graphite(schema, backend_addr, backend_port, count_closed, "count_closed")
	send_data_graphite(schema, backend_addr, backend_port, count_open , "count_open")
