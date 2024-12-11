import {createRouter, createWebHashHistory} from 'vue-router'

import Login from "../components/Login.vue";
import Home from "../components/Home.vue";
import Dashboard from "../components/Dashboard.vue";
import Students from "../components/Students.vue";
import Profile from "../components/Profile.vue";
import Password from "../components/Password.vue";
import guest from "./middleware/guest.js";
import auth from "./middleware/auth.js";
import admin from "./middleware/admin.js";
import middlewarePipeline from "./middlewarePipeline.js";

const routes = [
  {
    path: '/login',
    component: Login,
    name: 'login',
    meta: {
      middleware: [guest]
    },
  },
  {
    component: Home,
    meta: {
      middleware: [auth]
    },
    children: [
      {
        path: '/',
        component: Dashboard,
        name: 'dashboard',
      },
      {
        path: '/students',
        component: Students,
        name: 'students',
        meta: {
          middleware: [admin]
        },
      },
      {
        path: '/profile',
        component: Profile,
        name: 'profile',
      },
      {
        path: '/password',
        component: Password,
        name: 'password',
      }
    ]
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
router.beforeEach((to, from, next) => {
  if (!to.meta.middleware) {
    return next()
  }
  const middleware = to.meta.middleware
  const context = {
    to,
    from,
    next,
    store
  }
  return middleware[0]({
    ...context,
    next: middlewarePipeline(context, middleware, 1)
  })
})

export default router