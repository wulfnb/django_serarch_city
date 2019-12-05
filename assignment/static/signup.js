const app = new Vue({
    el: '#main',

    delimiters: ["<%", "%>"],

    data: {
        email: '',
        phone: '',
        first_name: '',
        last_name: '',
        gender: 'M',
        message: ''
        
    },

    computed: {
    },
    mounted() {
        
    },
    created() {
    },
    methods: {
        signup() {
            var signup_credintials = {
                'email': this.email,
                'phone': this.phone,
                'first_name': this.first_name,
                'last_name': this.last_name,
                'gender': this.gender
            }
            fetch('/users/signup_api/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(signup_credintials)
                }).then(response => {
                    return response.json()
                }).then(json => {
                    this.message = json.message
                    if(json.status === "success"){
                        this.email = ''
                        this.phone = ''
                        this.first_name = ''
                        this.last_name = ''
                        this.gender = 'M'
                    }
            })
        },

    }
})
