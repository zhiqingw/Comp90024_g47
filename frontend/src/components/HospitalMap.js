import * as React from 'react';
import Map, {Popup} from 'react-map-gl';
import ReactDOM from "react-dom"
export default function HospotalMap() {
    const [showPopup, setShowPopup] = React.useState(true);
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
        
        
        
    
    }
    
    
        
    }  
    

    />
  
  </div>;
}

