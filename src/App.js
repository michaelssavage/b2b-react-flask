import React from 'react';
import Home from './pages/Home.js'
import Signin from './pages/Signin.js'
import Signup from './pages/Signup.js'
import Products from './pages/Products.js'
import Orders from './pages/Orders.js'
import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={Signin} />
          <Route path="/signin" component={Signin} />
          <Route path="/signup" component={Signup} />
          <Route path="/home" component={Home} />
          <Route path="/products" component={Products} />
          <Route path="/orders" component={Orders} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;