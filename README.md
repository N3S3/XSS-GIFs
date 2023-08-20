# XSS-GIFs
XSS injection into GIFs

This peace is promptengineered with gpt-4.
I spent a lot of time to develope the right prompts!!!
Here is a example prompt:
Please use the .pac structure from the file inkognito.pac. Configure the Debian NetworkManager to use this .pac. To get the list of proxies, use the program www.github.com/N3S3/INKOGNITO. The functional logic is in modified_main.py. Output is a list of tested proxies which you can transfer to the proxy list of proxies in inkognito.pac.  Store inkognito.pac in the folder /tmp/ but have always a template under /home/user/ backuped. Task is to have a program which generates a output of a bunch  working proxy addresses(INKOGNITO does this), this is stored in a pac file which rotates the ips every 1 minute. This in a proxy chain of 3 server. Place that in autorun and start the whole process every 1 hour(get a proxy list --> store in /tmp/inkognito.pac for the DebianNetworkManager and make it randomly rotate: 1st the 3 server chain (every 5 minutes) and the proxy list(every 1hour). Do not forget the backup of the native incognito.pac in /root. If you have questions feel free to ask. Dont break the code!!! Use a very high correctness and run unit tests. Good luck!!!   

![Screenshot 1](https://github.com/N3S3/XSS-GIFs/assets/68975029/c1cb3f2a-b59c-4d54-88b4-5cbd345eecab)


with code examples
![Screenshot 2](https://github.com/N3S3/XSS-GIFs/assets/68975029/1e9c839a-5d7f-44ab-a7c1-4c4b10e5429f)



