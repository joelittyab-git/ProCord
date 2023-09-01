"use client";
import { useEffect } from "react";
import axios from "axios";

class Http{

     static _client = null;

     static setAuthToken() {
          const key = "";
          const authorization = window.localStorage.getItem("Authorization");
          if(authorization!==null){
               this._client.defaults.headers.common["Authorization"] = key;
          }
     }

     static get Client(){
          this._client =  axios.create(
               {
                    baseURL:"http://localhost:8000",
                    timeout:4000
               }
          )
          console.log(this._client);

          this.setAuthToken();
          return this._client;
     }
     
     static set Client(client){
          console.error("Cannot initialize the api client");
     }

     
}
export default Http;