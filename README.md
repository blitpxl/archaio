# About
Archaio is an application used for generating test files which is used to test
the capacity of a USB drive. Archaio will generate `.aio` file which is
essentially a text file containing millions of `1`.

# How does it work?
The integer `1` occupy 1 byte in disk space, Archaio will write millions of `1`
into a text file using a loop, the loop will breaks once the threshold attained.
to achieve certain file size, we can manually set the threshold. In one loop Archaio will
write exactly `1,000 bytes `(1kb), we can set how many time Archaio will loop, say we want 10MB file
which is `10,240,000 bytes` (10 million), so we set a limit to the loop so it will only loops `10240` times
and not `1024000` because Archaio will write `1,000 bytes` per loop not `1 byte` per loop. the code below will make it clearer:

* [![KC6qU7.md.png](https://iili.io/KC6qU7.md.png)](https://freeimage.host/i/KC6qU7)

* [![KC6flS.png](https://iili.io/KC6flS.png)](https://freeimage.host/)

# Speed & Performance

The test was performed on a rig with:
* Intel Core i5 3470
* 8GB HyperX DDR3
* SSD Gamer Galax 120GB

Peak Maximum Speed: 251 Mb/s

|Size|Time |
|----|-----|
|10MB|0.11s|
|50MB|0.56s|
|100MB|1.11s|
|500MB|5.37s|
|1GB|10.6s|
|5GB|53.4s|
|10GB|105.2s
`NOTE: The performance will vary depending on the hardware
you are running on. It can be also limited by the USB drive's bandwidth
or its maximum Transfer Speed.`
