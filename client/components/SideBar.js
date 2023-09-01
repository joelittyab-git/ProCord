"use client";

import React from 'react';
import { IconButton } from '@mui/material';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import GroupIcon from '@mui/icons-material/Group';
import PersonIcon from '@mui/icons-material/Person';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import NotificationsActiveIcon from '@mui/icons-material/NotificationsActive';

function SideBar() {

  return (
    <div className=' bg-black h-screen flex align-middle items-center  w-10 sm:w-14 md:w-17 lg:w-14 xl:w-16 2xl:w-17 overflow-hidden group transition-all duration-700 hover:w-64 z-50'>
     <div className=' w-full pb-10 space-y-6'>
          <div className='flex items-center justify-center group/group1 transition-colors duration-300 hover:bg-blue-600' >
               <IconButton color='white'>
                    <ExitToAppIcon htmlColor='#686868' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl group-hover/group1:text-white transition duration-700 group-hover:-translate-x-10'/>
                    <p className="hidden absolute top-0 left-5 text-lg p-2 text-slate-300 group-hover:block transition duration-300 ease-in-out font-semibold ">Exit</p>
               </IconButton>
          </div>
     
          <div className='flex justify-center items-center group/group2  transition-colors duration-300 hover:bg-blue-600'>
               <IconButton color='white'>
                    <GroupIcon htmlColor='#686868' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl group-hover/group2:text-white transition duration-700 group-hover:-translate-x-10 justify-center'/>
                    <p className="hidden absolute top-0 left-5  text-lg p-2 text-slate-300 group-hover:block transition duration-300 ease-in-out font-semibold">Group</p>
               </IconButton>
          </div>
     
          <div className='flex justify-center items-center group/group3  transition-colors duration-300 hover:bg-blue-600'>
               <IconButton color='white'>
                    <PersonIcon htmlColor='#686868' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl group-hover/group3:text-white transition duration-700 group-hover:-translate-x-10'/>
                    <p className="hidden absolute top-0 left-5 text-lg p-2 text-slate-300 group-hover:block transition duration-300 ease-in-out font-semibold">Messages</p>
               </IconButton>
          </div>

          <div className='flex justify-center items-center group/group4  transition-colors duration-300 hover:bg-blue-600'>
               <IconButton color='white'>
                    <NotificationsActiveIcon htmlColor='#686868' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl group-hover/group4:text-white transition duration-700 group-hover:-translate-x-10 justify-center'/>
                    <p className="hidden absolute top-0 left-5  text-lg p-2 text-slate-300 group-hover:block transition duration-300 ease-in-out font-semibold">Notification</p>
               </IconButton>
          </div>

          <div className="absolute bottom-3 justify-center w-full overflow-hidden items-center">
               <div className='flex justify-center items-center   transition-colors duration-300 hover:bg-blue-600'>
                    <IconButton color='white'>
                         <AccountCircleIcon htmlColor='white' className='text-2xl sm:text-2xl md:text-2xl lg:text-3xl xl:text-3xl 2xl:text-3xl group-hover/group2:text-white transition duration-700 group-hover:-translate-x-10'/>
                         <p className="hidden absolute top-0 left-8 text-lg p-2 text-slate-300 group-hover:block transition duration-300 ease-in-out font-medium">Account</p>
                    </IconButton>
               </div>
          </div>
     </div>
    </div>
  )
}

export default SideBar;