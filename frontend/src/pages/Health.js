import React from "react";
import ReactEcharts from "echarts-for-react"; 
import HospitalMap from "../components/HospitalMap";
import HospitalChart from '../components/HospitalChart'
export default function Health(props){


    var mapStyle="mapbox://styles/zhiqingw/cl2wqsq2z000q15o4tcesyqfs"
    
    var mapboxAccessToken="pk.eyJ1IjoiemhpcWluZ3ciLCJhIjoiY2t0anJ1Y2xoMWV6NTJ3bm1xNnBoNWt0eiJ9.oBR-Za509LFKgj2khrxf2g"
    var interactiveLayerIds=['hospital']
    // var html = <h1>{this.state.features.rd_seg_dsc}</h1>

    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li><a href="/">Tweets Overview</a></li>
                    <li ><a href="/environment">Environment</a></li>
                    <li class="active"><a href="/health">Health</a></li>
                    <li><a href="/entertainment">Entertainment</a></li>
                </div>
            </header>
            <div className="map-title">Melbourne Hospital Capacity Map</div>
            <HospitalMap mapStyle={mapStyle} mapboxAccessToken={mapboxAccessToken} interactiveLayerIds={interactiveLayerIds}/>
            <div class="map-overlay" id="map-legend"></div>
            <div className="health-left">
            <div className="chart-title">Twitter sentiment data and hospital capacity data</div>
            <HospitalChart url={props.url} header={props.header}/>
            </div>
            
        </div>

    )
}