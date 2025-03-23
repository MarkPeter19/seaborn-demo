import { createRouter, createWebHistory } from "vue-router";
import CompareView from "@/pages/CompareView.vue";
import LandingPage from "@/pages/LandingPage.vue";
import ChartPlayGround from "@/pages/ChartPlayGround.vue";
import RandomChart from "@/pages/RandomChart.vue";

const routes = [
  {
    path: "/",
    name: "Landing",
    component: LandingPage,
  },
  {
    path: "/playground",
    name: "ChartPlayground",
    component: ChartPlayGround,
  },
  {
    path: "/compare",
    name: "Compare",
    component: CompareView,
  },
  {
    path: "/random",
    name: "Random",
    component: RandomChart,
  },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
