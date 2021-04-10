import React from 'react';
import Home from './Home.js'
import Signin from './Signin.js'
import Signup from './Signup.js'
import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/signin" component={Signin} />
          <Route path="/signup" component={Signup} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;

// import React, {useState, useEffect} from 'react';

//   const [currentTime, setCurrentTime] = useState(1);
//   useEffect(() =>{
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//     })
//   }, []);
//   <p>The current time is {currentTime}.</p>