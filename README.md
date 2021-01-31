# oai_ue_graph_generator
Python script that generates plot from the text file and save in directory /Outputs

File should contain keyword "Test" for every new tests. It is the keyword that is used to detect new test. '\n' is ignored and the line after "Test" is taken as title for the graph and filename. 

An example input file can have:

Test 1
UE1 UP

[ ID] Interval       Transfer Bandwidth   Retr  Cwnd
[  4]   0.00-1.00   sec  2.67 MBytes  22.4 Mbits/sec 0 165 KBytes
[  4]   1.00-2.00   sec  2.49 MBytes  20.8 Mbits/sec 0 264 KBytes
[  4]   2.00-3.00   sec  2.42 MBytes  20.3 Mbits/sec 0 362 KBytes
[  4]   3.00-4.00   sec  2.17 MBytes  18.2 Mbits/sec   15 290 KBytes
[  4]   4.00-5.00   sec  1.93 MBytes  16.2 Mbits/sec 0 337 KBytes
[  4]   5.00-6.00   sec  1.93 MBytes  16.2 Mbits/sec 0 369 KBytes
[  4]   6.00-7.00   sec  1.74 MBytes  14.6 Mbits/sec 3 269 KBytes
[  4]   7.00-8.00   sec  2.11 MBytes  17.7 Mbits/sec 0 296 KBytes

.....
.....

Test 2
UE1 DOWN

[ ID] Interval       Transfer Bandwidth   Retr  Cwnd
[  4]   0.00-1.00   sec  2.67 MBytes  22.4 Mbits/sec 0 165 KBytes
[  4]   1.00-2.00   sec  2.49 MBytes  20.8 Mbits/sec 0 264 KBytes
[  4]   2.00-3.00   sec  2.42 MBytes  20.3 Mbits/sec 0 362 KBytes
[  4]   3.00-4.00   sec  2.17 MBytes  18.2 Mbits/sec   15 290 KBytes
[  4]   4.00-5.00   sec  1.93 MBytes  16.2 Mbits/sec 0 337 KBytes
[  4]   5.00-6.00   sec  1.93 MBytes  16.2 Mbits/sec 0 369 KBytes
[  4]   6.00-7.00   sec  1.74 MBytes  14.6 Mbits/sec 3 269 KBytes
[  4]   7.00-8.00   sec  2.11 MBytes  17.7 Mbits/sec 0 296 KBytes

...
...


