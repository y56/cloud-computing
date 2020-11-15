# to start mininet
sudo mn --custom topo-5sw-2host.py --topo mytopo --controller remote
# to install rules
sh rules.sh
# to start mininet with fat-tree topology
sudo mn --custom fat-tree.py --topo mytopo --controller remote
