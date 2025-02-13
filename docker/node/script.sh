#!/bin/bash
if grep "PRODUCTION" /node_mode > /dev/null; then
  cross-env NODE_ENV=production pm2-runtime start --name patio-prod server.js
elif grep "DEVELOPMENT" /node_mode > /dev/null; then
  cross-env NODE_ENV=development NODE_OPTIONS='--inspect' pm2-runtime start --name patio-dev server.js
else
  tail -f /dev/null
fi