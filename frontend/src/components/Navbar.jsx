import React from "react";
import './styles/navbar.css';
import {Route, Routes, Link} from 'react-router-dom';
import SearchBarTop from "./SearchBarTop";

const Navbar = (props) => {
    return (
        <nav>
            <div className="icon">
                <Link to={'/'}> <img src="./logo1.jpg" alt="logo" /> </Link>
                
            </div>
            <Routes>
                <Route path="/results" element={<SearchBarTop/>}/>
                <Route path="*" element={<div></div>}/>
            </Routes>
            <div className="btns">
                {/* <div> <a href="/landing"> home </a></div> */}
                <div> <a href="http://localhost:3000/?"> Home </a></div>
                <div> <a href="http://127.0.0.1:5000/"> Log Out </a></div>
                {/* http://localhost:3000/?
                 */}
                {/* <div>Home</div> */}
                {/* <Link to={'/about'}>About</Link> */}
            </div>
            {/* <div className="btns">
               
                
            </div> */}
        </nav>
    )
}

export default Navbar;