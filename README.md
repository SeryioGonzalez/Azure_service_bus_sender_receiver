
# Azure_service_bus_sender_receiver

These snippets allow creating a service bus namespace, write sample messages to it and read them

# Prerequisites
These snippets require a linux environment, python3, Azure Service Bus python SDK and Azure CLI installed. If you have those already installed, go to the next section. 
For installing the Azure az CLI, please refer to the [Azure Documentation](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
Additionally, you would need the to install additional packages with the following snippet:

```


```
Once installed, perform account login using ```az login```

If now, execute the following snippet:
```
export SERVICEBUS_NAMESPACE="sergio-servicebus"
export SERVICEBUS_KEY_NAME="RootManageSharedAccessKey"
export SERVICEBUS_KEY_VALUE="dsdsdsdsdsdsdsdsdddsdZC59/wMfcYVTWM="
export SERVICEBUS_TOPIC="device-messages"
```

# Creating an Azure service bus (Optional)
You can use the scripts provided for writing and reading from an existing service bus an topic, but the following script would create a test environment. You need to provide the subscription id as parameter and have executed previously az login to this very subscription.
<pre>
<b> ./0_create_service_bus.sh 11111111-2222-3333-4444-55555555555 </b>
Subscription set to 11111111-2222-3333-4444-55555555555
Creating RG service-bus-demo-rg in region westeurope
{
  "id": "/subscriptions/11111111-2222-3333-4444-55555555555/resourceGroups/service-bus-demo-rg",
  "location": "westeurope",
  "managedBy": null,
  "name": "service-bus-demo-rg",
  "properties": {
    "provisioningState": "Succeeded"
    .......
</pre>

# Sending sample messages to a service bus
If you have created the environment with the script **0_create_service_bus.sh**, the message delivery script does not need additional parameters.
<pre>
<b> ./1_service_bus_sender.sh  </b>
Initialized connection to service bus service-bus-demo-sb-namespace on topic service-bus-demo-sb-topic at 2020-04-10 15:59:42.774624
  Sending message b'Msg 0 at 2020-04-10 15:59:42.774983' 
  Sending message b'Msg 1 at 2020-04-10 15:59:48.323102' 
  Sending message b'Msg 2 at 2020-04-10 15:59:48.430927' 
  Sending message b'Msg 3 at 2020-04-10 15:59:48.539948' 
  Sending message b'Msg 4 at 2020-04-10 15:59:48.648204' 
</pre>

Additionally it can send sample messages to any service bus topic overriding default parameters
<pre>
<b>./1_service_bus_sender.sh -h  </b>
Usage: cmd [-n service_bus_namespace_name] [-g resource_group] [-k key_value] [-t topic]
</pre>

# Receiving messages from a service bus
If you have created the environment with the script **0_create_service_bus.sh**, the script for receiving messages does not need additional parameters.
<pre>
<b>  ./2_service_bus_receiver.sh  </b>
Initialized connection to service bus service-bus-demo-sb-namespace on topic service-bus-demo-sb-topic at 2020-04-10 16:05:10.806744
  Recieved message: b'Msg 0 at 2020-04-10 15:59:42.774983'
  Recieved message: b'Msg 1 at 2020-04-10 15:59:48.323102'
  Recieved message: b'Msg 2 at 2020-04-10 15:59:48.430927'
  Recieved message: b'Msg 3 at 2020-04-10 15:59:48.539948'
  Recieved message: b'Msg 4 at 2020-04-10 15:59:48.648204'
</pre>

Additionally it can receive messages to any service bus topic overriding default parameters
<pre>
<b>./2_service_bus_receiver.sh -h </b>
Usage: cmd [-n service_bus_namespace_name] [-g resource_group] [-k key_value] [-t topic]
</pre>
