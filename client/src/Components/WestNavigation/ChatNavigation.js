import React from 'react';
import './ChatNavigation.css';
import GroupIcon from '@mui/icons-material/Group';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import Stack from '@mui/material/Stack';
import GroupsIcon from '@mui/icons-material/Groups';
import Person3Icon from '@mui/icons-material/Person3';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import { useState } from 'react';
import { useEffect } from 'react';



export const ChatNavigation = () => {

  const [iconSize, setIconSize] = useState();
  const [navSize, setNavSize] = useState();

  const matchQuery = () => {
    var x = window.matchMedia("(min-width:800px) and (max-width: 1000px)");
    if(x.matches){
      setIconSize("large");
      setNavSize("16");
      console.log("large")
    }else{
      setIconSize("medium");
      setNavSize("10");
      console.log("medium");
  }
  }

  useEffect(
    ()=>matchQuery,
    []  
  )

 


  return (
    <div className={" bg-black h-screen  text-gray-400  align-middle w-16 "+navSize}>
      <div className='justify-center align-middle  grid h-screen place-items-center pb-20'>
      <Stack direction={"column"} spacing={2}>
        <IconButton aria-label="delete" size={iconSize}>
          <GroupsIcon htmlColor='white' fontSize={iconSize}/>
        </IconButton>
        <IconButton aria-label="delete" size={iconSize}>
          <Person3Icon htmlColor='white' fontSize={iconSize}/>
        </IconButton>
        <IconButton aria-label="delete" size={iconSize}>
          <ExitToAppIcon htmlColor='white' fontSize={iconSize}/>
        </IconButton>
      </Stack>
      </div>
    </div>
  )
}
