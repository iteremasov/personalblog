import React from 'react';
import PropTypes from 'prop-types';
import { Container } from 'semantic-ui-react';

export const Layout = ({children}) => {
  return (
    <Container>
        {children}
    </Container>
  )
};

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};
