import React from "react";
import PropTypes from "prop-types";
import FontAwesome from "react-fontawesome";
import "./Navigation.css";

const Navigation = ( { toggleStats, statsOn } ) => (
  <nav className="navigation">
  </nav>
);

Navigation.propTypes = {
  toggleStats: PropTypes.func.isRequired,
  statsOn: PropTypes.bool.isRequired,
};

Navigation.defaultProps = {
};

export default Navigation;
