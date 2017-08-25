# ! python3.
# this script accepts a location from the system in cmd
# also a product to search for on an e-commerce website olx.com.ng
# no olx API, would have used that to minimize the code
# practice.py

import sys
import requests
import webbrowser
import bs4

# import all the needed modules
# you must have a module installed before you acn import it in a script
# you can install modules by using pip

print('Opening webpage...')
# the above string is displayed while loading

if len(sys.argv) > 1:
    # get location and product name from command line.
    location = ''.join(sys.argv[1])
    product = '-'.join(sys.argv[2:])


webbrowser.open_new_tab('http://olx.com.ng/' + location + '/q-' + product + '/?search')

# first argv takes the location
# note: while running the batch file
# you ned to provide the arguments, the name of the item [1]

res = requests.get('http://olx.com.ng/ads/q-' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.marginright5.link.linkWithHash.detailsLink')
numOpen = min(3, len(linkElems))
for i in range(numOpen):
    webbrowser.open_new_tab('http://olx.com.ng/ad/' + linkElems[i].get('href'))

















