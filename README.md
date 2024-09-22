# pishingDetector
Phishing is when a website tries to trick you into giving up sensitive information, by sending you a link to a fake website disguised like a trustworthy one. You can use this to train a machine learning model that can predict if a web address is a real link, or a phishing link to a fake website.

In this project, the training dataset used includes attributes of five hundred legitimate web addresses, and five hundred phishing links.

The 'address type' field is 'IP addr' if the link has a numeric IP address like '104.20.74.246' or 'DNS name' if the link has a name-based address like 'machinelearningforkids.co.uk'.
The 'url length' field groups the training addresses by how long they are.
The 'shortening' field is 'yes' if the web address uses a shortening service like TinyURL or bit.ly, or 'no' if it doesn't.
The 'includes @' field is 'yes' if the web address includes an @ symbol, or 'no' if it doesn't.
The 'port number' field is 'standard' if the web address uses a standard port number like 80 or 443, or 'non-std' if it uses something different.
The 'domain age' field groups addresses by how long ago the web address in the address was registered.
The 'redirects' field groups the training addresses by the number of times a web browser is sent to a different address before reaching a final page.
The 'domain reg' field is 'expiring' if the registration for the web address domain name expires within a year.
