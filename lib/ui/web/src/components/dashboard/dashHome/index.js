import { useEffect, useState } from 'react';
import { roomData } from './rooms';
import DeviceCard from '../../deviceCards';
import SyncDeviceStatuses from '../../../hooks/SyncDeviceStatuses';


function RenderDeviceCards() {
    const _allDevices = [];
    [...Object.values(roomData.Office)].forEach(device => {
        if (Array.isArray(device)) {
            device.map((dev, i) => _allDevices.push(<DeviceCard
                key={i}
                index={i}
                device={dev}
                room='Office'
            />
            ));
        } else {
            _allDevices.push(<DeviceCard device={device} room='Office' />);
        }
    });

    return _allDevices;
}

export default function DashboardHome() {
    const [isMounted, setIsMounted] = useState(false);
    SyncDeviceStatuses();
    useEffect(() => {
        setIsMounted(true);
        return () => setIsMounted(false);
    }, []);

    if (!isMounted) return null;

    return (
        <div className="w-full h-full flex flex-col overflow-hidden bg-zinc-900">
            <div className="flex flex-row flex-wrap justify-center items-center gap-4 w-full h-full my-3 overflow-y-auto mb-5">
                {RenderDeviceCards()}
            </div>
        </div>
    );
}
