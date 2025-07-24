
Video: https://www.youtube.com/watch?v=q8--R7O2GRA&list=PLm7Cwn08hhZWhPp6W7Ok0ksr4yFI4DLsf&ab_channel=InstitutefortheWirelessInternetofThings


## Core SRN with image `oai-5gcn`
```
cd oai-cn5g-fed/docker-compose
./core-network.sh start nrf spgwu
colosseumcli rf start -c 10011
```

After a UE registers with the core network and is assigned an IP address, run
the following command on the host running the core network containers to set a 
route towards the UE:
```
route add -net 12.1.1.0/24 gw 192.168.70.134 dev demo-oai
```


## RAN SRN with image `oai-5g-sa-ran` or `oai-gnb-e2agent`
Change `numactl --cpunodebind=netdev:usrp0 --membind=netdev:usrp0 ./nr-softmodem <command line options>` in `sa_gnb_run.sh`

to `numactl --cpunodebind=1 --membind=1 ./nr-softmodem <command line options>`
```
sed -i 's|numactl --cpunodebind=netdev:usrp0 --membind=netdev:usrp0|numactl --cpunodebind=1 --membind=1|g' sa_gnb_run.sh
./sa_gnb_run.sh
```

## UE SRN with image `oai-5g-sa-ran`
Change `numactl --cpunodebind=netdev:usrp0 --membind=netdev:usrp0 ./nr-softmodem <command line options>` in `sa_nrue_run.sh`

to `numactl --cpunodebind=1 --membind=1 ./nr-softmodem <command line options>`
```
sed -i 's|numactl --cpunodebind=netdev:usrp0 --membind=netdev:usrp0|numactl --cpunodebind=1 --membind=1|g' sa_nrue_run.sh
./sa_nrue_run.sh
```

In SA mode, after UE is assigned an IP address and before starting user-plane
traffic, use the following command to set the default route at host running UE
to route the traffic through OAI core network.
```
route add default gw 12.1.1.1
```

## Iperf
### On UE side:
```
iperf -s -i 1 -u -B 12.1.1.2
```

UE ip: `12.1.1.2`

To check UE ip `ifconfig oaitun_ue1`

### On Core side:
```
iperf -c 12.1.1.2 -u -b 1M --bind 192.168.136.1
```

The ip is `192.168.<SRN ID + 100>.1`
