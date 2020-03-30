import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);
const routes = [
  { path: "/", component: () => import("@/views/Index") }, //引导页
  { path: "/painter", component: () => import("@/views/Painter") }, //画家详情页
  { path: "/craft", component: () => import("@/views/Craft") }, //作品详情页
  { path: "/gallery", component: () => import("@/views/Gallery") }, //画廊
  { path: "/analyse", component: () => import("@/views/Analyse") }, //作品分析页
  { path: "/home", component: () => import("@/views/Home") }, //个人主页
  { path: "/model", component: () => import("@/views/Model") }, //模型管理页
  { path: "/data", name: "story", component: () => import("@/views/Data") } //数据管理页
];
router.beforeEach((to, from, next) => {
  //路由守卫
  if (to.matched.some(res => res.meta.isLogin)) {
    //判断是否需要登录
    if (sessionStorage["username"]) {
      next();
    } else {
      next({ path: "/login", query: { redirect: to.fullPath } });
    }
  }
});
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});
export default router;
