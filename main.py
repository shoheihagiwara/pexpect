#!/usr/bin/env python

import pexpect

child = pexpect.spawn('/bin/bash -c "ps aux | grep usr/bin/dbus"')
index = child.expect([pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
    print("index: 0(EOF)")
    print("----------")
    print("child.before(bytes): " + str(child.before))
    print("----------")
    print("child.before(decoded): " + child.before.decode())
elif index == 1:
    print("index: 1(TIMEOUT)")
    print("----------")
    print("child.before(bytes): " + str(child.before))
    print("----------")
    print("child.before(decoded): " + child.before.decode())
child.close()
