## UmbrUI (Umb-roo-eee)
### [Umbrel](https://github.com/getumbrel/umbrel) UI developed for 3.5" GPIO screens

- Intended to be run as part of the Umbrel App system (hence the docker-compose)
- See [Renderer](https://github.com/EddWills95/UmbrUI-Renderer) for SPI screen image

Milestones:
- [x] Use SPI screen without needing higher privileges
- [ ] Connect to BTC & LND services
- [ ] Allow user to set screen size
- [ ] Allow user to chose what is displayed
- [ ] Shutdown script to blank out screen on uninstall / shutdown

The goal is to be able to present the user with some helpful information such as: 
- [x] IP address 
- [x] TOR address 
- [x] QR Code to link to url
- [ ] Funds Status
- [ ] How many channels
- [ ] Forwards in the last 24hrs
- [ ] Sync status

Early doors figma: https://www.figma.com/file/nPWWBp3BCrX71FmxRNnj1M/UmbrUI?node-id=0%3A1

We can go the Raspiblitz route and add some touchscreen functionality but for now I think this should focus on presenting some basic data to allow the user to get up and running.

To run localy (within X / mac):
```
NOTPI=true python3 ui.py
```

On Pi:
```
python3 ui.py
```

