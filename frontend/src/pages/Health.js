import React from "react";
import ReactEcharts from "echarts-for-react"; 
import HospotalMap from "../components/HospitalMap";
export default function Health(){


    
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Home</a></li>

                    <li ><a href="/f1">Overview</a></li>
                    <li class="active"><a href="/health">Health</a></li>
                </div>
            </header>
            <h1>
                Health
            </h1>
            <HospotalMap />
        </div>

    )
}