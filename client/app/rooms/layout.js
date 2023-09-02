import React from 'react';
import SideNav from '@/components/SideNav';
import SideBar from '@/components/SideBar';

function layout({children}) {
  return (
    <main className=' relative'>
      <div className='sidebar absolute h-screen items-center'>
        <SideNav/>
      </div>
      <div className=' ml-14 p-2'>
            <div className=' bg-white h-screen w-full'>{children}</div>
      </div>
    </main>
  )
}

export default layout;