import React from "react";
import ReactEcharts from "echarts-for-react"; 
import PollutantMap from "../components/PollutantMap";
import PollutantGraph from "../components/PollutantGraph";
export default function Environment(props){


    var mapStyle="mapbox://styles/zhiqingw/cl377f4js000114nvsbiuclbo"
    
    var mapboxAccessToken="pk.eyJ1IjoiemhpcWluZ3ciLCJhIjoiY2t0anJ1Y2xoMWV6NTJ3bm1xNnBoNWt0eiJ9.oBR-Za509LFKgj2khrxf2g"
    var interactiveLayerIds=['pollutant']
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Tweets Overview</a></li>
                    <li class="active"><a href="/environment">Environment</a></li>
                    <li><a href="/health">Health</a></li>
                    <li><a href="/entertainment">Entertainment</a></li>
                </div>
            </header>
            <div className="map-title">Melbourne Air Emission Map</div>
            <PollutantMap mapStyle={mapStyle} mapboxAccessToken={mapboxAccessToken} interactiveLayerIds={interactiveLayerIds}/>
            {/* <div class="map-overlay" id="map-legend"></div> */}
            <div className="health-left">
            <div className="chart-title">Twitter sentiment data and air pollution data</div>
            <PollutantGraph url={props.url} header={props.header}/>
            </div>
        </div>

    )
}