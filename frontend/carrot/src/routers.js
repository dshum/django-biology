import {createRouter, createWebHashHistory} from 'vue-router'

import Dashboard from "./components/Dashboard.vue";
import Students from "./components/Students.vue";
import Profile from "./components/Profile.vue";
import Password from "./components/Password.vue";

const routes = [
  {path: '/', component: Dashboard, name: 'dashboard'},
  {path: '/students', component: Students, name: 'students'},
  {path: '/profile', component: Profile, name: 'profile'},
  {path: '/password', component: Password, name: 'password'}
]

export default createRouter({
  history: createWebHashHistory(),
  routes,
})