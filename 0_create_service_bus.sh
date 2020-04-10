#!/bin/bash

source config.sh

subscription=$1


if [ $subscription"zz" != "zz" ]
then
    echo "Subscription set to $subscription"
    az account set --subscription $subscription
else
    echo "Specify subscription id for creating the environment"
    echo "Usage: ./create_service_bus.sh SUBSCRIPTION_ID"
    exit
fi

echo "Creating RG $rg in region $region"
az group create --name $rg --location $region --subscription $subscription --tags environment=$environment_name

echo "Creating service bus $service_bus_namespace_name"
az servicebus namespace create -g $rg --name $service_bus_namespace_name --sku Standard

echo "Creating topic $service_bus_namespace_topic in $service_bus_namespace_name"
az servicebus topic create -g $rg --namespace-name $service_bus_namespace_name --name $service_bus_namespace_topic
