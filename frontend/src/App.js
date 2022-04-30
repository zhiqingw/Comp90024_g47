import logo from './logo.svg';
import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "../src/pages/Home.js"
import Second from "../src/pages/Second.js"
function App() {
  return (
  <Router>
    <Routes>
      <Route exact path='/' element={<Home/>}/>
    </Routes>
    <Routes>
      <Route exact path='/f1' element={<Second/>}/>
    </Routes>
  </Router>
  );
}

export default App;
