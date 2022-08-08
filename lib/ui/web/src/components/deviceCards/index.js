import { useState, useEffect } from 'react';
import { UserAPI } from '../../APIs';
import { useDeviceContext } from '../../providers/devices';
import { CgScreenWide } from 'react-icons/cg';
import { GiLightBulb } from 'react-icons/gi';
import { eventDefaults } from '../../utils/utils';

async function toggleWemoDevice(deviceName, currentState, dispatch) {
    let command = `alfred toggle ${deviceName}`;
    command = command.toLowerCase();
    await UserAPI.remoteAccess({ command });
    // NOSONAR
    // If the timing of the SyncDeviceStatuses is increased (lowered below 1000ms)
    //
    // Comment out the dispatch call below, as it will interfere with the real-time updates
    // for best results and instant updates set the fetchIntervalInMs in the SyncDeviceStatuses
    // to 50ms. We are currently polling every 1.5 seconds.
    dispatch({
        type: 'UPDATE_DEVICE',
        payload: {
            device: deviceName,
            status: currentState === 1 ? 0 : 1
        }
    });
    return true;
}

function deviceState(state, device, room) {

    const currentRoom = state[room];
    let status = null;

    if (room !== undefined && currentRoom.length > 0 && device.name !== 'Vizio TV') {
        const devices = currentRoom?.filter(_dev => _dev.name === device.name);
        const dev = devices[0];
        status = dev.status;
    }

    return status;
}

export default function DeviceCard({ device, room, index }) {
    const [isMounted, setIsMounted] = useState(false);
    const [state, dispatch] = useDeviceContext();
    const currentState = deviceState(state, device, room);
    const deviceName = device.name;

    const lightBulbClasses = `mt-8 h-12 w-12 ${currentState === 1 ? 'text-yellow-200' : ''}`;
    const statusIndicatorClasses = `rounded-full ${currentState === 1 ? 'bg-emerald-400' : 'bg-red-600'} p-2`;
    const onOrOff = currentState === 1 ? 'ON' : 'OFF';
    function handleAction(e) {
        eventDefaults(e);
        if (deviceName === 'Vizio TV') {
            return;
        }

        if (deviceName.includes('switch')) {
            toggleWemoDevice(deviceName, currentState, dispatch);
        }
    }

    useEffect(() => {
        setIsMounted(true);
        return () => setIsMounted(false);
    }, []);
    // eslint-disable-next-line

    return isMounted && (
        <div
            onDoubleClick={handleAction}
            className="flex flex-col gap-3 w-96 h-[200px] bg-gray-600 rounded-lg">
            <div
                className="p-1 flex flex-col justify-start items-center rounded-t-lg h-full rounded-lg bg-black/40 w-full">
                <h1 className="text-white items-center text-shadow text-center text-2xl font-bold p-1 text-shadow ">
                    <p className="block">
                        {deviceName || 'Unknown Device'}
                    </p>
                </h1>
                {deviceName.includes('TV') ?
                    <CgScreenWide className="mt-8 h-12 w-12" /> :
                    <GiLightBulb className={lightBulbClasses} />}
                <div className='w-full flex flex-row justify-around mt-5'>
                    {deviceName.includes('TV') ?
                        null :
                        <span className='gap-3 flex flex-row justify-center items-center'>
                            <span className={statusIndicatorClasses}>
                            </span>
                            <p className='text-shadow'>
                                Turn{' '}{onOrOff}
                            </p>
                        </span>
                    }
                </div>
            </div>
        </div>
    );
}
