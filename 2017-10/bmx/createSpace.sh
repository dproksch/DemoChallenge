#!/bin/bash

. ../.bmxConfig

${BX} cf create-space ${SPACE_NAME} -o ${ORG}

${BX} target -o ${ORG}  -s ${SPACE_NAME}
