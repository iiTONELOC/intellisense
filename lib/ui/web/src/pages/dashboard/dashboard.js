import { useState, useEffect } from 'react';
import { ComputedPageHeight } from "../../hooks";
import { useAuthContext } from "../../providers/withAuth";
import { NotFound, DashboardHome } from '../../components';
const SideBarViews = {
    Home: (props) => <DashboardHome {...props} />,
    Dashboard: () => 'dashboard',
    Settings: () => 'settings',
};
const views = {
    home: 'home',
    dashboard: 'dashboard',
    settings: 'settings',
};
const rooms = {
    'Living Room': 'Living Room',
    'Kitchen': 'Kitchen',
    'Master Bedroom': 'Master Bedroom',
};
export default function Dashboard() {
    const [isMounted, setIsMounted] = useState(false);
    const [view, setView] = useState(views.home);
    const [currentRoom, setCurrentRoom] = useState(rooms['Living Room']);
    const data = useAuthContext();


    useEffect(() => {
        setIsMounted(true);
        return () => setIsMounted(false);
    }, []);

    function setRoom(e) {
        e.preventDefault();
        e.stopPropagation();
        const room = e.target.innerText;
        setCurrentRoom(rooms[room]);
    };


    function ViewController(view) {
        switch (view) {
            case 'home':
                return <SideBarViews.Home
                    setRoom={setRoom}
                    room={currentRoom}
                    user={data?.isAuthenticated?.user}
                />;
            case 'dashboard':
                return <SideBarViews.Dashboard />;
            case 'settings':
                return <SideBarViews.Settings />;
            default:
                return <NotFound />;
        };
    };

    return (
        <div
            className="w-full text-gray-300 flex flex-col md:flex-row h-full"
            style={{ height: ComputedPageHeight() }}
        >
            <div
                className="bg-black w-full h-12 md:w-16 md:h-full flex flex-col md:flex-row">
                SideBar
            </div>
            {ViewController(view)}
        </div>
    );
};
