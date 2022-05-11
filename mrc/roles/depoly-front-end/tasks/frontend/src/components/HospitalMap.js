import * as React from 'react';
import Map, {Popup} from 'react-map-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import ReactDOM from "react-dom"

export default class HospotalMap extends React.Component {

    constructor(props) {
        super(props);
        
        this.state = {showPopup: false,
        features: {},
        longitude: 144.9631,
        latitude: -37.814107
        };
      }

      componentDidMount(){}

    render(){
        return <div className="hospital-map">
  <Map
    initialViewState={{
      longitude: 144.9631,
      latitude: -37.814107,
      zoom: 15
    }}
    style={{width: 800, height: 500}}
    mapStyle="mapbox://styles/zhiqingw/ckur17j9i1zir17k9t1q5ascb"
    
    mapboxAccessToken="pk.eyJ1IjoiemhpcWluZ3ciLCJhIjoiY2t0anJ1Y2xoMWV6NTJ3bm1xNnBoNWt0eiJ9.oBR-Za509LFKgj2khrxf2g"
    interactiveLayerIds={['accident', 'on_street_parking', 'commercial']} 
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
    >
    {this.state.showPopup && (
      <Popup longitude={this.state.longitude} latitude={this.state.latitude}
        anchor="bottom"
        onClose={() =>this.setState({showPopup:false}) }
        >
        <h1>{this.state.features.rd_seg_dsc}</h1>
      </Popup>)
      
      }
    </Map>
  
  </div>;
    }
  
}

