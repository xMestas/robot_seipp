#!/bin/bash

# Run the get_ranks.py script every 5 minutes.
# I would do this as a cron job, but I can't setup cron jobs on the machine I'm using.
while [ true ]
do

python3 get_ranks.py
sleep 300

done
