import logo from './logo.svg';
import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "../src/pages/Home.js"
import Second from "../src/pages/Second.js"
import Health from './pages/Health';
function App() {
  return (
  <Router>
    <Routes>
      <Route exact path='/' element={<Home/>}/>
    </Routes>
    <Routes>
      <Route exact path='/f1' element={<Second/>}/>
    </Routes>
    <Routes>
      <Route exact path='/health' element={<Health/>}/>
    </Routes>
  </Router>
  );
}

export default App;
