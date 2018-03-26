#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()

import os

acao=var.split("=")[0]

print("content-type: text/html")
print("")

if acao == "di":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 start")
	print("<h1>Iniciado!<h1/>")
elif acao == "dp":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 stop")
	print("<h1>Parado!<h1/>")
elif acao == "dr":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 restart")
	print("<h1>Reiniciado!<h1/>")
elif acao == "ni":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
	print("<h1>Iniciado!<h1/>")
elif acao == "np":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
	print("<h1>Parado!<h1/>")
elif acao == "nr":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
	print("<h1>Reiniciado!<h1/>")
elif acao == "fi":
	os.system("sudo bash /usr/lib/cgi-bin/infire.sh")
	print("<h1>Iniciado!<h1/>")
elif acao == "fp":
	os.system("sudo bash /usr/lib/cgi-bin/pafire.sh")
	print("<h1>Parado!<h1/>")
elif acao == "fr":
	os.system("sudo bash /usr/lib/cgi-bin/refire.sh")
	print("<h1>Reiniciado!<h1/>")
elif acao == "AGENDAR":
	f = open("/var/www/html/cron.html", "r")
	cron=f.read()
	f.close()
	print(cron)
