const app = new Vue({
    el: '#main',

    delimiters: ["<%", "%>"],

    data: {
        email: '',
        otp: '',
        page: {
            email: true,
            otp: false
        },
        message: ''
        
    },

    computed: {
    },
    mounted() {

        
    },
    created() {
    },
    methods: {
        login() {
            var login_credintials = {
                'email': this.email
            }
            fetch('/users/login_api/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(login_credintials)
                }).then(response => {
                    return response.json()
                }).then(json => {
                    this.message = json.message
                    if(json.status === "success"){
                        this.page.email = false
                        this.page.otp = true
                    }
            })
        },

        validate_otp() {
            var login_credintials = {
                'email': this.email,
                'otp': this.otp
            }
            fetch('/users/validate_otp_api/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(login_credintials)
                }).then(response => {
                    return response.json()
                }).then(json => {
                    if(json.status === "success"){
                        alert(json.message)
                        window.location.replace("/users/dashboard/");
                    }
                    else{
                        this.message = json.message
                    }
            })
        },

    }
})
