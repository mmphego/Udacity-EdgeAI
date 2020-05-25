import { connect } from "react-redux";
import Stats from "./Stats";

// maps the redux state to this components props
const mapStateToProps = state => ( {
  statsOn: state.stats.statsOn,
} );

export default connect( mapStateToProps )( Stats );
