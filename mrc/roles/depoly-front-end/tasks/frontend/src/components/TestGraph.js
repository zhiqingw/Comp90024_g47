import React from "react";
import ReactEcharts from "echarts-for-react"; 

export default class TestGraph extends React.Component {
    


    constructor(props) {
        super(props);
        
        this.state = {option: {}};
      }


    componentDidMount(){
        var eva = [0,0,0,0,0,0,0,0,0,0,0,0]
        var temp = [0,0,0,0,0,0,0,0,0,0,0,0]
        var pre = [0,0,0,0,0,0,0,0,0,0]
        this.setState({option: this.initialOption(eva,temp, pre)})
        this.fetchOption();
        
        
    }

    



    render() {
      return <ReactEcharts option={this.state.option} />;
    }

    fetchOption(){
        
        // headers.append('Access-Control-Allow-Origin','*')

        fetch(this.props.url + '/twitter/8914b8269ed7f98dffcb73a6aa0012ee', {
            method: "GET",
            headers: this.props.header,
            // body: JSON.stringify({
            //     name: "admin",
            //     password: "admin"
            
            // }),
        }).then((response) => response.json())
        .then((data) => {
            this.setState({option: this.initialOption(data.evaporation, data.Temperature, data.Precipitation)})
            
            // this.initialOption(data.Evaporation)
        });
    }

    initialOption(evaporation, temperature, precipitation){
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
            data: ['Evaporation', 'Precipitation', 'Temperature']
            },
            xAxis: [
            {
                type: 'category',
                axisTick: {
                alignWithLabel: true
                },
                // prettier-ignore
                data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            }
            ],
            yAxis: [
            {
                type: 'value',
                name: 'Evaporation',
                position: 'right',
                alignTicks: true,
                axisLine: {
                show: true,
                lineStyle: {
                    color: colors[0]
                }
                },
                axisLabel: {
                formatter: '{value} ml'
                }
            },
            {
                type: 'value',
                name: 'Precipitation',
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
                formatter: '{value} ml'
                }
            },
            {
                type: 'value',
                name: '温度',
                position: 'left',
                alignTicks: true,
                axisLine: {
                show: true,
                lineStyle: {
                    color: colors[2]
                }
                },
                axisLabel: {
                formatter: '{value} °C'
                }
            }
            ],
            series: [
            {
                name: 'Evaporation',
                type: 'bar',
                data: evaporation
            },
            {
                name: 'Precipitation',
                type: 'bar',
                yAxisIndex: 1,
                data: precipitation
            },
            {
                name: 'Temperature',
                type: 'line',
                yAxisIndex: 2,
                data: temperature
            }
            ]
        }
        return option;
    }
  }
