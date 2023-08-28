import React from 'react';
import client from './../Configurations/Client';
import { ChatNavigation } from '../Components/WestNavigation/ChatNavigation';
import './Stylesheets/ChatPage.css';
function ChatPage() {
  return (
    <div className='min-h-screen grid bg-slate-950'>
      <div class="relative h-32 w-32 ...">
        <ChatNavigation/>
      </div> 
    </div>
  )
}

export default ChatPage;