# run

     alias mmm='sudo mn --custom topology.py --topo mytopo --mac --switch ovsk --controller remote'
     alias rrr='sh flow.sh && ryu-manager controller-lab3.py'

# trouble shooting
    if get error:
        `OSError: [Errno 98] Address already in use`
    then:
        `sudo lsof -i :6653`
        `sudo kill that_pid`

    again, `ryu-manager --verbose sample_code.py`
    wait patiently on `move onto main mode`

# to read flow table
sudo ovs-ofctl -O openflow13 dump-flows s1

# code skeleton reference

sample-code-modified.py
    from classmate

sample_code.py
    from course

testarp.py
    from RyuBook(zh-TW)

# reference
https://gist.github.com/aweimeow/d3662485aa224d298e671853aadb2d0f

# don't print multicast

# ping all 
h4 ping -c1 h1 && ping -c1 h2 && ping -c1 h3 && ping -c1 h4

# udp test

y56:~$ nc -z -v -u 192.168.1.2 123
Connection to 192.168.1.2 123 port [udp/ntp] succeeded!

y56:~$ nc -z -v -u ptt.cc 123
Connection to ptt.cc 123 port [udp/ntp] succeeded!

this will send 5 udp packets

## send only one packet

xterm h1 
    nc -l -u 22 // to listen to udp port 22


# tcp test
xterm h2
inside h2: nc -l 22 // netcat listen to 22
inside mininet
nc -z -v ptt.cc 22
// Connection to ptt.cc 22 port [tcp/ssh] succeeded!
We can see from the printout that tcp packet are passed clockwise and switch learned rules.

# xterm too small
https://askubuntu.com/questions/621176/why-are-the-characters-in-xterm-so-small-and-how-do-i-change-it

nano ~/.Xresources

xterm*faceName: Ubuntu Mono:style=Regular:antialias=true
xterm*faceSize: 12
XTerm*Background: black
XTerm*Foreground: grey

xrdb -I$HOME ~/.Xresources


# test tool
## arp: arping
* h1 arping h2
* h1 arp -a // show arp table
## icmp: ping/pingall
* pingall
* h1 ping h2
## tcp/udp: nc (netcat) or iperf
### iperf
* in xterm of host A: as server: iperf  -s (-u) -p
* in xterm of host B: as server: iperf  -c  dst_IP (-u) -p
### netcat
* nc -l (-u) 22 // to listen as server
* nc -z -v -u dst_IP port_number // -v for verbose // -z for not containing data
## http: (ie tcp@8080)
### iperf
* in xterm of host A: as server: iperf  -s (-u) -p
* in xterm of host B: as server: iperf  -c  dst_IP (-u) -p

