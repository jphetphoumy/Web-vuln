<script>
	export let domain = '';
	export let promise = {data: ''};
	async function getIpInformation(domain) {
		const response = await fetch('http://localhost:8000/nslookup', {
			method: 'POST',
			body: JSON.stringify({'domain': domain}),
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			}
		})
			.then(data => data.json())
		console.log(response)
		return response
	}

	function handleClick(domain) {
		promise = getIpInformation(domain)
	}

	function handleKeydown(event) {
		if (event.keyCode === 13) {
			promise = getIpInformation(domain);
		}
	}
</script>

<main>
	<h1>Nslookup - Software as a service</h1>
	<p>Récupération de l'address ip du domain : {domain}</p>
	<input bind:value={domain} on:keydown={handleKeydown}>
	<button disabled={!domain} type="submit" on:click={handleClick(domain)}>Récupérer l'ip</button>

	<div>
		{#await promise}
			<strong>Information :</strong> 
			<p>Chargement de la réponse ...</p>
		{:then response}
			{#if response.data !== ''}
			<strong>Information :</strong>
			<p>{@html response.data}</p>
			{/if}
		{:catch error}
			<p>{error}</p>
		{/await}
	</div>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>