import { useState, useEffect } from 'react';
import { UserAPI } from '../../APIs';
import { useDeviceContext } from '../../providers/devices';
import { CgScreenWide } from 'react-icons/cg';
import { GiLightBulb } from 'react-icons/gi';

async function toggleLight(e, room, index, setSwitchState, switchState) {
    e.preventDefault();
    e.stopPropagation();
    const light_num = index + 1;
    let command = 'none';
    if (room === 'Living Room' || room === 'Master Bedroom') {
        command = 'jarvis ' + room + ' toggle light ' + light_num;
    };
    if (room === 'Kitchen') command = 'jarvis toggle ' + room + ' light';
    command = command.toLowerCase();
    await UserAPI.remoteAccess({ command: command });
    if (switchState === 1) setSwitchState(0);
    if (switchState === 0) setSwitchState(1);
    return true;
}

function deviceState(state, device, room) {

    const currentRoom = state[room];
    let status = null;

    if (room !== undefined && currentRoom.length > 0) {
        const devices = currentRoom?.map(_dev => _dev.name === device.name ? _dev : null);
        const dev = devices?.filter(_dev => _dev !== null)?.[0];
        status = dev.status;
    }
    return status;
}

export default function DeviceCard({ device, room, index }) {
    const [switchState, setSwitchState] = useState(0);
    const [isMounted, setIsMounted] = useState(false);
    const [state] = useDeviceContext();


    useEffect(() => {
        setIsMounted(true);
        return () => setIsMounted(false);
    }, []);

    useEffect(() => {
        if (state && state[room] && state[room].length > 0) {
            setSwitchState(deviceState(state, device, room));
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [room]);

    useEffect(() => {
        if (isMounted && state) {
            // console.log("State Object Changed", state)
            setSwitchState(deviceState(state, device, room));
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [state]);

    return isMounted && (
        <div
            onClick={(e) => toggleLight(e, room, index, setSwitchState, switchState)}
            className="flex flex-col gap-3 w-96 h-[200px] bg-gray-600 rounded-lg">
            <div
                className="p-1 flex flex-col justify-start items-center rounded-t-lg h-full rounded-lg bg-black/40 w-full">
                <h1 className="text-white items-center text-shadow text-center text-2xl font-bold p-1 text-shadow ">
                    <p className="block">
                        {device.name || 'Unknown Device'}
                    </p>
                </h1>
                {device.name.includes('TV') ?
                    <CgScreenWide className="mt-8 h-12 w-12" /> :
                    <GiLightBulb className={`mt-8 h-12 w-12 ${switchState === 1 ? "text-yellow-200" : ""}`} />}
                <div className='w-full flex flex-row justify-around mt-5'>
                    {device.name.includes('TV') ?
                        null :
                        <span className='gap-3 flex flex-row justify-center items-center'>
                            <span className={`rounded-full ${switchState === 1 ?
                                "bg-emerald-400" :
                                'bg-red-600'} p-2`}>
                            </span>
                            <p className='text-shadow'>
                                Turn
                                {switchState === 1 ?
                                    ` OFF` :
                                    ' ON'}
                            </p>
                        </span>
                    }
                </div>
            </div>
        </div>
    );
}