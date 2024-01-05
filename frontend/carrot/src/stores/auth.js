import {defineStore} from 'pinia';
import axios from "axios";
import BASE_API_URL from "../constants/constants.js";
import router from "../router/router.js";

export const useAuthStore = defineStore('authStore', {
  state: () => ({
    authUser: null,
  }),
  getters: {},
  actions: {
    setAuthUser(user) {
      this.authUser = user;
    },
  },
})