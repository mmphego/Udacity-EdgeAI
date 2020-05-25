import React from "react";
import PropTypes from "prop-types";
import moment from "moment";
import DataBox from "components/data-box/DataBox";
import FontAwesome from "react-fontawesome";
import mq from "../../MqttClient";
import { MQTT, SETTINGS } from "../../constants/constants";
import "./Stats.css";

class Stats extends React.Component {
  constructor( props ) {
    super( props );

    this.handleMqtt = this.handleMqtt.bind( this );
    this.calculateClasses = this.calculateClasses.bind( this );
    this.calculateSpeed = this.calculateSpeed.bind( this );
    this.state = {
      currentClassCount: 0,
      currentFrameData: [],
      currentFrameLabels: [],
      currentSpeed: 0,
      currentSpeedData: [],
      currentSpeedLabels: [],
    };
  }

  componentDidMount() {
    // register handler with mqtt client
    mq.addHandler( "class", this.handleMqtt );
  }

  componentWillUnmount() {
    mq.removeHandler( "class" );
  }

  handleMqtt( topic, payload ) {
    switch ( topic ) {
      case MQTT.TOPICS.CLASS:
        this.calculateClasses( payload );
        break;
      case MQTT.TOPICS.SPEEDOMETER:
        this.calculateSpeed( payload );
        break;
      default:
        break;
    }
  }

  calculateClasses( input ) {
    let newLabel = this.state.currentFrameLabels;
    let newFrameData = this.state.currentFrameData;
    newLabel.push( input.class_names );
    if ( input.class_names.length != undefined ) {
      newFrameData.push( input.class_names.length );
    }
    if ( newFrameData.length > SETTINGS.MAX_POINTS ) {
      const sliceFrameData = newFrameData.slice( SETTINGS.SLICE_LENGTH );
      const sliceFrameLabels = newLabel.slice( SETTINGS.SLICE_LENGTH );
      newFrameData = sliceFrameData;
      newLabel = sliceFrameLabels;
    }
    this.setState( { currentClassCount: input.class_names.length,
      currentFrameLabels: newLabel,
      currentFrameData: newFrameData } );
  }

  calculateSpeed( input ) {
    let newLabel = this.state.currentSpeedLabels;
    let newFrameData = this.state.currentSpeedData;
    newLabel.push( input.speed );
    if ( input.speed != undefined ) {
      newFrameData.push( input.speed );
    }
    if ( newFrameData.length > SETTINGS.MAX_POINTS ) {
      const sliceFrameData = newFrameData.slice( SETTINGS.SLICE_LENGTH );
      const sliceFrameLabels = newLabel.slice( SETTINGS.SLICE_LENGTH );
      newFrameData = sliceFrameData;
      newLabel = sliceFrameLabels;
    }
    this.setState( { currentSpeed: input.speed,
      currentSpeedLabels: newLabel,
      currentSpeedData: newFrameData } );
  }

  render() {
    return (
      <div className={ `stats ${ this.props.statsOn ? "active" : "" }` }>
        { /* Current class count */ }
        <DataBox title="Classes Counted" data={ this.state.currentClassCount } />
        { /* Current speed */ }
        <DataBox title="Speed" data={ this.state.currentSpeed } color="blue" />
      </div>
    );
  }
}

Stats.propTypes = {
  statsOn: PropTypes.bool.isRequired,
};

Stats.defaultProps = {
};

export default Stats;
