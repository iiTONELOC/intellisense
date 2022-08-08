import { useEffect } from 'react';
import { useDeviceContext } from '../providers/devices';
import { UserAPI } from '../APIs';
// custom hook to fetch and update device status

export default function SyncDeviceStatuses() {
    const [, dispatch] = useDeviceContext();
    // Needs to be around 50ms to enable real-time updates
    // This only matters if the state is updated outside of our server
    // this could be from a phone or Alfred running in another instance
    // times greater than 1000ms can be used to reduce the frequency of server calls
    // and we can manage the state with the dispatch event in our toggleWemoDevice function
    // if we are certain that the UI is the only method being used or if we don't care about a
    // few second lag in the UI visual updates
    const fetchIntervalInMs = 1500;
    const getAllDeviceStatus = async () => {
        const res = await UserAPI.deviceStatusAll();
        const data = await res.json();

        if (res.status === 200) {
            if (data && data !== undefined) {
                dispatch({ type: 'SET_DEVICES', payload: data });
                return data;
            } else {
                return null;
            }
        } else {
            return null;
        }
    };

    useEffect(() => {
        // HANDLES THE FIRST FETCH
        (async () => getAllDeviceStatus())();
        setInterval(async () => {
            await getAllDeviceStatus();
        }, fetchIntervalInMs);
        // eslint-disable-next-line
    }, []);

    return true;
}
