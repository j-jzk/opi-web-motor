# Web motor
A tool to control a CD drive stepper motor through a web interface.

It was designed for Orange Pi PC, but it should also be usable on other single-board computers with some tinkering.

## How to use
Connect your motor controller according to the table. 

| Wire          | WiringPi pin | BCM pin | "Physical" pin |
| ------------- | ------------ | ------- | -------------- |
| Coil A, end 1 | 25           | 20      | 37             |
| Coil A, end 2 | 24           | 10      | 35             |
| Coil B, end 1 | 23           | 9       | 33             |
| Coil B, end 2 | 22           | 8       | 31             |
_Tab.: pin connections in different numbering systems_

Then clone the repository, navigate into it and run these commands: 
```bash
sudo pip3 install flask OrangePi.GPIO
sudo flask run --host=0.0.0.0
```

