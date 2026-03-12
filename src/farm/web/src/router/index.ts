import EnvironmentDetail from '@/pages/EnvironmentDetail.vue'
import Envrionments from '@/pages/Envrionments.vue'
import Wizard from '@/pages/Wizard.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Envrionments',
      component: Envrionments
    },
    {
      path: '/environment/:id',
      name: 'Environment Detail',
      component: EnvironmentDetail
    },
    {
      path: '/wizard',
      name: 'Wizard',
      component: Wizard
    }
  ],
})

export default router
