<!DOCTYPE HTML>
<!--
	Astral by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Astral by HTML5 UP</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
		
		<!-- Scripts -->
		<script src="assets/js/jquery.min.js"></script>
		<script src="assets/js/skel.min.js"></script>
		<script src="assets/js/skel-viewport.min.js"></script>
		<script src="assets/js/util.js"></script>
		<!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
		<script src="assets/js/main.js"></script>
	</head>
	
	<body>
		<!-- Wrapper-->
		<div id="wrapper">
			<!-- Nav -->
			<nav id="nav">
				<a href="#home" class="icon fa-home active"><span>Home</span></a>
				<a href="#about" class="icon fa-info-circle"><span>About</span></a>
				<a href="#samples" class="icon fa-music"><span>Find</span></a>
				<a href="#upload" class="icon fa-upload"><span>Upload</span></a>
				<a href="#contact" class="icon fa-envelope"><span>Contact</span></a>
				<a href="#account" class="icon fa-user"><span>Account</span></a>
			</nav>
			
			<!-- Main -->
			<div id="main">
				<!-- Home -->
				<article id="home" class="panel">
					<header>
						<?php include 'home_header.php'; ?>
					</header>
					<section>
						<?php include 'home_section.php'; ?>
					</section>
				</article>
				
				<!-- About -->
				<article id="about" class="panel">
					<header>
						<?php include 'about_header.php'; ?>
					</header>
					<section>
						<?php include 'about_section.php'; ?>
					</section>
				</article>
				
				<!-- Samples -->
				<article id="samples" class="panel">
					<header>
						<?php include 'samples_header.php'; ?>
					</header>
					
					<section>
						<?php include 'samples_section.php'; ?>
					</section>
				</article>

				<!-- Upload Samples -->
				<article id="upload" class="panel">
					<header>
						<?php include 'upload_header.php'; ?>
					</header>
					
					<section>
						<?php include 'upload_section.php'; ?>
					</section>
				</article>
				
				<!-- Contact -->
				<article id="contact" class="panel">
					<header>
						<?php include 'contact_header.php'; ?>
					</header>
					
					<section>
						<?php include 'contact_section.php'; ?>
					</section>
				</article>
				
				<!-- User Account -->
				<article id="account" class="panel">
					<header>
						<?php include 'account_header.php'; ?>
					</header>
					
					<section>
						<?php include 'account_section.php'; ?>
					</section>
				</article>
				
			</div>
			
			<!-- Footer -->
			<div id="footer">
				<ul class="copyright">
					<li>&copy; Untitled.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
				</ul>
			</div>
		</div>		
	</body>
</html>