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
        
        // headers.append('Access-Control-Allow-Origin','*')

        fetch(this.props.url + '/result/c414f40fbf9a3fa3d034c86b59c46938', {
            method: "GET",
            headers: this.props.header,
            // body: JSON.stringify({
            //     name: "admin",
            //     password: "admin"
            
            // }),
        }).then((response) => response.json())
        .then((data) => {
            this.setState({option: this.initialOption(data.data, data.indicator)})
            
            // this.initialOption(data.Evaporation)
        });
    }

    initialOption(data, indicator){
        var option = {
            
            legend: {
              data: ['Most positive LGA', 'Most negative LGA'],
            },
            radar: {
              // shape: 'circle',
              indicator: indicator
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
