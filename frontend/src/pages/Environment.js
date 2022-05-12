import React from "react";
import ReactEcharts from "echarts-for-react"; 
import TextGraph from "../components/TestGraph";
import PollutantMap from "../components/PollutantMap";
import PollutantGraph from "../components/PollutantGraph";
export default function Environment(props){


    var mapStyle="mapbox://styles/zhiqingw/cl32oa5lb000f14nxv4ffxees"
    
    var mapboxAccessToken="pk.eyJ1IjoiemhpcWluZ3ciLCJhIjoiY2t0anJ1Y2xoMWV6NTJ3bm1xNnBoNWt0eiJ9.oBR-Za509LFKgj2khrxf2g"
    var interactiveLayerIds=['pollutant']
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Tweets Overview</a></li>
                    <li class="active"><a href="/environment">Environment</a></li>
                    <li><a href="/health">Health</a></li>
                </div>
            </header>
            <h1>
                Second
            </h1>
            <PollutantMap mapStyle={mapStyle} mapboxAccessToken={mapboxAccessToken} interactiveLayerIds={interactiveLayerIds}/>
            <div className="health-left">
            <PollutantGraph url={props.url} header={props.header}/>
            </div>
        </div>

    )
}