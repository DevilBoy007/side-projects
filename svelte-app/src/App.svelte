<svelte:head>
	title="archives"
</svelte:head>
<script>
import SiteView from './SiteView.svelte'
import TwitchFeed from './TwitchFeed.svelte'
import InputBar from './InputBar.svelte'

let sites = [{url:'https://www.codespot.org/',
								  title:'codespot '},
								{url:'https://www.merriam-webster.com/word-of-the-day/calendar',
									title: 'word of the day'},
								{url:'https://css-tricks.com/snippets/css/a-guide-to-flexbox/',
									title:'css-tricks flexbox'},
								{url:'http://www.nationalgeographic.com', title:'Nat Geo'}]
</script>
<body style="background-color:#272727;justify-content: space-evenly;">
	<InputBar on:add={(e) => sites = [...sites, e.detail]}/>
	<div style="display:flex;overflow-x:auto;">
	{#each sites as site}
	<div style="margin-top: 20vh;">
		<SiteView {...site}/>
	</div>
	{/each}
	</div>
	<div style="display:flex;overflow-x:auto;">
	{#each sites.reverse() as site, i (i)}
		<SiteView {...site}/>
	{/each}
	</div>
</body>
