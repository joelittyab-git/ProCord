import React from 'react';
import { IconButton } from '@mui/material';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import GroupIcon from '@mui/icons-material/Group';
import PersonIcon from '@mui/icons-material/Person';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import Divider from '@mui/material/Divider';

function SideBar() {
  return (
    <div className=' bg-black h-screen flex align-middle items-center  w-10 sm:w-14 md:w-17 lg:w-14 xl:w-16 2xl:w-17 transition-all duration-300 hover:w-60 group'>
     <div className=' w-full pb-10 space-y-6'>
          <div className='flex items-center justify-center '>
               <IconButton color='white'>
                    <ExitToAppIcon htmlColor='#c2c2c2' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl hover:text-white'/>
               </IconButton>
          </div>
     
          <div className='flex justify-center items-center'>
               <IconButton color='white'>
                    <GroupIcon htmlColor='#c2c2c2' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl hover:text-white '/>
                    <p class="transition hidden  group-hover:block  text-white  text-lg  pl-2  ">Group</p>
               </IconButton>
          </div>
     
          <div className='flex justify-center items-center'>
               <IconButton color='white'>
                    <PersonIcon htmlColor='#c2c2c2' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl  hover:text-white '/>
               </IconButton>
          </div>

          <div className="absolute bottom-3 justify-center w-full">
               <div className='flex justify-center items-end pt-6 '>
                    <IconButton color='white'>
                         <AccountCircleIcon htmlColor='white' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl  hover:text-white  '/>
                    </IconButton>
               </div>
          </div>
     </div>
    </div>
  )
}

export default SideBar;