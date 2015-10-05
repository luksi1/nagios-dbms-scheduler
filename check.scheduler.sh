#!/bin/bash

# Wrapper for check.scheduler.py
# This is needed to set LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/oracle/instantclient_12_1

# Make sure this points to your script
python /opt/oracle/scripts/monitoring/check.scheduler.py
