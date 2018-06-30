import {applyMiddleware, combineReducers, createStore} from 'redux';

import {createLogger} from 'redux-logger';
import thunk from 'redux-thunk';
import {composeWithDevTools} from 'redux-devtools-extension';

import {routerMiddleware, routerReducer,} from 'react-router-redux';
import createHistory from 'history/createBrowserHistory';
import SomeReducer from "./SomeReducer";
import SnackbarReducer from "./SnackbarReducer";

export const appHistory = createHistory();
const historyMiddleware = routerMiddleware(appHistory);
const loggerMiddleware = createLogger();


let middlewares = (localTest) => {
    const middlewareDebug = [thunk, loggerMiddleware, historyMiddleware];
    const middlewareLive = [thunk, historyMiddleware];

    if (localTest) {
        return composeWithDevTools(applyMiddleware(...middlewareDebug))
    } else {
        return applyMiddleware(...middlewareLive);
    }
};


const Store = createStore(
    combineReducers({
        SomeReducer,
        SnackbarReducer,
        router: routerReducer
    }),
    middlewares(module.hot)
);

export default Store;