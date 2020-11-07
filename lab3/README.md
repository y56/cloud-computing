term 1

    `sudo mn --custom topology.py --topo mytopo --mac --arp --switch ovsk --controller remote`

term 2

    `sh ./flow.sh`

term 2

    `ryu-manager --verbose sample_code.py`

    if get error:
        `OSError: [Errno 98] Address already in use`
    then:
        `sudo lsof -i :6653`
        `sudo kill that_pid`

    again, `ryu-manager --verbose sample_code.py`
    wait patiently on `move onto main mode`


sudo ovs-ofctl -O openflow13 dump-flows s1

# code skeleton

sample-code-modified.py
    from classmate

sample_code.py
    from course

testarp.py
    from RyuBook(zh-TW)

