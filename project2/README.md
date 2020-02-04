Hey all, this one was sort of fun. TIme crunch made it difficult to follow a coherent design but we did it lads.

For this we started with building the Routing table, by using a RoutingInfo object and doing the bitwise operations there.

Next we dumped our table to make sure the routing table was working properly and we knew how to send packets,
to the apropriate location.

Finally we worked on update, we obviously did the part with the routing table here first but then we finished it,
by creating the apropaite packet, by changing the src dst and ASPath of the message, then sending out the
 apropriate update packet to the apropriate hosts.
