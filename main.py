from time import sleep
from threading import Event
import pygame

from umbrui import UmbrUI
from lib.btc import BtcRPC

exit = Event()


def main():
    umbrui = UmbrUI()
    locked = True
    first_load = True

    while not exit.is_set():
        if locked:
            try:
                # Test connection to BTC (by extension LND)
                locked = umbrui.btc_rpc.connection_locked()
            except Exception:
                print(
                    "Please make sure BITCOIN_RPC_PORT, BITCOIN_RPC_PASS, BITCOIN_IP and BITCOIN_RPC_PORT are set and valid")
                # Show warning UI if can't connect
                umbrui.warnUI()

                # Wait and restart loop to wait for unlock
                sleep(10)
                continue

        if first_load:
            # If we're unlocked load main UI elements for first time
            umbrui.mainUI()
            first_load = False

        # Load refreshable elements and take screenshot
        umbrui.load_updatable_elements()

        # At most we should update every 10 seconds as it's expensive
        sleep(10)


def quit(signo, _frame):
    print("Interrupted by %d, shutting down" % signo)
    pygame.quit()
    exit.set()
    quit()


if __name__ == '__main__':

    import signal
    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit)

    main()
