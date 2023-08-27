<script>
  let title = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat, illum?"

  let updateTitle = () => {
    title = title.toUpperCase()
  }
</script>

<h2>{title}</h2>

<input type="text" bind:value={title}>

<button class="btn" on:click={updateTitle}>Push me</button>

<p class="lead">
  This is a lead paragraph. It stands out from regular paragraphs.
</p>
<p class="lead">
  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci architecto assumenda autem commodi deserunt eveniet fuga, fugit hic itaque, magnam nobis numquam omnis quia quo ratione soluta sunt. Amet architecto, consequatur debitis doloribus, dolorum eius eligendi error excepturi fugiat harum illum inventore libero nemo officia pariatur placeat possimus quia quisquam repellendus reprehenderit, sed similique suscipit tempora totam veritatis voluptate voluptatum.
</p>

<div class="my-4">
  <form>
    <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label">Email address</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
      <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword1" class="form-label">Password</label>
      <input type="password" class="form-control" id="exampleInputPassword1">
    </div>
    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1">
      <label class="form-check-label" for="exampleCheck1">Check me out</label>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</div>