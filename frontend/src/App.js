// Author:      Zhiqing Wu
// Student id:  931919
// Description: Front End main program

import logo from './logo.svg';
import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "../src/pages/Home.js"
import Health from './pages/Health';
import Environment from './pages/Environment.js';
import Entertainment from './pages/Entertainment';
function App() {
  var url = "http://172.26.134.66:5984";
  
  var headers = new Headers();
  headers.append('Authorization', 'Basic ' + btoa("admin" + ':' + "admin"));
  return (
  <Router>
    <Routes>
      <Route exact path='/' element={<Home url={url} header={headers}/>}/>
    </Routes>
    <Routes>
      <Route exact path='/environment' element={<Environment url={url} header={headers}/>}/>
    </Routes>
    <Routes>
      <Route exact path='/health' element={<Health url={url} header={headers}/>}/>
    </Routes>
    <Routes>
      <Route exact path='/entertainment' element={<Entertainment url={url} header={headers}/>}/>
    </Routes>
  </Router>
  );
}

export default App;
