import React, {Component} from 'react';
import {Switch,Route} from 'react-router-dom'
import { Layout } from './components/Layout';
import { Articles } from './components/Articles';
import './App.css';


class App extends Component {
  render() {
    return (

      <div>
        <Layout>
          <Switch>
            <Route exact path="/" component={Articles} />
          </Switch>
        </Layout>
      </div>

    );
  }
}

export default App;
