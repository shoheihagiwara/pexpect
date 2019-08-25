#!/usr/bin/env python

import pexpect

password="XXXXXXXXX"

child = pexpect.spawn('ssh -p8222 shohei@localhost "ps aux | grep usr/bin/dbus"')
index = child.expect([pexpect.EOF, pexpect.TIMEOUT, "[Pp]assword: "])
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
elif index == 2:
    print("Password detected.")
    print("child.before(bytes): " + str(child.before))

    print("sending password: {}".format(password))
    child.sendline(password)

    print("expecting EOF")
    child.expect(pexpect.EOF)
    print("detected EOF")
    print("----------")
    print("child.before(bytes): " + str(child.before))
    print("----------")
    print("child.before(decoded): " + child.before.decode())
    if len(child.before.decode()) > 0:
        print("process runnning. OK")
child.close()
