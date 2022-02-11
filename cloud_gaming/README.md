# Cloud Gaming at home

## My situation

- An expensive gaming rig at home.
- I am always away from home.
- I want to play Minecraft, The Wither or any Steam games with good quality.
- My laptop is a potato.

## Iteration 1

### Solution

- Use [Parsec](https://parsec.app/).

### Deployement

- Install Parsec on my gaming rig as host and
  on my laptop as client (there is a AUR package).
- Find the best settings and driver.

### Results

- Need to lower the graphics in order for the stream to not freeze in some
  games (like The Witcher 3).
- Overall playable for solo games, trickier for online games.

### Problems

- I don't know when exactly I'll want to play,
  so I can't power on my pc in advance.
- I also don't want my gaming pc to be always turned on.

## Iteration 2

### Solution

- Use a **Raspi** with both a Wifi and Ethernet interface
  to **wake-on-lan** my gaming pc on-demand.
- A way to communicate to the Raspi:
  - Using a free **RabbitMQ** service, without
    having to open ports.

### Deployement

*Every operation below on the Raspi (host) should be done as root in order to*
*invoke the etherwake command*

- Get a [free RabbitMQ](https://www.cloudamqp.com/) service running.
- Install **pika** python lib: `pip3 install pika`.
- Install etherwake package on the Raspi.
- Connect the Raspi to internet by wifi and to your gaming pc with ethernet.
- Get your PC's ethernet port mac address.
- Use the client and host scripts.
- Configure Windows to boot without password.
- Enjoy

### Resources

- https://www.instructables.com/Raspberry-Pi-As-Wake-on-LAN-Server/#:~:text=Open%20Network%20settings%20and%20go,and%20to%20enable%20Magic%20Packet.

## Iteration 3

### Solution

- Create a **VPN** connection to my home
  and ssh to the raspi to send the wake-on-lan packet.
