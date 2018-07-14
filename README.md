# pidom
Python project controlling teleruptors using Raspberry Pi GPIO

# Automate using cron jobs
```
# 22H outside: ON, stairs: ON
0 22 * * * curl -k -u USER:PASS -X POST https://URL/frontdoorgroupstate --header 'Content-Type: application/json' -d'[true,true]'
# 2H outside: OFF, stairs: ON
0 2 * * * curl -k -u USER:PASS -X POST https://URL/frontdoorgroupstate --header 'Content-Type: application/json' -d'[false,true]'
# 6H outside: OFF, stairs: OFF
0 6 * * * curl -k -u USER:PASS -X POST https://URL/frontdoorgroupstate --header 'Content-Type: application/json' -d'[false,false]'
```
