Use Raspberry Pi to control LEGO Mindstorms NXT brick with python
=================================================================

Establish bluetooth connection between RPi and NXT
==================================================

rpi 3 has bluetooth built in
----------------------------

install bluetooth libraries

<https://gist.github.com/lexruee/fa2e55aab4380cf266fb>

sudo apt-get update sudo apt-get install python-pip python-dev ipython

sudo apt-get install bluetooth libbluetooth-dev sudo pip install pybluez

sudo apt install bluez\*

pair the NXT mindstorm device
-----------------------------

sudo bluetoothctl -a

### Do this to search for the device:

    [bluetooth]# scan on
    Discovery started
    [CHG] Controller B8:27:EB:84:19:D6 Discovering: yes
    [NEW] Device 00:16:53:17:52:EE 00-16-53-17-52-EE
    [CHG] Device 00:16:53:17:52:EE LegacyPairing: no
    [CHG] Device 00:16:53:17:52:EE Name: JAWS
    [CHG] Device 00:16:53:17:52:EE Alias: JAWS

### Do this to pair the device once the ID is found

\[bluetooth\]\# pair 00:16:53:17:52:EE Attempting to pair with
00:16:53:17:52:EE Failed to pair: org.bluez.Error.AuthenticationTimeout

### Look at NXT screen for code and press the orange button

acknowledge, use that code to pair.

\[bluetooth\]\# pair 00:16:53:17:52:EE Attempting to pair with
00:16:53:17:52:EE Request PIN code \[agent\] Enter PIN code: 1234
\[CHG\] Device 00:16:53:17:52:EE Connected: yes \[CHG\] Device
00:16:53:17:52:EE UUIDs: 00001101-0000-1000-8000-00805f9b34fb \[CHG\]
Device 00:16:53:17:52:EE ServicesResolved: yes \[CHG\] Device
00:16:53:17:52:EE Paired: yes Pairing successful \[CHG\] Device
00:16:53:17:52:EE ServicesResolved: no \[CHG\] Device 00:16:53:17:52:EE
Connected: no \[CHG\] Device 00:16:53:17:52:EE RSSI: -51 \[CHG\] Device
00:16:53:17:52:EE RSSI: -36

set up python software
======================

nxt-python
----------

<https://github.com/Eelviny/nxt-python/tree/master>

must use python 2 and tag v2.2.2 do not use master branch to build will
not work with python3

use: git checkout v2.2.2

test if things work
-------------------

<https://onegoodapp.wordpress.com/2013/07/02/raspberry-pi-model-b-setup-to-communicate-with-nxt/>

wget <http://home.wlu.edu/~levys/courses/csci250s2013/nxt_beep.py>

run python nxt~beep~.py and the nxt should beep if things work. I had to
turn on the volume on the nxt brick first.

ideas
=====

<https://rebeccaajones.wordpress.com/2013/06/19/raspberry-pi-robotics-part-1-pi-controlling-the-nxt/>
<http://www.nxtprograms.com/castor_bot/steps.html>
<http://www.raspberry-pi-geek.com/Archive/2015/10/Build-cool-stuff-with-Lego-and-Pi>
