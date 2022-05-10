import React from "react";
import ReactEcharts from "echarts-for-react"; 
import HospotalMap from "../components/HospitalMap";
import TextGraph from '../components/TestGraph'
export default function Health(props){


    
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Overview</a></li>

                    <li ><a href="/environment">Environment</a></li>
                    <li class="active"><a href="/health">Health</a></li>
                </div>
            </header>
            <h1>
                Health
            </h1>
            <HospotalMap />
            <TextGraph url={props.url} header={props.header}/>
        </div>

    )
}