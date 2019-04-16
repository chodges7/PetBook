// var app = new Vue({
//   el: '#app',
//   data: {
//     message: 'Hello Vue!'
//   }
// })
//
// var app2 = new Vue({
//   el: '#app-2',
//   data: {
//     message: 'You loaded this page on ' + new Date().toLocaleString()
//   }
// })
// var app4 = new Vue({
//   el: '#app-4',
//   data: {
//     todos: [
//       { text: 'Learn JavaScript' },
//       { text: 'Learn Vue' },
//       { text: 'Build something awesome' }
//     ]
//   }
// })

var app4 = new Vue({
	el: '#app-4',
	data: {
		pets: [],
	},
	//Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
	created: function() {
		this.fetchPetList();
		this.timer = setInterval(this.fetchPetList, 15000);
	},
	methods: {
		fetchPetList: function() {
			// $.get('/suggestions/', function(suggest_list) {
			//     this.suggestions = suggest_list.suggestions;
			//     console.log(suggest_list);
			// }.bind(this));
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
