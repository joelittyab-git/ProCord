import React from 'react';
import SideBar from '@/components/SideBar';

function layout({children}) {
  return (
    <main>
     <div className='flex'>
          <div className='sidebar absolute h-screen w-10 sm:w-14 md:w-17 lg:w-14 xl:w-16 2xl:w-17 items-center  transition-all duration-300 hover:w-60'>
               <SideBar/>
          </div>
          <div className=' bg-white w-screen h-screen'>{children}</div>
     </div>
    </main>
  )
}

export default layout