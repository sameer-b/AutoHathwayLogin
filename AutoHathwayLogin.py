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
import urllib2, sys, time, socket

userName="USERNAME"
password="PASSWORD"

sleepTime=30

hostname = ['login.hathway.com', '203.212.193.60', '203.212.193.61']

def setup():
	global url, sleepTime

	if len(sys.argv) > 1:
		userName=sys.argv[1]
		password=sys.argv[2]
		sleepTime=int(sys.argv[3])

	socket.setdefaulttimeout(sleepTime)
	url = "/bsp/login.do?action=doLoginSubmit&flowId=UserLogin&username=" + userName + "&password=" + password

def checkInternetConnectivity():
	x = 1
	try:
		socket.create_connection( ("www.google.com", 80) )
	except:
		x = 0
	finally:
		return x

def connectToHathway():

	if len(hostname) == 0:
		sys.exit(1)
	else:
		for host in hostname:
			real_host = "http://" + host + url
			try:
				sys.stdout.write("Trying to authenticate to server %s\n" % (real_host) )
				urllib2.urlopen(real_host)
			except:
				sys.stderr.write("Failed to connect to %s Retrying\n" % (real_host) )
				continue
	
setup()
while 1==1:
	if checkInternetConnectivity() == 0:
		sys.stderr.write("Internet connectivity is dead. Trying to contact Hathway auth severs.\n")
		connectToHathway()
		time.sleep(sleepTime)
		continue
	else:
		sys.stdout.write("Internet connectivity alive. Sleeping for %s seconds.\n" % (sleepTime) )
		time.sleep(sleepTime)
		continue 
