import React from 'react';
import SideNav from '@/components/SideNav';
import SideBar from '@/components/SideBar';

export const metadata = {
  title: 'ProCord | Chat',
  description:'Dive into a new world of networking!!'

}

function layout({children}) {
  return (

      <div className=' relative'>
      <div className='sidebar absolute h-screen items-center'>
        <SideNav/>
      </div>
      <div className=' ml-14 pl-2'>
            <div className=' bg-white h-screen w-full'>{children}</div>
      </div>
      </div>

  )
}

export default layout;