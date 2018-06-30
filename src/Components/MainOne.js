import {connect} from "react-redux";
import React from "react";

class MainOne extends React.Component {


    render () {
        return (
            <div>TEST</div>
        )
    }


}



const mapStateToProps = state => {
    return {
    };
};

const mapDispatchToProps = dispatch => {
    return {
    }
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(MainOne);