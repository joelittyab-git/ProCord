import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import HomePage from './Pages/HomePage';
import ChatPage from './Pages/ChatPage';
import {BrowserRouter,Route,Routes} from 'react-router-dom';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<HomePage/>}/>
      <Route path='/rooms' element={<ChatPage/> }/>
    </Routes>
  </BrowserRouter>
);

