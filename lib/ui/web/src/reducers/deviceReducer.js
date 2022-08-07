import { useReducer } from 'react';

const reducer = (state, action) => {
    switch (action.type) {
        case 'SET_DEVICES':
            return {
                ...action.payload
            };
        case 'UPDATE_DEVICE':
            return;
        default:
            return state;
    }
}

const useDeviceReducer = initialState => useReducer(reducer, initialState);

export default useDeviceReducer;

