import React from "react";
import ReactEcharts from "echarts-for-react"; 

export default class RadarChart extends React.Component {
    


    constructor(props) {
        super(props);
        
        this.state = {option: {}};
      }


    componentDidMount(){
        var data = [
            {
              value: [0, 0, 0],
              name: 'Most positive LGA'
            },
            {
              value: [0, 0, 0],
              name: 'Most negative LGA'
            }
          ]
        var indicator = [
                
            { name: 'Health', max: 4 },
            { name: 'Education', max: 4 },
            { name: 'Environment', max: 4 },
          ]
        this.setState({option: this.initialOption(data, indicator)})
        this.fetchOption();
        
        
    }

    render() {
      return <ReactEcharts option={this.state.option} />;
    }

    fetchOption(){

        fetch(this.props.url + '/result/c414f40fbf9a3fa3d034c86b59c46938', {
            method: "GET",
            headers: this.props.header,
        }).then((response) => response.json())
        .then((data) => {
            this.setState({option: this.initialOption(data.data, data.indicator)})

        });
    }

    initialOption(data, indicator){
        var legend_data = []
        for(let i = 0; i < data.length; i++){
          legend_data.push(data[i]['name'])
        }
        var option = {
            
            legend: {
              data: legend_data,
            },
            radar: {
              indicator: indicator,
              center: ['50%', '60%']
            },
            series: [
              {
                name: 'Budget vs spending',
                type: 'radar',
                data: data
              }
            ]
          };
        return option;
    }
  }
