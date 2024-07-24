import axios from "axios";

//Instancia de axios con la base url del api
const Api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", 
});

// type para definir el tipo de respuesta de la funcion login
type LoginResponse = {
  message: string;
};

// type para definir el tipo que se envia a la solicitud del login
type LoginData = {
  username: string;
  password: string;
};

// Función para manejar el login
export const login = async (data: LoginData): Promise<LoginResponse> => {
  try {
    const response = await Api.post("auth/login/", data);
    return response.data;
  } catch (error: any) {
    // Manejo de errores de la respuesta del servidor
    if (error.response) {
      // Error de la respuesta del servidor
      throw new Error(error.response.data.detail || "Error desconocido del servidor");
    } else if (error.request) {
      // No se recibió respuesta del servidor
      throw new Error("No se recibió respuesta del servidor");
    } else {
      // Error al realizar la solicitud
      throw new Error("Error al realizar la solicitud");
    }
  }
};
