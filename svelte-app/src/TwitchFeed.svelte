<head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Stylish&display=swap" rel="stylesheet">
</head>
<style>
h1
{
	color:deepskyblue;
	text-shadow: -1px 1px 2px #FFF
}
</style>
<script>
	export let title
</script>
<body>
	<h1 style="color:deepskyblue;font-family:Stylish">{title}</h1>
  <!-- Add a placeholder for the Twitch embed -->
<div id="twitch-embed"></div>

<script src="https://player.twitch.tv/js/embed/v1.js"></script>
<script type="text/javascript">
export let channel
new Twitch.Player("twitch-embed", { channel: channel });
</script>
</body>
