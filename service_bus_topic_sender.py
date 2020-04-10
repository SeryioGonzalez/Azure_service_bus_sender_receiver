import os
from azure.servicebus.control_client import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME
from datetime import datetime

servicebus_namespace = os.environ['service_bus_namespace_name']
servicebus_topic     = os.environ['service_bus_namespace_topic']
servicebus_key_value = os.environ['service_bus_namespace_key_value']
servicebus_key_name  = os.environ['service_bus_namespace_key_name']

now = datetime.now()

#Creating a bus service instance
bus_service = ServiceBusService(
    service_namespace=servicebus_namespace,
    shared_access_key_name=servicebus_key_name,
    shared_access_key_value=servicebus_key_value)

print ("Initialized connection to service bus {} on topic {} at {}".format(servicebus_namespace, servicebus_topic, now))

num_messages = 5
for i in range(num_messages):
    now = datetime.now()
    message_content = 'Msg {0} at {1}'.format(i, now).encode('utf-8')
    print ("  Sending message {} ".format(message_content))
    msg = Message(message_content, custom_properties={'messageposition': i})
    bus_service.send_topic_message(servicebus_topic, msg)
