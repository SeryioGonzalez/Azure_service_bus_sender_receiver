import os
import sys

from azure.servicebus.control_client import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

servicebus_namespace = os.environ['SERVICEBUS_NAMESPACE']
servicebus_key_value = os.environ['SERVICEBUS_KEY_VALUE']
servicebus_key_name = os.environ['SERVICEBUS_KEY_NAME']
servicebus_topic = os.environ['SERVICEBUS_TOPIC']

bus_service = ServiceBusService(
    service_namespace=servicebus_namespace,
    shared_access_key_name=servicebus_key_name,
    shared_access_key_value=servicebus_key_value)

bus_service.create_subscription(servicebus_topic, 'Messages')

while True :
    msg = bus_service.receive_subscription_message(servicebus_topic, 'Messages', peek_lock=False)
    print(msg.body)