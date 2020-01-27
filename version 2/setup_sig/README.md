# Establishing SCION IP Gateway between two AS's

The [SCION IP Gateway `SIG`](https://github.com/netsec-ethz/netsec-scion/tree/scionlab/go/sig) enables legacy IP applications to communicate over SCION.

Here we are establishing a link through Scion IP Gateway between two dedicated Ubuntu 16.04 machines running Scion AS's.

## The Two ASes and ports used

### AS 1: 19-ffaa:1:bf9

IP for Sig to bind to: 172.16.0.11
IP net for communication: 172.16.11.0/24

### AS 2: 19-ffaa:1:cc5

IP for Sig to bind to: 172.16.0.12
IP net for communication: 172.16.12.0/24

## Build the sig binary (to be done on both machines)

Follow [scionproto README](https://github.com/netsec-ethz/netsec-scion/) till step 6 to download the source code of scion.

Run the following to build scion binaries.

```shell
./scion.sh build
```

Make sure that you are in the directory of the scion source code.
Copy the sig binary to /usr/bin/:

```shell
sudo cp bin/sig /usr/bin/sig
```

## Configuring AS 1: 19-ffaa:1:bf9

We will create the folder and configuration files for the Sig.
Run the following commands to create the necessary folder.

```shell
sudo mkdir  /etc/scion/gen/ISD19/ASffaa_1_bf9/sig19-ffaa_1_bf9
cd /etc/scion/gen/ISD19/ASffaa_1_bf9/sig19-ffaa_1_bf9
```

Now we will create the sig.config and sig.json files.

```shell
sudo nano sig.config
```

Paste the following into sig.config and save the file.

```
[features]
    # Feature flags are various boolean properties as defined in go/lib/env/features.go

[logging]
    [logging.file]
        # Location of the logging file. If not specified, logging to file is disabled.
        Path = "/var/log/scion/sig.log"

        # File logging level. (trace|debug|info|warn|error|crit) (default debug)
        Level = "debug"

        # Max size of log file in MiB. (default 50)
        Size = 50

        # Max age of log file in days. (default 7)
        MaxAge = 7

        # Maximum number of log files to retain. (default 10)
        MaxBackups = 10

        # How frequently to flush to the log file, in seconds. If 0, all messages
        # are immediately flushed. If negative, messages are never flushed
        # automatically. (default 5)
        FlushInterval = 5

    [logging.console]
        # Console logging level (trace|debug|info|warn|error|crit) (default crit)
        Level = "crit"

[metrics]
    # The address to export prometheus metrics on (host:port or ip:port or :port).
    # If not set, metrics are not exported. (default "")
    Prometheus = "127.0.0.1:30456"

[sd_client]
    # The Sciond path. (default sciond.DefaultSCIONDPath)
    Path = "/run/shm/sciond/default.sock"

    # Maximum time spent attempting to connect to sciond on start. (default 20s)
    InitialConnectPeriod = "20s"

[sig]
    # ID of the SIG. (required)
    ID = "sig19-ffaa_1_bf9"

    # The SIG config json file. (required)
    SIGConfig = "/etc/scion/gen/ISD19/ASffaa_1_bf9/sig19-ffaa_1_bf9/sig.json"

    # The local IA. (required)
    IA = "19-ffaa:1:bf9"

    # The bind IP address. (required)
    IP = "172.16.0.11"

    # Control data port, e.g. keepalives. (default 30256)
    CtrlPort = 30256

    # Encapsulation data port. (default 30056)
    EncapPort = 30056

    # SCION dispatcher path. (default "")
    Dispatcher = ""

    # Name of TUN device to create. (default DefaultTunName)
    Tun = "sig"

    # Id of the routing table. (default 11)
    TunRTableId = 11
```

```shell
sudo nano sig.json
```

Paste the following into sig.json and save the file.

```
{
    "ASes": {
        "19-ffaa:1:cc5": {
            "Nets": [
                "172.16.12.0/24"
            ]
        }
    },
    "ConfigVersion": 1
}
```

Edit all the topology.json files in the subfolders of /etc/scion/gen/ and paste the following to the top of the json file after '{' and save the files.

```
"SIG": {
    "sig19-ffaa_1_bf9": {
      "Addrs": {
        "IPv4": {
          "Public": {
            "Addr": "172.16.0.11",
            "L4Port": 31056
          }
        }
      }
    }
  },
```

## Configuring AS 2: 19-ffaa:1:cc5

We will create the folder and configuration files for the Sig.
Run the following commands to create the necessary folder.

```shell
sudo mkdir  /etc/scion/gen/ISD19/ASffaa_1_cc5/sig19-ffaa_1_cc5
cd /etc/scion/gen/ISD19/ASffaa_1_cc5/sig19-ffaa_1_cc5
```
Now we will create the sig.config and sig.json files.

```shell
sudo nano sig.config
```

Paste the following into sig.config and save the file.

```
[features]
    # Feature flags are various boolean properties as defined in go/lib/env/features.go

[logging]
    [logging.file]
        # Location of the logging file. If not specified, logging to file is disabled.
        Path = "/var/log/scion/sig.log"

        # File logging level. (trace|debug|info|warn|error|crit) (default debug)
        Level = "debug"

        # Max size of log file in MiB. (default 50)
        Size = 50

        # Max age of log file in days. (default 7)
        MaxAge = 7

        # Maximum number of log files to retain. (default 10)
        MaxBackups = 10

        # How frequently to flush to the log file, in seconds. If 0, all messages
        # are immediately flushed. If negative, messages are never flushed
        # automatically. (default 5)
        FlushInterval = 5

    [logging.console]
        # Console logging level (trace|debug|info|warn|error|crit) (default crit)
        Level = "crit"

[metrics]
    # The address to export prometheus metrics on (host:port or ip:port or :port).
    # If not set, metrics are not exported. (default "")
    Prometheus = "127.0.0.1:30456"

[sd_client]
    # The Sciond path. (default sciond.DefaultSCIONDPath)
    Path = "/run/shm/sciond/default.sock"

    # Maximum time spent attempting to connect to sciond on start. (default 20s)
    InitialConnectPeriod = "20s"

[sig]
    # ID of the SIG. (required)
    ID = "sig19-ffaa_1_cc5"

    # The SIG config json file. (required)
    SIGConfig = "/etc/scion/gen/ISD19/ASffaa_1_cc5/sig19-ffaa_1_cc5/sig.json"

    # The local IA. (required)
    IA = "19-ffaa:1:cc5"

    # The bind IP address. (required)
    IP = "172.16.0.12"

    # Control data port, e.g. keepalives. (default 30256)
    CtrlPort = 30256

    # Encapsulation data port. (default 30056)
    EncapPort = 30056

    # SCION dispatcher path. (default "")
    Dispatcher = ""

    # Name of TUN device to create. (default DefaultTunName)
    Tun = "sig"

    # Id of the routing table. (default 11)
    TunRTableId = 11
```

```shell
sudo nano sig.json
```

Paste the following into sig.json and save the file.

```json
{
    "ASes": {
        "19-ffaa:1:bf9": {
            "Nets": [
                "172.16.11.0/24"
            ]
        }
    },
    "ConfigVersion": 1
}
```

Edit all the topology.json files in the subfolders of /etc/scion/gen/ and paste the following to the top of the json file after '{' and save the files.

```json
"SIG": {
    "sig19-ffaa_1_cc5": {
      "Addrs": {
        "IPv4": {
          "Public": {
            "Addr": "172.16.0.12",
            "L4Port": 31056
          }
        }
      }
    }
  },
```

## Create the service for Sig and configure routing and dummy interfaces

Now we will create the service on both machines for starting Sig when scion starts.

```shell
sudo nano /lib/systemd/system/scion-ip-gateway@.service
```

Paste the following into the file and save it.

```
[Unit]
Description=SCION IP Gateway
Documentation=https://www.scionlab.org
After=network-online.target scion-dispatcher.service
Wants=network-online.target
PartOf=scionlab.target

[Service]
Type=simple
User=scion
Group=scion
ExecStart=/usr/bin/scion-systemd-wrapper /usr/bin/sig /etc/scion/gen/ISD-isd-/AS-as-/sig%i/sig.config %i
RemainAfterExit=False
KillMode=control-group
Restart=on-failure

[Install]
WantedBy=scionlab.target
```

Now we will create the script to configure routing and dummy interfaces for sig

```shell
sudo nano /etc/scion/preSigConfig.sh
```

On AS 1: 19-ffaa:1:bf9 paste the following and save the file.

```
#!/bin/bash
sudo setcap cap_net_admin+eip /usr/bin/sig
sudo sysctl net.ipv4.conf.default.rp_filter=0
sudo sysctl net.ipv4.conf.all.rp_filter=0
sudo sysctl net.ipv4.ip_forward=1
sudo modprobe dummy
sudo ip link add dummy11 type dummy
sudo ip addr add 172.16.0.11/32 brd + dev dummy11
sudo ip link add sigIF type dummy
sudo ip addr add 172.16.11.1/24 brd + dev sigIF
sudo ifconfig sigIF up
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
```

On AS 2: 19-ffaa:1:cc5 paste the following and save the file.

```
#!/bin/bash
sudo setcap cap_net_admin+eip /usr/bin/sig
sudo sysctl net.ipv4.conf.default.rp_filter=0
sudo sysctl net.ipv4.conf.all.rp_filter=0
sudo sysctl net.ipv4.ip_forward=1
sudo modprobe dummy
sudo ip link add dummy12 type dummy
sudo ip addr add 172.16.0.12/32 brd + dev dummy12
sudo ip link add sigIF type dummy
sudo ip addr add 172.16.12.1/24 brd + dev sigIF
sudo ifconfig sigIF up
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
```

```shell
sudo nano /etc/scion/postSigConfig.sh
```

On AS 1: 19-ffaa:1:bf9 paste the following and save the file.

```
#!/bin/bash
sudo ip route add 172.16.12.0/24 dev sig src 172.16.11.1 metric 100
```

On AS 2: 19-ffaa:1:cc5 paste the following and save the file.

```
#!/bin/bash
sudo ip route add 172.16.11.0/24 dev sig src 172.16.12.1 metric 100
```

Add permission for execution to the script

```shell
sudo chmod +x /etc/scion/preSigConfig.sh
sudo chmod +x /etc/scion/postSigConfig.sh
```

Now we will create a service on both machines that will run the above scripts upon startup.

```shell
sudo nano /lib/systemd/system/preSigConfig.service
```

Paste the following and save the file.

```
[Unit]
 Description=Configuration before staring SiG
 After=network-online.target
 Wants=network-online.target
 Before=scionlab.target

[Service]  
 Type=oneshot
 ExecStart=/etc/scion/preSigConfig.sh
 Restart=no

[Install]
 WantedBy=multi-user.target
```

```shell
sudo nano /lib/systemd/system/postSigConfig.service
```

Paste the following and save the file.

```
[Unit]
 Description=Configuration after staring SiG
 After=scionlab.target systemctl is-active sys-devices-virtual-net-sig.device

[Service]
 Type=oneshot
 ExecStartPre=/bin/bash -c "systemctl is-active sys-devices-virtual-net-sig.device"
 ExecStart=/etc/scion/postSigConfig.sh
 

[Install]
 WantedBy=multi-user.target
```

## Enable services

Now we will enable the services that we created.

```shell
sudo systemctl daemon-reload
sudo systemctl enable preSigConfig.service
sudo systemctl enable postSigConfig.service
```

On AS 1:

```shell
sudo systemctl enable scion-ip-gateway@19-ffaa_1_bf9.service
```

On AS 2:

```shell
sudo systemctl enable scion-ip-gateway@19-ffaa_1_cc5.service
```

Start the services on both machines

```shell
sudo systemctl start preSigConfig.service
sudo systemctl restart scionlab.target
sudo systemctl start postSigConfig.service
```

Now every time the machines are started, sig should be running alongside scion.

To check if all scion services are running:

```shell
sudo systemctl list-dependencies scionlab.target
```

If some services are not running, try:

```shell
sudo systemctl restart scionlab.target
sudo systemctl restart postSigConfig.service
```

## Testing the connection

To test the sig connection run the following on AS 1:

```shell
ping 172.16.12.1
```

If the setup was successful, the ping should be successful.

If the ping is unsuccessful, make sure that the time zone is UTC and the date and time are correct on both machines.
