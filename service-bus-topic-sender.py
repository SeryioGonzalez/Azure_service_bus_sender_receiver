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

for i in range(5):
    msg = Message('Msg {0}'.format(i).encode('utf-8'),custom_properties={'messageposition': i})
    bus_service.send_topic_message(servicebus_topic, msg)
