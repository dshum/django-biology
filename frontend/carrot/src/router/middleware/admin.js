export default function admin({next, store}) {
  if (!store.getters.auth.isStaff) {
    return next({
      name: 'dashboard'
    })
  }

  return next()
}