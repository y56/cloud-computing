from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import arp
from ryu.lib.packet import ipv4
from ryu.lib.packet import tcp
from ryu.lib.packet import udp
from ryu.lib.packet import icmp


class SimpleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SimpleSwitch13, self).__init__(*args, **kwargs)

        self.ip2mac={
            '10.0.0.1': '10:00:00:00:00:01',
            '10.0.0.2': '10:00:00:00:00:02',
            '10.0.0.3': '10:00:00:00:00:03',
            '10.0.0.4': '10:00:00:00:00:04'
        }

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # install table-miss flow entry
        #
        # We specify NO BUFFER to max_len of the output action due to
        # OVS bug. At this moment, if we specify a lesser number, e.g.,
        # 128, OVS will send Packet-In with invalid buffer_id and
        # truncated packet data. In that case, we cannot output packets
        # correctly.  The bug has been fixed in OVS v2.1.0.
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]

        mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                    match=match, instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        # If you hit this you might want to increase
        # the "miss_send_length" of your switch
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']
        print('in_port', in_port)
        pkt = packet.Packet(msg.data)

        eth = pkt.get_protocol(ethernet.ethernet)

        dst = eth.dst
        src = eth.src

        pkt_arp = pkt.get_protocol(arp.arp)
        pkt_ipv4 = pkt.get_protocol(ipv4.ipv4)
        pkt_icmp = pkt.get_protocol(icmp.icmp)
        pkt_tcp = pkt.get_protocol(tcp.tcp)
        pkt_udp = pkt.get_protocol(udp.udp)

        # ARP
        if pkt_arp:
            print("[ARP] arrive at", datapath.id, dst)
            if pkt_arp.opcode != arp.ARP_REQUEST:
                return
            print('PEKO\n', pkt)
            # print('PEKO', pkt_arp)

            # dst_ip, dst_mac=ffffff
            mypkt = packet.Packet()
            mypkt.add_protocol(ethernet.ethernet(
                src=self.ip2mac[pkt_arp.dst_ip], # need to know the ip asked
                dst=src # eth src
            ))
            mypkt.add_protocol(arp.arp(
                #src_mac=self.ip2mac[pkt_arp.dst_ip], # 根据dst_ip得到的mac, # need to know the ip asked
                dst_mac=pkt_arp.src_mac,
                #src_ip=pkt_arp.dst_ip, # need to know the ip asked
                dst_ip=pkt_arp.src_ip,
                opcode=arp.ARP_REPLY,
                src_mac='10:00:00:00:00:02',
                src_ip='10.0.0.2'
            ))
            print('A\n', mypkt)
            self._send_packet(datapath, in_port, mypkt)

        else:
            print("ELSE\n")
            print(pkt)

        # # IPV4
        # elif pkt_ipv4:
        #     # ICMP
        #     if pkt_icmp:
        #         # calc out port
        #         out_port =
        #         # add flow
        #         match = parser.OFPMatch()
        #         actions = [parser.OFPActionOutput(port=out_port)]
        #         self.add_flow(datapath, 1, match, actions)
        #         # send packet
        #         self._send_msg(datapath, pkt, out_port)
        #     # TCP
        #     elif pkt_tcp:
        #         # HTTP RST
        #         if pkt_tcp.dst_port == 80 and (HOST2 or HOST4):
        #             # generate an HTTP RST packet
        #             # send packet
        #         # NON-TCP HTTP
        #         else:
        #             # calc out port
        #             # add flow
        #             # send packet
        #             # add http flow
        #     # UDP
        #     elif pkt_udp:
        #         if HOST1 or HOST4:
        #             # add drop flow
        #         else:
        #             # calc out port
        #             # add flow
        #             # send packet

    # def _send_msg(self, switch, pkt, out_port):
    #     return

    def _send_packet(self, datapath, port, pkt):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        pkt.serialize()
        # self.logger.info("LOG:: packet-out %s" % (pkt,))
        data = pkt.data
        actions = [parser.OFPActionOutput(port=port)]
        print("out:", port, "sw:", datapath.id)
        out = parser.OFPPacketOut(datapath=datapath,
                                  buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=ofproto.OFPP_CONTROLLER,
                                  actions=actions,
                                  data=data)
        datapath.send_msg(out)
