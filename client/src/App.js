import React, {Component} from 'react';
import { Bar } from './components/Bar'
import { Layout } from './components/Layout';
import { Articles } from './components/Articles';
import './App.css';

class App extends Component {
  render() {
    return (

      <div>
        <Bar />
        <Layout><Articles /></Layout>
      </div>

    );
  }
}

export default App;
