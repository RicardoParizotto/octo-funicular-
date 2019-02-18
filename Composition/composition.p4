
            parser MyParser( {

 state start { 
} state parse_ipv4 { 

                    {'default': 'accept', 'hdr.ipv4.protocol) {\n            6': 'parse_tcp'};
                    {'default': 'accept', 'hdr.ipv4.protocol) {\n            6': 'parse_tcp'};} state parse_tcp { 
} state parse_ethernet { 

                    {'default': 'accept', 'hdr.ethernet.etherType) {\n            0x800': 'parse_ipv4'};
                    {'default': 'accept', 'hdr.ethernet.etherType) {\n            0x800': 'parse_ipv4'};}}


control MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {
            action drop() {
        mark_to_drop();
    }

action set_ecmp_select(bit<16> ecmp_base, bit<32> ecmp_count) {
        /* TODO: hash on 5-tuple and save the hash result in meta.ecmp_select 
           so that the ecmp_nhop table can use it to make a forwarding decision accordingly */
    }

action set_nhop(bit<48> nhop_dmac, bit<32> nhop_ipv4, bit<9> port) {
        hdr.ethernet.dstAddr = nhop_dmac;
        hdr.ipv4.dstAddr = nhop_ipv4;
        standard_metadata.egress_spec = port;
        hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
    }

action rewrite_mac(bit<48> smac) {
        hdr.ethernet.srcAddr = smac;
    }

action drop() {
        mark_to_drop();
    }

action drop() {
        mark_to_drop();
    }

action set_ecmp_select(bit<16> ecmp_base, bit<32> ecmp_count) {
        /* TODO: hash on 5-tuple and save the hash result in meta.ecmp_select 
           so that the ecmp_nhop table can use it to make a forwarding decision accordingly */
    }

action set_nhop(bit<48> nhop_dmac, bit<32> nhop_ipv4, bit<9> port) {
        hdr.ethernet.dstAddr = nhop_dmac;
        hdr.ipv4.dstAddr = nhop_ipv4;
        standard_metadata.egress_spec = port;
        hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
    }

action set_chaining(egressSpec_t prog){
         meta.context_control = 1;
         meta.extension_id1 = prog;
        } table ecmp_group{
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            drop;
            set_ecmp_select;
        }
        size = 1024;
    }

table ecmp_nhop{
        key = {
            meta.ecmp_select: exact;
        }
        actions = {
            drop;
            set_nhop;
        }
        size = 2;
    }

table send_frame{
        key = {
            standard_metadata.egress_port: exact;
        }
        actions = {
            rewrite_mac;
            drop;
        }
        size = 256;
    }

table ecmp_group{
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            drop;
            set_ecmp_select;
        }
        size = 1024;
    }

table ecmp_nhop{
        key = {
            meta.ecmp_select: exact;
        }
        actions = {
            drop;
            set_nhop;
        }
        size = 2;
    }

table shadow{
           key = {
              hdr.ethernet.dstAddr: lpm;
           }
           actions = {
               set_chaining;
               NoAction;
           }
           size = 1024;
           default_action = NoAction();
        }

}