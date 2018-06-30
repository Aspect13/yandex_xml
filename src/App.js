import React, { Component } from 'react';

import { connect } from 'react-redux';

import {Redirect, Route, Switch} from "react-router-dom";

import {push} from "react-router-redux";
import MainOne from "./Components/MainOne";
import Navbar from "./Navbar/Navbar";
import SnackbarCustom from "./SnackbarCustom";

class App extends Component {
    render() {
        return (
            <div>
                <Navbar/>
                <Switch>
                    <Route exact path='/' component={MainOne}/>
                </Switch>
                <SnackbarCustom/>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
    };
};

const mapDispatchToProps = dispatch => {
    return {
        move: newLocation => dispatch(push(newLocation))
    }
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(App);