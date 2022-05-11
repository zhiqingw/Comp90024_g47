import React from "react";
import ReactEcharts from "echarts-for-react"; 
import TextGraph from "../components/TestGraph";
export default function Environment(props){


    
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Overview</a></li>
                    <li class="active"><a href="/environment">Environment</a></li>
                    <li><a href="/health">Health</a></li>
                </div>
            </header>
            <h1>
                Second
            </h1>
            <TextGraph url={props.url} header={props.header}/>
        </div>

    )
}