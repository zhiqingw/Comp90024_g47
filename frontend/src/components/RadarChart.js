import React from "react";
import ReactEcharts from "echarts-for-react"; 

export default class RadarChart extends React.Component {
    


    constructor(props) {
        super(props);
        
        this.state = {option: {}};
      }


    componentDidMount(){
        var eva = [0,0,0,0,0,0,0,0,0,0,0,0]
        var temp = [0,0,0,0,0,0,0,0,0,0,0,0]
        var pre = [0,0,0,0,0,0,0,0,0,0]
        this.setState({option: this.initialOption(eva,temp, pre)})
        // this.fetchOption();
        
        
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
        var option = {
            title: {
              text: 'Basic Radar Chart'
            },
            legend: {
              data: ['Allocated Budget', 'Actual Spending']
            },
            radar: {
              // shape: 'circle',
              indicator: [
                
                { name: 'Health', max: 10000 },
                { name: 'Education', max: 30000 },
                { name: 'Environment', max: 30000 },
              ]
            },
            series: [
              {
                name: 'Budget vs spending',
                type: 'radar',
                data: [
                  {
                    value: [4200, 3000, 20000],
                    name: 'Allocated Budget'
                  },
                  {
                    value: [5000, 14000, 28000],
                    name: 'Actual Spending'
                  }
                ]
              }
            ]
          };
        return option;
    }
  }
