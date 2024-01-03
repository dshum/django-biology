<template>
  <aside id="logo-sidebar"
         class="absolute top-0 left-0 z-40 lg:z-0 w-64 h-screen pt-20 transition-transform -translate-x-full lg:translate-x-0 bg-white border-r border-gray-200 dark:bg-gray-800 dark:border-gray-700"
         aria-label="Sidebar">
    <div class="h-full pr-4 pb-4 overflow-y-auto bg-white dark:bg-gray-800">
      <ul class="space-y-2 font-medium">
        <li>
          <router-link :to="{name: 'dashboard'}"
                       class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
            <font-awesome-icon icon="chart-pie"
                               class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"/>
            <span class="ms-3">Dashboard</span>
          </router-link>
        </li>
        <li>
          <router-link :to="{name: 'students'}"
                       class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
            <font-awesome-icon icon="graduation-cap"
                               class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"/>
            <span class="flex-1 ms-3 whitespace-nowrap">Students</span>
            <span
                class="inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300">1</span>
          </router-link>
        </li>
        <li>
          <a href="#"
             class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
            <font-awesome-icon icon="list-check"
                               class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"/>
            <span class="flex-1 ms-3 whitespace-nowrap">Tests</span>
            <span
                class="inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300">0</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>

<script setup>
</script>