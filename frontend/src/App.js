import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import Main_Screen from 'components/Main_Screen';
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
              pxCode Screen List: <br />
              <Link to="/Main_Screen">Main_Screen</Link>
            </div>
          </Route>

          <Route exact path="/Main_Screen" component={Main_Screen} />
        </Switch>
      </Router>
    );
  }
}

export default App;
