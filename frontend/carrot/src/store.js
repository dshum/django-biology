import Vuex from 'vuex'

export default new Vuex.Store({
  state: {
    user: {
      loggedIn: false,
      isActive: false,
      isStaff: false,
    }
  },
  getters: {
    auth(state) {
      return state.user
    }
  }
})