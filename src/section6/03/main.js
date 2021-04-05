const app = Vue.createApp({
    data() {
        return {
            flag: true,
            shape: {
                backgroundColor: 'green',
                border: '5px solid orange'
            }
        }
    },
    methods: {
        changeShape() {
            const vm = this
            vm.flag = !vm.flag
        }
    }
})

const mountedApp = app.mount('#app')