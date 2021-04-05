const app = Vue.createApp({
    data() {
        return {
            auth: false,
            product: 'Sunglasses',
            quantity: 0,
            sale: false
        }
    },
    methods: {
        logIn() {
            const vm = this
            vm.auth = true
        },
        logOut() {
            const vm = this
            vm.auth = false
        }
    }
})

const mountedApp = app.mount('#app')