const app = Vue.createApp({
    data() {
        return {
            users: ['alice', 'bob', 'batman', 'robin']
        }
    },
    methods: {}
})

const mountedApp = app.mount('#app')