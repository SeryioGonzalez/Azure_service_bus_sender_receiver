#!/bin/bash

#Environment
export environment_name="service-bus-demo"
export region="westeurope"

#Resource Group
export rg=$environment_name"-rg"

#Service Bus
export service_bus_namespace_name=$environment_name"-sb-namespace"
export service_bus_namespace_topic=$environment_name"-sb-topic"
export service_bus_namespace_key_name="RootManageSharedAccessKey"