import React from 'react';
import { Media } from 'reactstrap';
import './Articles.css';

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
          <Media className='Articles'>
            <Media body>
              <Media heading>{article.title}</Media>
              <td dangerouslySetInnerHTML={{__html: article.body}} />
            </Media>
          </Media>
        )
      })
    }
  }
}
