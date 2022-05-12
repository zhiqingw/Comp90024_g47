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
            <div className="map-title">Melbourne Restaurant, Cafe, Bar Seats Capacity Map</div>
            <EntertainmentMap mapStyle={mapStyle} mapboxAccessToken={mapboxAccessToken} interactiveLayerIds={interactiveLayerIds}/>
            <div className="health-left">
            <div className="chart-title">Twitter sentiment data and Restaurant, Cafe, Bar Seats Capacity data</div>
            <EntertainmentChart url={props.url} header={props.header}/>
            </div>
        </div>

    )
}