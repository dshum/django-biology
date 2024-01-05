import {createApp} from 'vue'
import {createPinia} from 'pinia';
import router from './router/router'
import App from './App.vue'
import './style.css'

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
const pinia = createPinia()

app.component('font-awesome-icon', FontAwesomeIcon)
app.use(pinia)
app.use(router)
app.mount('#app')
