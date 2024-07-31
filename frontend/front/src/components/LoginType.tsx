import { login } from "../store"; 
import { useMutation } from "@tanstack/react-query"; 
import { useState } from "react"; 
import { useForm } from "react-hook-form"; 
import { useNavigate } from "@tanstack/react-router"; 


type Response = {
  numero_documento: string; 
  password: string; 
};


const LoginComponent = () => {
  const navigate = useNavigate(); 
  const [messageError, setErrorMessage] = useState("");
  

  const {
    register, 
    handleSubmit, 
    formState: { errors }, 
  } = useForm<Response>(); 

  // Configuración del hook de react-query para manejar la mutación del login
  const useMutationLogin = useMutation({
    mutationFn: login, 
    onSuccess: (data) => {
      console.log("Usuario autorizado", data); 
      navigate({ to: "/home" }); 
    },
    onError: (error: Error) => {
      console.log("Error:", error.message);
      setErrorMessage(error.message);
    },
  });

  // Función que se llama al enviar el formulario
  const onsubmitData = (data: Response) => {
    useMutationLogin.mutate(data); // Ejecuta la mutación de login con los datos del formulario
    console.log("", data); 
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
            id="numero_documento"
            placeholder="Usuario"
            {...register("numero_documento", {
              required: {
                value: true,
                message: "El nombre de usuario es obligatorio",
              },
            })}
          />
          {errors.numero_documento && (
            <p className="text-red-500">{errors.numero_documento.message}</p>
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


export default LoginComponent;
