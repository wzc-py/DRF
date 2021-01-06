import Vue from 'vue'
import Router from 'vue-router'
import First from "../components/First";
import Second from "../components/Second";
import Third from "../components/Third";
import User_details from "../components/User_details";
import Add_emp from "../components/Add_emp";


Vue.use(Router)

export default new Router({
    routes: [
        {path:"/user",component:First},
        {path:"/addr",component:Second},
        {path:"/note",component:Third},
        {path:"/user_de",component:User_details},
        {path:"/add_emp",component:Add_emp},
        {path:"/",redirect:"/user"},
        {path:"/*",redirect:"/user"},
    ]
})
