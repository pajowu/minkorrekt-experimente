#!/bin/bash

scp -r -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null site/* pajowu@pajowu.de:/srv/http/minkorrekt