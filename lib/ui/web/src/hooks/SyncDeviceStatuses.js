import { useEffect, useState } from 'react';
import { UserAPI } from '../APIs';
const { deviceStatusAll } = UserAPI;
// custom hook to fetch and update device status

export default function SyncDeviceStatuses({ dispatch }) {
    const [isMounted, setMounted] = useState(false);
    const [interval, intervalSet] = useState(null);
    const getAllDeviceStatus = async () => {
        const res = await deviceStatusAll();
        const data = await res.json();
        if (res.status === 200) {
            if (data && data !== undefined) {
                dispatch({ type: 'SET_DEVICES', payload: data });
                return data
            }
        } else {
            return null;
        };
    };

    useEffect(() => {
        setMounted(true);
        return () => setMounted(false)
    }, []);

    useEffect(() => {
        // HANDLES THE FIRST FETCH
        if (isMounted) getAllDeviceStatus();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [isMounted]);

    useEffect(() => {
        // HANDLES THE FIRST FETCH
        if (isMounted && !interval) {
            setInterval(async () => {
                getAllDeviceStatus();
            }, 3500);
            intervalSet(true);
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [isMounted]);

    return true
}