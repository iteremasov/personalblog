import React from 'react';
import {Container, Row} from 'reactstrap'
import PropTypes from 'prop-types';

export const Layout = ({children}) => {
  return (
    <Container>
      <Row>
        {children}
      </Row>
    </Container>
  )
};

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};
