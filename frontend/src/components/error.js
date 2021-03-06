import React from 'react';
import PropTypes from 'prop-types';
import { Row, Col } from 'reactstrap';
import RaisedButton from 'material-ui/RaisedButton';
import { Link } from 'react-router-dom';
import './error.css'

const Error = ({ title, content }) => (
  <div className="error_container">
    <Row>
      <Col lg="4">
        <h2>{title}</h2>
        <p>{content}</p>
        <Link to="/">
          <RaisedButton
            label="Go Home"
            primary={true}
          />
        </Link>
      </Col>
    </Row>
  </div>
);

Error.propTypes = {
  title: PropTypes.string,
  content: PropTypes.string,
};

Error.defaultProps = {
  title: 'Uh oh',
  content: 'An unexpected error came up',
};

export default Error;
