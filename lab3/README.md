# term 1

    `sudo mn --custom topology.py --topo mytopo --mac --arp --switch ovsk --controller remote`

# term 2

    `sh ./flow.sh`

# term 2

    `ryu-manager --verbose sample_code.py`
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
