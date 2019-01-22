action drop {
        mark_to_drop();
    }action simple_forward{
        standard_metadata.egress_spec = port;
    }action drop {
        mark_to_drop();
    }action set_ecmp_select {
        /* TODO: hash on 5-tuple and save the hash result in meta.ecmp_select 
           so that the ecmp_nhop table can use it to make a forwarding decision accordingly */
    }action set_nhop {
        hdr.ethernet.dstAddr = nhop_dmac;
        hdr.ipv4.dstAddr = nhop_ipv4;
        standard_metadata.egress_spec = port;
        hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
    }action rewrite_mac {
        hdr.ethernet.srcAddr = smac;
    }action drop {
        mark_to_drop();
    }action drop {
        mark_to_drop();
    }action simple_forward{
        standard_metadata.egress_spec = port;
    }action drop {
        mark_to_drop();
    }action set_ecmp_select {
        /* TODO: hash on 5-tuple and save the hash result in meta.ecmp_select 
           so that the ecmp_nhop table can use it to make a forwarding decision accordingly */
    }action set_nhop {
        hdr.ethernet.dstAddr = nhop_dmac;
        hdr.ipv4.dstAddr = nhop_ipv4;
        standard_metadata.egress_spec = port;
        hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
    }action rewrite_mac {
        hdr.ethernet.srcAddr = smac;
    }action drop {
        mark_to_drop();
    }table eth_exact{
        key = {
            hdr.ethernet.srcAddr:exact;
        }
        actions={
             simple_forward();
             NoAction;
             drop;
        }
        size = 1024;
        default_action = NoAction();
    }table ecmp_group{
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            drop;
            set_ecmp_select;
        }
        size = 1024;
    }table ecmp_nhop{
        key = {
            meta.ecmp_select: exact;
        }
        actions = {
            drop;
            set_nhop;
        }
        size = 2;
    }table send_frame{
        key = {
            standard_metadata.egress_port: exact;
        }
        actions = {
            rewrite_mac;
            drop;
        }
        size = 256;
    }table eth_exact{
        key = {
            hdr.ethernet.srcAddr:exact;
        }
        actions={
             simple_forward();
             NoAction;
             drop;
        }
        size = 1024;
        default_action = NoAction();
    }table ecmp_group{
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            drop;
            set_ecmp_select;
        }
        size = 1024;
    }table ecmp_nhop{
        key = {
            meta.ecmp_select: exact;
        }
        actions = {
            drop;
            set_nhop;
        }
        size = 2;
    }table send_frame{
        key = {
            standard_metadata.egress_port: exact;
        }
        actions = {
            rewrite_mac;
            drop;
        }
        size = 256;
    }