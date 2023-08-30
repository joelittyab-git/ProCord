import axios from "axios";

class HttpClient{

     static Client = axios.create(
          {
               baseURL:"http://localhost:8000",
               timeout:4000
          }
     )

     static setAuthToken = () => {
          const key = "";
          const authorization = localStorage.getItem("Authorization");
          if(authorization!==null){
               HttpClient.Client.defaults.headers.common["Authorization"] = key;
          }
     }

     
}
export default HttpClient;