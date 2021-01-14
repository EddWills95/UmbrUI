## UmbrUI (Umb-roo-eee)
### [Umbrel](https://github.com/getumbrel/umbrel) UI developed for 3.5" GPIO screens

- Intended to be run as part of the Umbrel App system (hence the docker-compose)
- See [Renderer](https://github.com/EddWills95/UmbrUI-Renderer) for SPI screen image

Milestones:
- [x] Use SPI screen without needing higher privileges
- [x] Connect to BTC & LND services
- [ ] Allow user to set screen size
- [ ] Allow user to chose what is displayed
- [x] Shutdown script to blank out screen on uninstall / shutdown

The goal is to be able to present the user with some helpful information such as: 
- [x] IP address 
- [x] TOR address 
- [x] QR Code to link to url
- [ ] Funds Status
- [ ] How many channels
- [x] Forwards in the last 24hrs
- [x] Sync status

Early doors figma: https://www.figma.com/file/nPWWBp3BCrX71FmxRNnj1M/UmbrUI?node-id=0%3A1

We can go the Raspiblitz route and add some touchscreen functionality but for now I think this should focus on presenting some basic data to allow the user to get up and running.

On Pi:
```
python3 ui.py
```

The googleapis submodule is only needed for the generation of some python files.
You don't need it normally while using or developing this app, except when adding a new feature that requires a newer version of LND.
If that's the case, first update the rpc.proto to the version from the latest LND, then run:
```
python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=. --grpc_python_out=. rpc.proto
```

Please not that you need to have grpcio-tools installed to do this.

rpc.proto is available at https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto.
Please don't use the file from a later version of LND than the one currently used in Umbrel to avoid issues.
