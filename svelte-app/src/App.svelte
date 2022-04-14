<head>
	title="archives"
</head>
<script>
import SiteView from './SiteView.svelte'
import TwitchFeed from './TwitchFeed.svelte'

const codespot = {url:'https://www.codespot.org/',
								title:'codespot '}
const wiki = {url:'https://wikipedia.com/',
							 title: 'wikipedia'}
const wotd = {url:'https://www.merriam-webster.com/word-of-the-day/calendar',
						 title: 'word of the day'}
const css = {url:'https://css-tricks.com/snippets/css/a-guide-to-flexbox/',
						 title:'css-tricks flexbox'
}
const channel_1 = {channel:'xqcow',
							title: 'stream #1' }

</script>
<body style="background-color:black;justify-content: space-evenly;">
	<div style="display:flex;overflow-x:auto;">
		<SiteView {...wotd}/>
		<SiteView {...codespot}/>
		<SiteView {...wiki}/>
		<SiteView {...css}/>
	</div>
	<div style="display:flex;overflow-x:auto;">
	  <SiteView {...css}/>
		<SiteView {...wiki}/>
		<SiteView {...codespot}/>
		<SiteView {...wotd}/>
	</div>
</body>
