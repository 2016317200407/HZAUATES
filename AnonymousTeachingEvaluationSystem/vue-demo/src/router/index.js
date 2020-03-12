import Vue from 'vue'
import Router from 'vue-router'
import homepage from '@/components/homepage'
import teacherinformation from '@/components/teacherinformation'
import classinformation from '@/components/classinformation'
Vue.use(Router)
export default new Router({
  mode:'history',
  routes: [
    {
      path: '/homepage',
      name: 'homepage',
      component: homepage
    },
    {
      path: '/',
      name: 'homepage',
      component: homepage
    },
    {
      path:'/teacherinformation/:username',
      name:'teacherinformation',
      component:teacherinformation
    },
    {
      path:'/classinformation/:classname',
      name:'classinformation',
      component:classinformation
    }

  ]
})