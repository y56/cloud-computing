sudo ovs-ofctl add-flow s1 in_port=1,tp_dst=80,dl_type=0x0800,nw_proto=6,actions:output=2
sudo ovs-ofctl add-flow s1 in_port=3,tp_dst=80,dl_type=0x0800,nw_proto=6,actions:output=1
sudo ovs-ofctl add-flow s1 in_port=3,actions:output=1
sudo ovs-ofctl add-flow s1 in_port=1,actions:output=3
sudo ovs-ofctl add-flow s2 in_port=2,tp_dst=80,dl_type=0x0800,nw_proto=6,actions:output=3
sudo ovs-ofctl add-flow s2 in_port=3,actions:output=1
sudo ovs-ofctl add-flow s4 in_port=3,tp_dst=80,dl_type=0x0800,nw_proto=6,actions:output=1
sudo ovs-ofctl add-flow s4 in_port=1,tp_dst=80,dl_type=0x0800,nw_proto=6,actions:output=5
sudo ovs-ofctl add-flow s4 in_port=4,actions:output=1
sudo ovs-ofctl add-flow s4 in_port=1,actions:output=3
sudo ovs-ofctl add-flow s3 in_port=5,tp_dst=80,dl_type=0x0800,nw_proto=6,actions:output=3
sudo ovs-ofctl add-flow s3 in_port=3,actions:output=2
sudo ovs-ofctl add-flow s3 in_port=2,actions:output=3
sudo ovs-ofctl add-flow s5 in_port=2,actions:output=4
sudo ovs-ofctl add-flow s5 in_port=1,actions:output=2

