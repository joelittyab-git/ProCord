import React from 'react';

function layout({children}) {
  return (
    <main>
     <div className='flex'>
          <div className='sidebar absolute h-screen bg-black w-10 sm:w-14 md:w-17 lg:w-14 xl:w-16 2xl:w-17'>

          </div>
          <div className=' bg-white w-screen h-screen'>{children}</div>
     </div>
    </main>
  )
}

export default layout