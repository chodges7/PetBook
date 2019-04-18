var app4 = new Vue({
	el: '#app-4',
	data: {
		pets: [],
	},
	//Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
	created: function() {
		this.fetchPetList();
		this.timer = setInterval(this.fetchPetList, 10000);
	},
	methods: {
		fetchPetList: function() {
			axios
				.get('/pets/')
				.then(response => (this.pets = response.data.pets))
			console.log(this.pets)
		},
		cancelAutoUpdate: function() { clearInterval(this.timer) }
	},
	beforeDestroy() {
		clearInterval(this.timer)
	}

})
