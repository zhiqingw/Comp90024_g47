// Author:      Zhiqing Wu
// Student id:  931919
// Description: Chart for visualising the pollutant data

import React from "react";
import ReactEcharts from "echarts-for-react"; 

export default class PollutantGraph extends React.Component {
    


    constructor(props) {
        super(props);
        
        this.state = {option: {}};
      }


    componentDidMount(){
        var eva = [0,0,0,0,0]
        var temp = [0,0,0,0,0]
        var pre = [0,0,0,0,0]
        var lga = ["","","","",""]
        this.setState({option: this.initialOption(eva,temp, pre)})
        this.fetchOption();
        
        
    }

    



    render() {
      return <ReactEcharts option={this.state.option} />;
    }

    fetchOption(){
        
        // headers.append('Access-Control-Allow-Origin','*')

        fetch(this.props.url + '/result/d428bceb0b93d1b0b4c7eb8dc0e1cfb9', {
            method: "GET",
            headers: this.props.header,
            // body: JSON.stringify({
            //     name: "admin",
            //     password: "admin"
            
            // }),
        }).then((response) => response.json())
        .then((data) => {
            this.setState({option: this.initialOption(data.positive_tweets, data.negative_tweets, data.pollutant,data.lga)})
            
            // this.initialOption(data.Evaporation)
        });
    }

    initialOption(positive_tweets, negative_tweets, capacity,lga){
        var colors = ['#5470C6', '#91CC75', '#EE6666'];
        var option = {
            color: colors,
            tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            }
            },
            grid: {
            right: '20%'
            },
            toolbox: {
            feature: {
                dataView: { show: true, readOnly: false },
                restore: { show: true },
                saveAsImage: { show: true }
            }
            },
            legend: {
            data: ['Positive Tweets', 'Negative Tweets', 'Pollutant']
            },
            xAxis: [
            {
                axisLabel:{
                    show: true,
                    rotate: 40,
                },
                type: 'category',
                axisTick: {
                alignWithLabel: true
                },
                // prettier-ignore
                data: lga
            }
            ],
            yAxis: [
            {
                type: 'value',
                name: 'Positive',
                position: 'right',
                alignTicks: true,
                axisLine: {
                show: true,
                lineStyle: {
                    color: colors[0]
                }
                },
                axisLabel: {
                formatter: '{value}'
                }
            },
            {
                type: 'value',
                name: 'Negative',
                position: 'right',
                alignTicks: true,
                offset: 80,
                axisLine: {
                show: true,
                lineStyle: {
                    color: colors[1]
                }
                },
                axisLabel: {
                formatter: '{value}'
                }
            },
            {
                type: 'value',
                name: 'Pollutant',
                position: 'left',
                // alignTicks: true,
                axisLine: {
                show: true,
                lineStyle: {
                    color: colors[2]
                }
                },
                axisLabel: {
                formatter: '{value}'
                },
                
            }
            ],
            series: [
            {
                name: 'Positive Tweets',
                type: 'bar',
                data: positive_tweets
            },
            {
                name: 'Negative Tweets',
                type: 'bar',
                yAxisIndex: 1,
                data: negative_tweets
            },
            {
                name: 'Pollutant',
                type: 'line',
                yAxisIndex: 2,
                data: capacity
            }
            ]
        }
        return option;
    }
  }
