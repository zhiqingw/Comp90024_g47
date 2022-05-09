import React from "react";
import ReactEcharts from "echarts-for-react"; 
import TextGraph from "../components/TestGraph";
export default function Second(){


    
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Home</a></li>
                    <li class="active"><a href="/f1">Overview</a></li>
                </div>
            </header>
            <h1>
                Second
            </h1>
            <TextGraph />
        </div>

    )
}