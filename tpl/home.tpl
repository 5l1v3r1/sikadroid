<!DOCTYPE html>
<!--
/*
 * Copyright (c) 2012 Archzilon Eshun-Davies <laudarch@qremiaevolution.org>
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */
-->
<html>
	<head>
		<title>{{ appname }}</title>
		<link href="/static/css/Site.css" rel="stylesheet" type="text/css">
		<script src="/static/js/xhr.js" type="text/javascript"></script>
		<script src="/static/js/fun.js" type="text/javascript"></script>
	</head>
	<body>
		<div id="page">
			<header>
				<div id="title">
					<h1><img src="/static/images/logo.jpg" align="center" width="100" height="120"/>{{ appname }}</h1>
				</div>
			</header>
			<nav>
				<ul id="menu">
					<li><a onclick="transactions();">Transactions</a></li>
					<li><a onclick="overlay('overlay');">New Client</a></li>
					<li><a href="/static/files/Sika Droid.apk"><b>Download Android APP</b></a></li>
					<li><a href="slides/index.html">Presentation Slides</a></li>
				</ul>
			</nav>
			<section id="main">
				<hr />
					<div id="ares"></div>
				<hr /><br />
			</section>
			<footer>
				&copy; 2012 laudarch <a href="http://qremiaevolution.org">Qremia Evolution</a> | <a href="http://code.google.com/p/sika-droid/">Source Code for this App(including android app source)</a> Source is under OpenBSD License.
			</footer>
		</div>
		<debug id="dbg"></debug>
		<div id="overlay">
		     <div>
			<a href="javascript:overlay('overlay');" align="right">Close(X)</a>
			<p>
				<canvas width="27" height="27" id="loader"></canvas>
				<form id="frm">
					<table border="1"><tr>
					<td width="50%"><p>Full Name:
					<input type="text" id="fname" /></p></td></tr><tr><td>
					<p>Account Number
					<input type="text" id="accnum" /></p></td></tr><tr><td>
					<p>Client ID
					<input type="text" id="cid" /></p></td></tr><tr><td>
					<p>Initial Deposit
					<input type="text" id="deposit" /></p></td></tr><tr><td>
					<p><input type="button" value="Register New Client" onclick="newclient();"/></p>
					</td></tr></table>
				</form>
			</p>
		     </div>
		</div>
		<script type="text/javascript">
		  var _gaq = _gaq || [];
		  _gaq.push(['_setAccount', 'UA-30228916-1']);
		  _gaq.push(['_trackPageview']);

		  (function() {
		    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		  })();
		</script>
	</body>
</html>