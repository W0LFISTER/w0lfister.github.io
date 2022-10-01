# Burp Suite HOW-TO

1. Start Burp Suit
	![[Pasted image 20220926172444 1.png]]
2. Configure Proxy on Firefox
	1. Go to Settings
	2. Type Proxy in the search bar
	3. ![[Pasted image 20220926173409.png]]
	4. select the Manual proxy configuration where we enter as an HTTP Proxy the 127.0.0.1 IP and port the 8080 where Burp Proxy is listening.
		Note: It is advisable to also check the option of Also use this proxy for FTP and HTTPS so all requests can
		go through Burp.
		![[Pasted image 20220926173621.png]]
3. Disable the interception in Burp suite as it's enabled by default. Navigate to Proxy Tab and under Intercept subtab select the button where Intercept in on so to disable it. ![[Pasted image 20220926174037.png]]
4. Navigate to target domain

### Links
[Using Web Proxies](https://academy.hackthebox.eu/course/preview/using-web-proxies)

[YouTube](https://www.youtube.com/watch?v=IWWYNDiwYOA)



###TAGS 
#burpsuit #proxy #firefox 