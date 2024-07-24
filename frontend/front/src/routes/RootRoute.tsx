import { Outlet, Link, createRootRoute } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/router-devtools";

// Definimos la ruta raíz usando TanStack Router
export const rootRoute = createRootRoute({
  // Componente que define la estructura principal de la aplicación
  component: () => (
    <>
      <div>
        <Link to="/">Inicio</Link>
      </div>
      <div>
        <Link to="/home">Home</Link>
      </div>
      <hr />
      {/* Outlet se usa para renderizar rutas hijas */}
      <Outlet />
      {/* Herramientas de desarrollo de TanStack Router */}
      <TanStackRouterDevtools />
    </>
  ),
});
