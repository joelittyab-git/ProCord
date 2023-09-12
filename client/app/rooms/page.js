"use client";

import Image from 'next/image';
import SideBar from '@/components/SideBar';
import axios from 'axios';
import { useState, useEffect } from 'react';
import { headers } from '@/next.config';

export default function Room() {

  // useEffect(
  //   ()=>{
  //     async function fetchData(){
  //       const response = await axios.post(
  //         "http://127.0.0.1:8000/server/user/auth/",
  //         {
  //           "username":"admin",
  //           "password":"Password123"
  //         }
  //       );
  //       console.log(response);
  //     }
  //     fetchData();
  //   },
  //   []
  // )

  return (
    <main className=' bg-black h-screen'>
      <SideBar />
    </main>
  )
}
