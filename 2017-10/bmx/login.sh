#!/bin/bash

# source the needed environment settings

. ../.bmxConfig

echo "Using API KEY: ${API_KEY}"

${BX} login --apikey ${API_KEY}
