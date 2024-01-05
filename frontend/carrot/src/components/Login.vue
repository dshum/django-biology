<template>
  <div class="container">
    <div class="flex justify-center items-center h-screen">
      <div class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
        <form @submit.prevent="login">
          <div class="mb-6">
            <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Login</label>
            <input type="text" id="username" autocomplete="username"
                   v-model="username"
                   class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                   placeholder="johnny" required>
          </div>
          <div class="mb-6">
            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
            <input type="password" id="password" autocomplete="current-password"
                   v-model="password"
                   class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                   placeholder="•••••••••" required>
          </div>
          <button type="submit"
                  class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
            Login
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from "vue";
import BASE_API_URL from "../constants/constants"
import axios from "axios";
import router from "../router/router";

const username = ref("")
const password = ref("")

function login() {
  const data = {
    username: username.value,
    password: password.value,
  }

  axios.post(BASE_API_URL + "/api/token/", data)
      .then(data => {
        router.push("/");
      })
      .catch(function (error) {
        console.log(error);
      })
}
</script>