import * as React from 'react';
import Map, {Popup} from 'react-map-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import ReactDOM from "react-dom"

export default class EntertainmentMap extends React.Component {

    constructor(props) {
        super(props);
        
        this.state = {showPopup: false,
        features: {},
        longitude: 144.9631,
        latitude: -37.814107
        };
      }

      componentDidMount(){

        let types = [
          {label: "<10",
            colors: "#f09d9d"
          },
          {label: "10-50",
            colors: "#f3f09b"
          },
          {label: "50-100",
            colors: "#5ee865"
          },
          {label: "100-200",
            colors: "#09bec8"
          },
          {label: ">200",
            colors: "#09bec8"
          }
      
        ]
        let legend = document.querySelector('#map-legend');
        // let i = 0;
        // myNode = document.getElementById("foo");
        while (legend.firstChild) {
          legend.removeChild(legend.lastChild);
        }
        for (let type of types) {
        
          let item = document.createElement('div');
      
          let key = document.createElement('span');
          
          key.classList.add('legend-key-dot');
          
          
          key.style.backgroundColor = type.colors;
      
          let value = document.createElement('span');
          value.innerHTML = type.label;
          item.appendChild(key);
          item.appendChild(value);
          legend.appendChild(item);
          
          
        }
      }

    render(){
      

      
        return <div className="hospital-map">
  <Map
    initialViewState={{
      longitude: 144.9631,
      latitude: -37.814107,
      zoom: 12
    }}
    style={{width: 800, height: 500}}
    mapStyle={this.props.mapStyle}
    
    mapboxAccessToken={this.props.mapboxAccessToken}
    interactiveLayerIds={this.props.interactiveLayerIds} 
    onClick={(e)=>{
        console.log(e.features[0].properties)
        setTimeout(
            this.setState({
                showPopup: true,
                longitude: e.lngLat.lng,
                latitude: e.lngLat.lat,
                features: e.features[0].properties
            })
        , 500);
    }} 
    // >
    // {this.state.showPopup && (
    //   <Popup longitude={this.state.longitude} latitude={this.state.latitude}
    //     anchor="bottom"
    //     onClose={() =>this.setState({showPopup:false}) }
    //     >
    //     <h1>hello</h1>
    //   </Popup>)
      
    //   }
   ></Map>
  
  </div>;
    }
  
}

