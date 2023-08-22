conda create -n prefect-ops python=3.9.12

prefect server start

In another terminal with same conda env,

prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api


## Initilise Project

prefect project init

Create a workpool

Deploy
prefect deploy 3.4/orchestrate.py:main_flow -n taxi1 -p zoompool

Start a worker

prefect worker start -p zoompool -t process