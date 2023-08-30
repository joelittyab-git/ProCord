import React from 'react';
import SideBar from '@/components/SideBar';

function layout({children}) {
  return (
    <main className=''>
     <div className='flex'>
          <div className='sidebar absolute h-screen items-center'>
               <SideBar/>
          </div>
          <div className=' bg-white w-screen h-screen'>{children}</div>
     </div>
    </main>
  )
}

export default layout