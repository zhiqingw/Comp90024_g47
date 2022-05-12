import React from "react";
import ReactEcharts from "echarts-for-react"; 
import PollutantGraph from "../components/PollutantGraph";
import EntertainmentMap from "../components/EntertainmentMap";
import EntertainmentChart from "../components/EntertainmentChart";
export default function Entertainment(props){


    var mapStyle="mapbox://styles/zhiqingw/cl331hvec000616pq3gazc13x"
    
    var mapboxAccessToken="pk.eyJ1IjoiemhpcWluZ3ciLCJhIjoiY2t0anJ1Y2xoMWV6NTJ3bm1xNnBoNWt0eiJ9.oBR-Za509LFKgj2khrxf2g"
    var interactiveLayerIds=['seat']
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Tweets Overview</a></li>
                    <li><a href="/environment">Environment</a></li>
                    <li><a href="/health">Health</a></li>
                    <li class="active"><a href="/entertainment">Entertainment</a></li>
                </div>
            </header>
            <h1>
                Second
            </h1>
            <EntertainmentMap mapStyle={mapStyle} mapboxAccessToken={mapboxAccessToken} interactiveLayerIds={interactiveLayerIds}/>
            <div className="health-left">
            <EntertainmentChart url={props.url} header={props.header}/>
            </div>
        </div>

    )
}