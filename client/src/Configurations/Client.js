import axios from 'axios';

//extracting authentication token for backend
const headers_d = {}
const authToken = localStorage.getItem("Authorization");

if(authToken!==null){
     headers_d = {
          Authorization:authToken
     }
}
const client = axios.create({
     baseURL:'http://localhost:8000',
     timeout:5000,
     headers:headers_d
})

export default client;