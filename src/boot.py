import poll


def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    import utime
    first_try = utime.time()
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WiFi SSID', 'WiFI Pass')
        while not sta_if.isconnected():
            if utime.time() - first_try <= 5:
                pass
            else:
                print('Coudnt connect to network')
                import sys
                sys.exit()
                break
    print('network config: ', sta_if.ifconfig())


def no_debug():
    import esp
    esp.osdebug(None)


no_debug()
connect()
poll.start_server()
