#!/bin/bash

source config.sh

while getopts "n:g:k:t:h" opt; do
  case ${opt} in
    n ) # process option n
        echo "EVENT HUB NAMESPACE IS $OPTARG"
        export service_bus_namespace_name=$OPTARG
      ;;
    g ) # process option g
        echo "RG IS $OPTARG"
        export rg=$OPTARG
      ;;
    k ) # process option k
        echo "KEY IS $OPTARG"
        export service_bus_namespace_key_value=$OPTARG
      ;;
    t ) # process option t
        echo "TOPIC IS $OPTARG"
        export service_bus_namespace_topic=$OPTARG
      ;;
    h ) # process option h
        echo "Usage: cmd [-n service_bus_namespace_name] [-g resource_group] [-k key_value] [-t topic]"
        exit
      ;;
    \? ) 
        echo "Usage: cmd [-n service_bus_namespace_name] [-g resource_group] [-k key_value] [-t topic]"
        exit
      ;;
  esac
done

set -e

if [ $service_bus_namespace_key_value"zzz" = "zzz" ]
then
    export service_bus_namespace_key_value=$(az servicebus namespace authorization-rule keys list -g $rg --namespace-name $service_bus_namespace_name -n RootManageSharedAccessKey --query "primaryKey" -o tsv)
fi

python3 service_bus_topic_receiver.py
