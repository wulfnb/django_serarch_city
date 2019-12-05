Vue.component('autocomplete', {
    delimiters: ["<%", "%>"],

    template: '#template-autosuggest',
    
    props: {
        suggestions: {
            type: Array,
            required: true
        },
        selection: {
            type: String,
            required: true,
            twoWay: true
        }
    },

    data: function () {
        return {
            open: false,
            current: 0,
            entered: ''
        }
    },


    computed: {
        //Filtering the suggestion based on the input
        matches() {
            if (this.suggestions.length > 0 && this.entered){
                return this.suggestions
            }
        },

        //The flag
        openSuggestion() {
            return this.entered !== "" &&
                this.selection.length != 0 &&
                this.open === true;
        }
    },
    methods: {
        // When the user changes input
        change() {
            this.$parent.changePage('search')
            if(this.entered){
                this.$parent.getCountries(this.entered)
            }
            if (this.open == false) {
                this.open = true;
                this.current = 0;
            }
        },

        // When one of the suggestion is clicked
        suggestionClick(index,code) {
            this.$parent.changePage('details');
            this.$parent.getDetails(code);
            this.entered = this.matches[index].city__name.concat(
                                            ', ', this.matches[index].name,', (', 
                                            this.matches[index].languages__language,')');
            this.open = false;
        },
    }

})


const app = new Vue({
    el: '#app',

    delimiters: ["<%", "%>"],

    data: {
        cities: [],

        value: '',
        page : {
            search: true,
            details: false
        },
        country_details: [],
        
    },

    computed: {
    },
    mounted() {
        
    },
    created() {
    },
    methods: {

        changePage(val){
            for (var key in this.page) {
                this.page[key] = false
            }
            this.page[val] = true
        },

        getCountries(search) {
            fetch('/country/q/'+search, {
                method: 'GET',
                credentials: 'include',
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
            }).then(response => {
                return response.json()
            }).then(json => {
                this.cities = json
            })

        },

        getDetails(code) {
                fetch('/country/details/'+code, {
                    method: 'GET',
                    credentials: 'include',
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                    },
                }).then(response => {
                        return response.json()
                }).then(json => {
                    this.country_details = json
                })

        },

    }
})
