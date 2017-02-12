#!/usr/bin/env python

#
# $Id: main.py,v 1.0 2012/03/18 22:31:54 aedavies Exp $
#
#/*
# * Copyright (c) 2012 Archzilon Eshun-Davies <laudarch@qremiaevolution.org>
# *
# * Permission to use, copy, modify, and distribute this software for any
# * purpose with or without fee is hereby granted, provided that the above
# * copyright notice and this permission notice appear in all copies.
# *
# * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# */

# imports
import os
import sys
import cgi
import math
import datetime
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

# import from private library
try:
	from laudlib import lauddb
except ImportError:
	print "Fatal Error: can't import private library"

# app settings
_Author_  = "Archzilon Eshun-Davies(laudarch)";
_Appname_ = "Sika Droid";
_DEBUG_   = True; # Debug mode?
_SHOW_    = True; # Show verbose details :)

def init_laudlib():
	DIR_PATH = os.path.abspath(
        os.path.dirname(os.path.realpath(__file__)));

	LAUDLIB_PATHS = [
  		DIR_PATH,
  		os.path.join(DIR_PATH, 'laudlib'),
  		os.path.join(DIR_PATH, 'laudlib', 'lauddb')
	]
	# Fix the sys.path to include our extra paths.
	sys.path = LAUDLIB_PATHS + sys.path;

#   Base request handler extends webapp.RequestHandler
class BaseRequestHandler(webapp.RequestHandler):
	#-------------------------------------------------------#
	# showtpl shows the requested template with its values  #
	# @args:                                                #
	#   tpl_name: template name                             #
	#   tpl_data: values to pass to template default is NUL #
	#-------------------------------------------------------#
	def showtpl(self, tpl_name, tpl_data={}):
		values = {
			'request': self.request,
			'appname': _Appname_,
		}
		values.update(tpl_data);

		# Construct the path to the template
		path = os.path.join(os.path.dirname(__file__), 'tpl', tpl_name);

		# Render template
		self.response.out.write(template.render( path, values, debug=_DEBUG_));

class Home(BaseRequestHandler):
    def get(self):
        self.showtpl("home.tpl");

class AddRecord(BaseRequestHandler):
    def get(self):
        uid = self.request.get("uid");
	amt = self.request.get("amt");
	curbal = lauddb.balance.gql( 'where clientid = :1', uid ).get();
	a  = int(amt);
	cb = int(curbal.currentbal);
	if (curbal):
		_currentbal = str(cb + a);
	else:
		_currentbal = amt;
	cdb = lauddb.deposit(clientid = uid, amountpaid = amt);
	bal = lauddb.balance(clientid = uid, currentbal = _currentbal);
	cdb.put();
	bal.put();
	self.response.out.write("Record Added! <a href='javascript:history.back(-1);'>Go Back</a>"+_currentbal);

class GetRecords(BaseRequestHandler):
    def get(self):
	deposits = db.Query(lauddb.deposit);
	deposits.get();
	show = "<table><tr><td>Client ID</td><td>Full Name</td><td>Amount</td><td>Balance</td><td>Account Number</td><td>Date</td></tr>";
	for d in deposits:
		c = lauddb.client.gql('where clientid = :1', d.clientid).get();
		b = lauddb.balance.gql('where clientid = :1', d.clientid).get();
		created = d.created.strftime("%Y-%m-%d %H:%M:%S");
		show += "<tr><td>"+d.clientid+"</td>"+"<td>"+c.clientname+"</td>"+"<td>"+d.amountpaid+"</td>"+"<td>"+b.currentbal+"</td>"+"<td>"+c.acctnum+"</td><td>"+created+"</td></tr>\n";
		
	show += "</table";
	self.response.out.write(show);

class Register(BaseRequestHandler):
    def get(self):
	fname   = self.request.get("fname");
	accnum  = self.request.get("accnum");
	cid     = self.request.get("cid");
	deposit = self.request.get("deposit");
	
	nr = lauddb.client(clientid=cid, clientname=fname, acctnum=accnum);
	dp = lauddb.deposit(clientid = cid, amountpaid = deposit);
	ba = lauddb.balance(clientid=cid, currentbal=deposit);
	
	# put all in now ^^
	nr.put();
	dp.put();
	ba.put();
	
	self.response.out.write("1");
	
def main():
    init_laudlib();
    droidcollector = webapp.WSGIApplication(
        [('/', Home),
         ('/AddRecord', AddRecord),
	 ('/GetRecords', GetRecords),
	 ('/Register', Register)], debug=_DEBUG_);

    util.run_wsgi_app(droidcollector)


if __name__ == '__main__':
    main()
