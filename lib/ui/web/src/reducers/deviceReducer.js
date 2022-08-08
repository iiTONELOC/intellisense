import { useReducer } from 'react';

const reducer = (state, action) => {
    switch (action.type) {
        case 'SET_DEVICES':
            return {
                ...state,
                ...action.payload
            };
        case 'UPDATE_DEVICE':
            const _state = { ...state };
            const _office = [..._state.Office].map(_dev => {
                if (_dev.name === action.payload.device) {
                    _dev.status = action.payload.status;
                }
                return _dev;
            });

            _state.Office = _office;
            return {
                ..._state
            };

        default:
            return state;
    }
};

const useDeviceReducer = initialState => useReducer(reducer, initialState);

export default useDeviceReducer;

