export default function auth({next, store}) {
  if (!store.getters.auth.loggedIn || !store.getters.auth.isActive) {
    return next({
      name: 'login'
    })
  }
  return next()
}