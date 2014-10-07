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

file=None
if file is None:
	#try:
	fh = open("/tmp/hathway.log", 'w')
	#except IOError:
	#	print "Couldn't write to file /tmp/hathway.log";
else:
	try:
		fh = open(file, 'w')
	except IOError:
		print "Couldn't write to file %s\n" % (file);

def setup():
	global url, sleepTime, userName, password

	if len(sys.argv) > 1:
		userName=sys.argv[1]
		password=sys.argv[2]
<<<<<<< HEAD
		sleepTime=int(sys.argv[3])

	socket.setdefaulttimeout(sleepTime)
	url = "/bsp/login.do?action=doLoginSubmit&flowId=UserLogin&username=" + userName + "&password=" + password
=======
		sleepTime=sys.argv[3]
	
def local_write(str):
	sys.stdout.write(str)
	fh.write(str)
	fh.flush()
>>>>>>> da95c3343d8b0554821c6c8756c9b29d155839e0

def checkInternetConnectivity():
	x = 1
	try:
		socket.create_connection( ("https://www.google.com", 80) )
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
				local_write("%s\tTrying to authenticate to server %s\n" % (time.ctime(), real_host) )
				urllib2.urlopen(real_host)
			except:
				local_write("%s\tFailed to connect to %s Retrying\n" % (time.ctime(), real_host) )
				continue
	
setup()
while 1==1:
	if checkInternetConnectivity() == 0:
		local_write("%s\tInternet connectivity is dead. Trying to contact Hathway auth severs.\n" % (time.ctime() ) )
		connectToHathway()
		time.sleep(sleepTime)
		continue
	else:
		local_write("%s\tInternet connectivity alive. Sleeping for %s seconds.\n" % (time.ctime(), sleepTime) )
		time.sleep(sleepTime)
		continue 
