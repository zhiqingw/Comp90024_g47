import React from "react";
import ReactEcharts from "echarts-for-react"; 

export default class DoughnutChart extends React.Component {
    


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
            tooltip: {
              trigger: 'item'
            },
            legend: {
              top: '5%',
              left: 'center'
            },
            series: [
              {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: true,
                itemStyle: {
                  borderRadius: 10,
                  borderColor: '#fff',
                  borderWidth: 2
                },
                label: {
                  show: false,
                  position: 'center'
                },
                // emphasis: {
                //   label: {
                //     show: true,
                //     fontSize: '40',
                //     fontWeight: 'bold'
                //   }
                // },
                labelLine: {
                  show: false
                },
                data: [
                  { value: 2348, name: 'Positive tweets' },
                  { value: 735, name: 'Negative tweets' },
                  
                ]
              }
            ]
          };
        return option;
    }
  }
