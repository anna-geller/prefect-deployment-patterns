# set during deployment build:
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule '{"rrule": "DTSTART:20221224T120000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=12,13,14,15,16,17", "timezone": "Europe/Berlin"}'

# set after the deployment has been created:
prefect deployment set-schedule flows/hello.py:hello --rrule '{"rrule": "DTSTART:20221224T120000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=12,13,14,15,16,17", "timezone": "Europe/Berlin"}'
