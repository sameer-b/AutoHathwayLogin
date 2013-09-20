'''
	Copyright (C) 2013 Sameer Balasubrahmanyam

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

 '''
import httplib, urllib2, sys, time
postUrl=None
sleepTime=30
def setup():
	global postUrl
	if len(sys.argv) == 1:
		userName="INSERT YOUR HATHWAY EMAIL"
		password="INSERT YOUR HATHEAY PASSWORD"
	else:
		userName=sys.argv[1]
		password=sys.argv[2]
		sleepTime=sys.argv[3]
	postUrl="http://login.hathway.com/bsp/login.do?action=doLoginSubmit&flowId=UserLogin&username="+userName+"&password="+password
	


def checkInternetConnectivity():
	conn = httplib.HTTPConnection("www.google.com")
	conn.request("GET", "/")
	r1 = conn.getresponse()
	status=r1.status
	
	if status != 302: 
		return 0
	else: 
		return 1


def connectToHathway():

	urllib2.urlopen(postUrl)
	


setup()
while 1==1:
	if checkInternetConnectivity() == 0:
		connectToHathway()
		time.sleep(sleepTime)
		continue
	else:
		time.sleep(sleepTime)
		continue 
		