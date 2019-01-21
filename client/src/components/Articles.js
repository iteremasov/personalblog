import React from 'react';
import './Articles.css';

const ReactMarkdown = require('react-markdown')

export class Articles extends React.Component {
  state = {
    loading: false,
    articles: [],
  };

  componentDidMount() {
    this.setState({ loading: true });

    fetch('/api/articles?page=1&pagesize=10').then((response) => {
      response.json().then((articles) => this.setState({ articles, loading: false }))
    })
  }

  render() {
    if (this.state.loading) {
      return <div>Loading....</div>
    } else {
      return this.state.articles.map((article) => {
        return (
          <div className='Articles'>
            <div body>
              < ReactMarkdown source={ article.title } />
              < ReactMarkdown source={ article.body  } />
            </div>
          </div>
        )
      })
    }
  }
}
