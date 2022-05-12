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

      componentDidMount(){}

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

