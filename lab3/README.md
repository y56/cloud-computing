# run

     sudo mn --custom topology.py --topo mytopo --mac --switch ovsk --controller remote
     sh flow.sh && ryu-manager controller-lab3.py

# trouble shooting

    if get error:
        `OSError: [Errno 98] Address already in use`
    then:
        `sudo lsof -i :6653`
        `sudo kill that_pid`
    
    // this is bc port:6653 for ryu is occupied 
    
    again, `ryu-manager --verbose sample_code.py`
    wait patiently on `move onto main mode`

# to read flow table

sudo ovs-ofctl -O openflow13 dump-flows s1

# code skeleton reference

sample-code-modified.py

* from classmate

sample_code.py

* from course

sample-code_ryubook.py

* from RyuBook(zh-TW)

# reference

https://gist.github.com/aweimeow/d3662485aa224d298e671853aadb2d0f

# don't print multicast

those packets to dst mac as 33:xxxx

# ping all 

h4 ping -c1 h1 && ping -c1 h2 && ping -c1 h3 && ping -c1 h4

pingall

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
    * this will send 5 udp packets
## http: (ie tcp@8080)
### iperf
* in xterm of host A: as server: iperf  -s (-u) -p
* in xterm of host B: as server: iperf  -c  dst_IP (-u) -p

