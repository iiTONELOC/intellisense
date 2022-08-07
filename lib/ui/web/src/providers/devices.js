import React, { createContext, useContext } from 'react';
import { useDeviceReducer } from '../reducers';
const DeviceContext = createContext();
const { Provider } = DeviceContext;


export const DeviceProvider = ({ value = [], ...props }) => {
    const initialState = {
        'Office': []
    };

    const [state, dispatch] = useDeviceReducer(initialState);
    return <Provider value={[state, dispatch]} {...props} />;
};

export const useDeviceContext = () => useContext(DeviceContext);

