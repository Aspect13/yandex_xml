import {connect} from "react-redux";
import React from "react";
import {BACKEND, STATIC_PATH} from "../Api";

class MainOne extends React.Component {

    getXML = xmlName => {
        const conf = {
            method: 'GET',
            mode: 'no-cors',
        };
        fetch(BACKEND + STATIC_PATH + xmlName, conf).then(
            response =>
                response.text()
        ).then(
            str => console.log(str)
        ).then(
            data => console.log('data', data)
        )
    };

// (new window.DOMParser()).parseFromString(str, "text/xml")

    render () {
        this.getXML('xml1.xml');

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