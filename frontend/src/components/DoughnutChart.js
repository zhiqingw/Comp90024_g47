import React from "react";
import ReactEcharts from "echarts-for-react"; 

export default class DoughnutChart extends React.Component {
    


    constructor(props) {
        super(props);
        
        this.state = {option: {}};
      }


    componentDidMount(){
        var data = [
            { value: 0, name: 'Positive tweets' },
            { value: 0, name: 'Negative tweets' },
            
          ]
        this.setState({option: this.initialOption(data)})
        this.fetchOption();
        
        
    }

    



    render() {
      return <ReactEcharts option={this.state.option} />;
    }

    fetchOption(){
        
        // headers.append('Access-Control-Allow-Origin','*')

        fetch(this.props.url + '/result/c414f40fbf9a3fa3d034c86b59c42a1f', {
            method: "GET",
            headers: this.props.header,
            // body: JSON.stringify({
            //     name: "admin",
            //     password: "admin"
            
            // }),
        }).then((response) => response.json())
        .then((data) => {
            this.setState({option: this.initialOption(data.data)})
            console.log(data.data)
            // this.initialOption(data.Evaporation)
        });
    }

    initialOption(data){
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
                data: data
              }
            ]
          };
        return option;
    }
  }
