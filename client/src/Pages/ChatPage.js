import React from 'react';
import client from './../Configurations/Client';
import { ChatNavigation } from '../Components/WestNavigation/ChatNavigation';
import './Stylesheets/ChatPage.css';
import GroupList from '../Components/GroupList/GroupList';
function ChatPage() {
  return (
    <div className='min-h-screen grid bg-slate-950'>
      <div className="fixed top-0 left-0 h-screen flex ">
        <ChatNavigation/>
        <GroupList/>
      </div>
    </div>
  )
}

export default ChatPage;