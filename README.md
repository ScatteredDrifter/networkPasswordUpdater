# networkPasswordUpdater
A simple script aiming to provide a mean to update passwords on several network devices.
It provides the ability to query a **dicepassword** from [diceware](diceware.dmuth.org/), 

However its easier to implement this within python, as it does not require js to be run in a browser to obtain a generated password. 
So I instead added code to supply a password from a dice-password

## Premises: 


A list of hosts ( exported from netbox for example) containing:
- ip-address
- username
- password
formatted as follows **per line**:

```bash
username,ip,password
```



## Running script:

## considerations   