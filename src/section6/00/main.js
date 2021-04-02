const app = Vue.createApp({data(){
    return {
        message: 'Hello World!',
        value: 5,
        imgSrc: 'https://images.unsplash.com/photo-1481349518771-20055b2a7b24?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8cmFuZG9tfGVufDB8fDB8&ixlib=rb-1.2.1&w=1000&q=80',
        link: 'https://google.com'
    }
}})

const mountedApp = app.mount('#app')