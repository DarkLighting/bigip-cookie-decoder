#!/usr/local/bin/python2.7

import sys;

ip_port = sys.argv[1].split('.');
ip_orig = ip_port[0];
port_orig = ip_port[1];
ip = hex( int( ip_orig ) )[2:];  # removing the '0x' string from the beginning;
port = hex( int( port_orig ) )[2:];  # removing the '0x' string from the beginning;
dest_ip = list();
dest_port = list();
for i in range( 0, len( ip ), 2 ):
    dest_ip.append( str( int( ip[i:i+2], base=16 ) ) );
for i in range( 0, len( port ), 2 ):
    dest_port.append( str( port[i:i+2] ) );
dest_ip.reverse();
dest_port.reverse();
dest_port = ''.join( dest_port );
print "BigIP address decoded: %s:%s" %( '.'.join( dest_ip ), int( str( dest_port ), base=16 ) );
