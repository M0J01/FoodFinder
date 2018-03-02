import mechanize
import cookielib
import json
#import urllib



APICode = "swc6iwKitEP0BtugYQn8Wo4nwWtn4uHrMDQWpxTc"

def get_webpage(url):

	#Set up mechanize and put in cookie jar
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	#Sets our Browser to handle Refreshes
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	#sets our Browser to immitate a browser
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	#Sets some cool stuff abut what mechanize browser can handle.
	br.set_handle_equiv(True)
	#br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)

	#Opens the URL given
	try:
		r = br.open(url)
		htmltextz = r.read()
		#htmltextz = htmltextz.lower() not gonna do this here. Messes with the tag searching.
	except:
		print (url)
		htmltextz = '0'

	return htmltextz





call_link = "" + APICode + ""

call_link = "https://api.nal.usda.gov/ndb/reports/?ndbno=11090&type=f&format=json&api_key=swc6iwKitEP0BtugYQn8Wo4nwWtn4uHrMDQWpxTc"
#call_link = "https://api.nal.usda.gov/ndb/reports/?ndbno=01009&type=b&format=xml&api_key=DEMO_KEY"
json1 = get_webpage(call_link)

parsed = json.loads(json1)
#print (json.dumps(parsed, indent=4, sort_keys=True))
#print (parsed['report'])

#print (data)