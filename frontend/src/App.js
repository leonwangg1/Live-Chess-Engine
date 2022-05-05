import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import Main_Screen from 'components/Main_Screen';
import About from 'components/About'
import Contact from 'components/Contact'
import AOS from 'aos';
import { isMobile } from 'react-device-detect';

import 'aos/dist/aos.css';
import './App.css';
import './fonts.css';

class App extends Component {
  componentDidMount() {
    setTimeout(() => {
      AOS.init({
        offset: isMobile ? 10 : 100,
      });
      AOS.refresh();
    }, 1500);
  }

  render() {
    return (
      <Router hashType="noslash" basename={process.env.BASE_PATH}>
        <Switch>
          <Route exact path="/">
            <div>
              <Link to="/Main_Screen">Home</Link>
            </div>
          </Route>

          {/* Routers  for pages */}
          <Route exact path="/Main_Screen" component={Main_Screen} />
          <Route exact path="/About" component={About} />
          <Route exact path="/Contact" component={Contact} />
        </Switch>
      </Router>
    );
  }
}

export default App;
