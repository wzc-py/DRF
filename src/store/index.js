import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        num:18,
    },
    mutations: {
        add_num(state){
            state.num--;
        }
    },
    getters: {},
})
