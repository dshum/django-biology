<script>
  import "../app.scss";
</script>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand shadow rounded px-4 text-light" href="/">Admin</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample07" aria-controls="navbarsExample07" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarsExample07">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/settings">Settings</a>
        </li>
      </ul>
      <form role="search">
        <input class="form-control" type="search" placeholder="Search" aria-label="Search">
      </form>
    </div>
  </div>
</nav>

<div class="container">
  <div class="section my-4">
    <slot></slot>
  </div>
</div>

<style>
  .navbar-brand {
    background-color: darkorchid;
  }
</style>