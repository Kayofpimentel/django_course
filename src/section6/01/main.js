const app = Vue.createApp({
    data() {
        return {
            lesson: 'Events and Methods',
            counter: 0
        }
    },
    methods: {
        incrementCounter() {
            const vm = this
            vm.counter += 1
            if (vm.counter === 10) {
                alert('Counter is at 10!')
            }
        },
        overTheBox() {
            console.log('Over The Box!')
        }
    }
})

const mountedApp = app.mount('#app')