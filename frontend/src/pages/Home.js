// Author:      Zhiqing Wu
// Student id:  931919
// Description: Home page

import React from "react";
import axios from 'axios';
import fetchToCurl from 'fetch-to-curl';
import RadarChart from "../components/RadarChart";
import DoughnutChart from "../components/DoughnutChart";
import DoughnutChartNegative from "../components/DoughnutChartNegative";

export default function Home(props){

    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li class="active"><a href="/">Tweets Overview</a></li>
                    <li><a href="/environment">Environment</a></li>
                    <li><a href="/health">Health</a></li>
                    <li><a href="/entertainment">Entertainment</a></li>
                </div>
            </header>
    
            
           
            <div className="doughnut-chart-left">
                <div className="chart-title-home">Most Positive Lga</div>
                <DoughnutChart url={props.url} header={props.header}/>
            </div>
            <div className="doughnut-chart-right">
            <div className="chart-title-home">Most Negative Lga</div>
                <DoughnutChartNegative url={props.url} header={props.header}/>
            </div>
            
            <div className="radar-chart">
            <div className="chart-title-home">The livability scale for the most negative and positive lga</div>
            <RadarChart url={props.url} header={props.header}/>
            </div>

            <div className="application-overview">
                This website demonstrated if Melbourne a livable city by examined the livability scales include Health, Environment and Entertainment factors, 
                with analysing the correlation between twitter sentiment and hospital capacity, pollutant emission and restaurant capacity respectively.
            </div>
            
     
        </div>

    )
}