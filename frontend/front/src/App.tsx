import { RouterProvider } from "@tanstack/react-router";
import { rootRoute } from "./routes/RootRoute.tsx";
import { indexRoute, inicioRoute } from "./routes/route.tsx";
import { createRouter } from "@tanstack/react-router";

// Configuramos el árbol de rutas. 
// rootRoute es la ruta raíz y a ella se le añaden las rutas hijas: indexRoute e inicioRoute.
const routeTree = rootRoute.addChildren([indexRoute, inicioRoute]);

// Creamos una instancia del enrutador utilizando el árbol de rutas configurado.
// Esta instancia se encargará de gestionar la navegación y el enrutamiento en la aplicación.
const router = createRouter({ routeTree });

function App() {
  return (
    // El RouterProvider proporciona el enrutador a toda la aplicación.
    <RouterProvider router={router} />
  );
}

export default App;
