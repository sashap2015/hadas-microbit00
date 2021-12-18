def onEvery_interval():
    mypause = 45
    basic.show_string("HA")
    basic.pause(mypause)
    basic.show_string("DA")
    basic.pause(mypause)
    basic.show_string("S")
    pass
loops.every_interval(500, onEvery_interval)

