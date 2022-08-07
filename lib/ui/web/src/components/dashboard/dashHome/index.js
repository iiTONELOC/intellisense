import { useDeviceContext } from '../../../providers/devices';
import SyncDeviceStatuses from '../../../hooks/SyncDeviceStatuses';
import { RoomNavBar } from './roomNavigationBar';
import DeviceCard from '../../deviceCards';
import { roomData } from './rooms';



function RenderDeviceCards(data) {
    let devices = null;
    const room = roomData[data];
    if (room) devices = [...Object.values(room)];


    return (
        devices?.map(device => {
            if (device?.name?.includes('Vizio TV')) {
                return <DeviceCard device={device} />;
            } else if (Array.isArray(device)) {
                device.map((dev, i) =>
                    <DeviceCard
                        key={i}
                        index={i}
                        device={dev}
                        room={data}
                    />
                )
            } else {
                return null;
            }
        })
    );
}

export default function DashboardHome({ setRoom, room, user }) {
    const [, dispatch] = useDeviceContext();
    SyncDeviceStatuses({ dispatch });

    return (
        <div className="w-full h-full flex flex-col overflow-hidden bg-zinc-900">
            <RoomNavBar room={room} setRoom={setRoom} user={user} />
            <div className="flex flex-row flex-wrap justify-center items-center gap-4 w-full h-full my-3 overflow-y-auto mb-5">
                {RenderDeviceCards(room)}
            </div>
        </div>
    );
};