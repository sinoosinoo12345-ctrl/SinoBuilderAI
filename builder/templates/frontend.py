INDEX_HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
name="viewport"
content="width=device-width,initial-scale=1">

<title>{project}</title>

<link
rel="stylesheet"
href="assets/css/style.css">

</head>

<body>

<div id="app"></div>

<script
src="assets/js/app.js"></script>

</body>

</html>
"""
STYLE_CSS = """
*{

margin:0;

padding:0;

box-sizing:border-box;

}

body{

background:#0f172a;

color:#ffffff;

font-family:Inter,Arial,sans-serif;

min-height:100vh;

}

#app{

padding:30px;

}
"""
APP_JS = """
console.log(

"Sino Builder Frontend"

);
"""
LAYOUT = """
<header class="topbar">

<div class="logo">

{project}

</div>

<nav>

<a href="home.html">Home</a>

<a href="dashboard.html">Dashboard</a>

<a href="settings.html">Settings</a>

</nav>

</header>

<main id="content">

</main>

<footer>

Powered By Sino Builder AI

</footer>
"""
HOME_PAGE = """
<section>

<h1>

Welcome

</h1>

<p>

Professional AI Generated Application

</p>

</section>
"""
DASHBOARD_PAGE = """
<section>

<h2>

Dashboard

</h2>

<div id="dashboard">

</div>

</section>
"""
SETTINGS_PAGE = """
<section>

<h2>

Settings

</h2>

<div id="settings">

</div>

</section>
"""
FRONTEND_TEMPLATE = {

    "index": INDEX_HTML,

    "style": STYLE_CSS,

    "javascript": APP_JS,

    "layout": LAYOUT,

    "home": HOME_PAGE,

    "dashboard": DASHBOARD_PAGE,

    "settings": SETTINGS_PAGE,

}
