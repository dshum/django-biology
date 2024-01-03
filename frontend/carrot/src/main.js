import {createApp} from 'vue'
import './style.css'
import router from './routers'
import App from './App.vue'

/* import the fontawesome core */
import {library} from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
/* import specific icons */
import {
  faCarrot,
  faGraduationCap,
  faPieChart,
  faListCheck,
  faHouse,
  faChevronRight
} from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faCarrot, faGraduationCap, faPieChart, faListCheck, faHouse, faChevronRight)

const app = createApp(App)
  .component('font-awesome-icon', FontAwesomeIcon)

app.use(router)
app.mount('#app')
