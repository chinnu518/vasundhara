#Unit Test Cases
import URi Maniplation as URi Maniplation
obj = URi Maniplation.URI_Maniplation()

assert "http://" ==  obj.get_scheme("http://british-site.co.uk")
	
assert "://british-site.co.uk" == obj.get_hostname("http://british-site.co.uk")
	
assert ("https://" == obj.get_scheme("https://news.google.co.in/nwshp?hl=en&tab=wn&ei=haQpWN-QLonfvgSirq3gBw&ved=0EKkuCAYoBQ"))
	
assert ("://news.google.co.in" ==  obj.get_hostname("https://news.google.co.in/nwshp?hl=en&tab=wn&ei=haQpWN-QLonfvgSirq3gBw&ved=0EKkuCAYoBQ"))

assert (':8080' == obj.get_portno("http://www.contoso.com:8080/letters/readme.html"))

assert("://www.contoso.com" == obj.get_hostname("http://www.contoso.com:8080/letters/readme.html"))

assert(None == obj.get_portno("http://img251.imagevenue.com/"))

assert("http://" == obj.get_scheme("http://img251.imagevenue.com/"))

assert("://img251.imagevenue.com" == obj.get_hostname("http://img251.imagevenue.com/"))

assert("https://img251.imagevenue.com/" == obj.alter_scheme("http://img251.imagevenue.com/", "https://"))

assert ("http://google.com/" == obj.alter_hostname("http://img251.imagevenue.com/", "://google.com"))

assert ("http://www.contoso.com:9090/letters/readme.html" == obj.alter_portno("http://www.contoso.com:8080/letters/readme.html", ":9090"))