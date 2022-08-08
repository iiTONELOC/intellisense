import React, { createContext, useContext } from 'react';
import { useDeviceReducer } from '../reducers';
const DeviceContext = createContext();
const { Provider } = DeviceContext;


export const DeviceProvider = ({ _value = [], ...props }) => {
    const [state, dispatch] = useDeviceReducer({
        'Office': []
    });

    return <Provider value={[state, dispatch]} {...props} />;
};

export const useDeviceContext = () => useContext(DeviceContext);

