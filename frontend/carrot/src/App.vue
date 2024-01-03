<script setup>
import Navbar from "./components/partials/Navbar.vue";
import Sidebar from "./components/partials/Sidebar.vue";
</script>

<template>
  <Navbar/>

  <div class="lg:container">
    <div class="relative">
      <Sidebar/>

      <div class="py-8 pl-4 lg:pl-8 pr-4 lg:pr-0 lg:ml-64">
        <div class="mt-14">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>
