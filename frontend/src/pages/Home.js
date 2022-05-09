import React from "react";
import axios from 'axios';
import fetchToCurl from 'fetch-to-curl';
export default function Home(){
    // const nano = require('nano')('http://admin:admin@172.26.130.233:5984');
    // nano.db.use('twitter').get()
	// .then((body) => {
	// 	console.log(body);
	// });
//     axios.get('http://admin:admin@172.26.134.66:5984/twitter')
//   .then(json => console.log(json))



// axios({
//     method: 'get',
//     url: `http://admin:admin@172.26.130.233:5984`,
//     withCredentials: false,
//     // params: {
//     //   access_token: SECRET_TOKEN,
//     // },
//   }) .then(json => console.log(json));
//   axios(`http://admin:admin@172.26.130.233:5984`, {
//     method: 'get',
//     mode: 'no-cors',
//     headers: {
//       'Access-Control-Allow-Origin': '*',
//       'Content-Type': 'application/json',
//       'Access-Control-Allow-Credentials':true,
//       'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
//     },
//     credentials: 'same-origin',
//     crossorigin:true
//   }).then(response => {
//       console.log(response)
//   })
    return(
        <div>
            <header>
                <div class="navbar-nav">
                    <li class="active"><a href="/">Home</a></li>
                    <li><a href="/f1">Overview</a></li>
                    <li><a href="/health">Health</a></li>
                </div>
            </header>
        <h1>
            home
        </h1>
        </div>

    )
}