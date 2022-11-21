# Setting up the raspi

## SSH

Do the raspi shady things with the ssh folder.
Then configure ssh properly.

*/etc/ssh/sshd_config*
```
PubkeyAuthentication yes
PasswordAuthentication no
```

Add your public key to `~/.ssh/authorized_keys` (you can transfer it with scp and then cat it in the file).

Restart the sshd service (not sure if necessary): `sudo systemctl restart sshd`.

## Auto update

See (this link)[https://wiki.debian.org/UnattendedUpgrades] for more info.

```
sudo apt install unattended-upgrades apt-listchanges
```

Uncomment the following line to make it work with apt-listchanges:

*/etc/apt/apt.conf.d/50unattended-upgrades*
```
Unattended-Upgrade::Mail "root";
Unattended-Upgrade::MailOnlyOnError "false";
```

Uncomment the following lines to make sure unattended-upgrade is correctly activated.

*/etc/apt/apt.conf.d/20auto-upgrades*
```
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```

If it does not exist, should run `dpkg-reconfigure -plow unattended-upgrades`

Receive mail with listchanges.

*/etc/apt/listchanges.conf*
```
[apt]
frontend=pager
email_address=root
confirm=0
save_seen=/var/lib/apt/listchanges.db
which=both
```

## Install mosquitto (MQTT broker)

Install with `sudo apt install mosquitto`.

Create and edit conf file:

*/etc/mosquitto/conf.d/server.conf*
```
allow_anonymous false
password_file /etc/mosquitto/passwd.txt
user mosquitto
listener 1883 0.0.0.0
```

Add an user `sudo mosquitto_passwd -c /etc/mosquitto/passwd.txt coco`.

## MQTT Host and Wake On Lan script

For now using a Python script.

Install Paho MQTT library for Python: `pip3 install paho`

Run the script on startup with systemd for exemple (beware to install the paho module for the root user if you wish to use systemd).

## TODO

Use mosquitto-tls to encrypt the connection.
