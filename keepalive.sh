#!/usr/bin/env bash

ERR=`journalctl --no-pager -u rezeptionistin --since $(date +%H:%m -d "1 hour ago") | grep -c "DEBUG:root:ERROR :Closing Link: nixe.k4cg.org"`

if [ $ERR -ne 0 ]; then
  systemctl restart rezeptionistin
fi
