# NixOS remote builder using AWS

## Pain points

- School homeworks requires building >50 packages because for some reasons they are not cached.
- It made my laptop burn.
- Why not take this load elsewhere ? I don't want to buy a new laptop.
- NixOS seemed really appropriate for this (spoiler: it is).

## Solution

### AWS

This is what I use on AWS:

- EC2 c5.large instance.
- 15 Go of storage.
- 120 to 200 euros per year if used 2h a day 5 days a week.

### Your computer

Add this in the NixOS configuration:

```nix
nix.buildMachines = [{
    hostName = "builder";
    system = "x86_64-linux";
    maxJobs = 2;
    speedFactor = 2;
    supportedFeatures = [];
    mandatoryFeatures = [];
}];

nix.distributedBuilds = true;

nix.extraOptions = ''
    builders-use-substitutes = true
'';
```

And this in the /root/.ssh/config.
You may need to change it if your instance's IP changes.

```ssh-config
Host builder
    HostName <Your EC2 instance public IP>
    User root
    IdentityFile ~/.ssh/<Your .pem file>
```

Add the `.pem` file AWS gave you to connect via ssh to the instance in the `/root/.ssh` directory.

## Resources

[Building on remote servor for NixOS on RaspberryPI - Blog post](https://eipi.xyz/blog/building-on-remote-server-for-nixos-on-raspberry-pi/)

[Access EC2 via SSH - AWS Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
