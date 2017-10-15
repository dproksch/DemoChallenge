#!/bin/bash


. ../.bmxConfig

${BX} cf delete-space ${SPACE_NAME} -o ${ORG}

