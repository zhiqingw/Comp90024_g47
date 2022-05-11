import React from "react";
import ReactEcharts from "echarts-for-react"; 
import HospotalMap from "../components/HospitalMap";
import TextGraph from '../components/TestGraph'
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
                </div>
            </header>
            <h1>
                Health
            </h1>
            <HospotalMap mapStyle={mapStyle} mapboxAccessToken={mapboxAccessToken} interactiveLayerIds={interactiveLayerIds}/>
            <div className="health-left">
            <TextGraph url={props.url} header={props.header}/>
            </div>
            <div className="health-right">
            <TextGraph url={props.url} header={props.header}/>
            </div>
        </div>

    )
}