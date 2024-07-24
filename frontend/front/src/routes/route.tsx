import { createRoute } from "@tanstack/react-router";
import { rootRoute } from "./RootRoute"; // Actualización de la importación
import LoginComponent from "../components/LoginType";
import Inicio from "../components/Inicio";

// Definimos la ruta para la página de inicio
export const indexRoute = createRoute({
  getParentRoute: () => rootRoute, // Indica que es una ruta hija de rootRoute
  path: "/", // Ruta principal
  component: function Index() {
    return <div><LoginComponent/></div>;
  },
});

// Definimos la ruta para la página de inicio
export const inicioRoute = createRoute({
  getParentRoute: () => rootRoute, // Indica que es una ruta hija de rootRoute
  path: "/inicio", // Ruta /home
  component: function Index() {
    return <Inicio/>;
  },
});
