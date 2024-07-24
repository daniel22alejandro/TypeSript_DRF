import { login } from "../store"; 
import { useMutation } from "@tanstack/react-query"; 
import { useState } from "react"; 
import { useForm } from "react-hook-form"; 
import { useNavigate } from "@tanstack/react-router"; 

// Definimos el tipo de datos que esperamos recibir del formulario
type Response = {
  username: string; // Nombre de usuario
  password: string; // Contraseña
};

// Definimos el componente funcional de inicio de sesión
const LoginComponent = () => {
  const navigate = useNavigate(); // Hook para cambiar de rutas
  const [messageError, setErrorMessage] = useState(""); // Estado para manejar mensajes de error

  // Configuración del hook de react-hook-form para gestionar el formulario
  const {
    register, // Función para registrar los campos del formulario
    handleSubmit, // Función para manejar el envío del formulario
    formState: { errors }, // Estado del formulario y errores
  } = useForm<Response>(); // Inicializamos el hook con el tipo de datos esperado

  // Configuración del hook de react-query para manejar la mutación del login
  const useMutationLogin = useMutation({
    mutationFn: login, // Función que realiza la operación de login
    onSuccess: (data) => {
      console.log("Usuario autorizado", data); // Mensaje en consola si el login es exitoso
      navigate({ to: "/home" }); // Redirige a la página de inicio (ruta /home) en caso de éxito
    },
    onError: (error: Error) => {
      console.log("Error:", error.message); // Mensaje en consola si hay un error
      setErrorMessage(error.message); // Establece el mensaje de error para mostrarlo en la interfaz
    },
  });

  // Función que se llama al enviar el formulario
  const onsubmitData = (data: Response) => {
    useMutationLogin.mutate(data); // Ejecuta la mutación de login con los datos del formulario
    console.log("", data); // Mensaje en consola con los datos enviados
  };

  // Renderizado condicional del mensaje de error
  const errorApi = messageError ? (
    <p className="text-red-500">{messageError}</p>
  ) : null;

  // Estructura del componente de inicio de sesión
  return (
    <div className="flex flex-col items-center w-full">
      <div className="flex flex-col items-start w-full pl-4 pt-4">
        <div
          className="w-20 h-20 bg-cover bg-center"
        ></div>
      </div>
      <div className="flex items-center justify-center w-full mt-24 h-auto shadow-lg rounded-lg p-8 bg-white">
        <form
          className="flex flex-col gap-4 w-full max-w-md"
          onSubmit={handleSubmit(onsubmitData)}
        >
          <div className="w-full text-center">
            <h1 className="text-2xl font-bold">Coffco</h1>
          </div>
          {errorApi} {/* Muestra el mensaje de error si existe */}
          <label className="font-semibold">Usuario:</label>
          <input
            className="text-black h-10 rounded-lg border border-gray-300 p-2"
            type="text"
            id="username"
            placeholder="Usuario"
            {...register("username", {
              required: {
                value: true,
                message: "El nombre de usuario es obligatorio",
              },
            })}
          />
          {errors.username && (
            <p className="text-red-500">{errors.username.message}</p>
          )}
          <label className="font-semibold">Contraseña:</label>
          <input
            type="password"
            className="text-black h-10 rounded-lg border border-gray-300 p-2"
            id="password"
            {...register("password", {
              required: {
                value: true,
                message: "La contraseña es obligatoria",
              },
            })}
          />
          {errors.password && (
            <p className="text-red-500">{errors.password.message}</p>
          )}
          <input
            className="bg-blue-500 text-white rounded-lg w-full h-10 mt-4 hover:bg-blue-600"
            type="submit"
            value="Entrar"
          />
        </form>
      </div>
    </div>
  );
};

// Exportamos el componente para que pueda ser utilizado en otras partes de la aplicación
export default LoginComponent;
