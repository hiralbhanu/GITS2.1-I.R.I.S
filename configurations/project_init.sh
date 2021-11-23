#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
echo "$SCRIPT_DIR"

PROJECT_DIR=${SCRIPT_DIR%/*}
echo "$PROJECT_DIR"

RELATIVE_GITS_PATH="code/gits.py"
echo "$RELATIVE_GITS_PATH"

GITS_EXEC_PATH="${PROJECT_DIR}/${RELATIVE_GITS_PATH}"
echo "$GITS_EXEC_PATH"

BASHRC=~/.bashrc
if [ -f "$BASHRC" ]; then
    echo "$BASHRC exists, appending gits commandline tool alias"
    echo "alias gits=\"python3 $GITS_EXEC_PATH\"" >> $BASHRC
    echo "export GITS_HOME=${PROJECT_DIR}" >> $BASHRC
else
    echo "$BASHRC does not exist, creating a new file and adding gits commandline tool alias"
    echo "alias gits=\"python3 $GITS_EXEC_PATH\"" >> $BASHRC
    echo "export GITS_HOME=${PROJECT_DIR}" >> $BASHRC
fi

echo "Initialising gits directory in user home directory"

GITS=~/.gits
GITS_LOG=~/.gits/logs

mkdir -p $GITS $GITS_LOG
