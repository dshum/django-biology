<template>
  <nav class="flex" aria-label="Breadcrumb">
    <ol class="mb-8 inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse">
      <li class="inline-flex items-center">
        <router-link :to="{name: 'dashboard'}"
                     class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white">
          <font-awesome-icon icon="house" class="w-3 h-3 me-2.5" />
          Dashboard
        </router-link>
      </li>
      <template v-for="element in elements">
        <li aria-current="page">
          <div class="flex items-center">
            <font-awesome-icon icon="chevron-right" class="rtl:rotate-180 w-3 h-3 text-gray-400 mx-1" />
            <span class="ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400">
              {{ element }}
            </span>
          </div>
        </li>
      </template>
    </ol>
  </nav>
</template>

<script setup>
defineProps({
  elements: Array[String]
})
</script>