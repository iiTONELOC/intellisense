import { useState } from 'react';
import { ComputedPageHeight } from '../../hooks';
import { useAuthContext } from '../../providers/withAuth';
import { NotFound, DashboardHome } from '../../components';

const SideBarViews = {
    Home: props => <DashboardHome {...props} />,
    Settings: () => 'settings'
};

const views = {
    home: 'home',
    settings: 'settings'
};

export default function Dashboard() {
    const [view, /*setView*/] = useState(views.home);
    const data = useAuthContext();

    function ViewController(_view) {
        switch (_view) {
            case 'home':
                return <SideBarViews.Home user={data?.isAuthenticated?.user} />;
            case 'dashboard':
                return <SideBarViews.Dashboard />;
            case 'settings':
                return <SideBarViews.Settings />;
            default:
                return <NotFound />;
        }
    }

    return (
        <div
            className="w-full text-gray-300 flex flex-col md:flex-row h-full"
            style={{ height: ComputedPageHeight() }}
        >
            {/* <div
                className="bg-black w-full h-12 md:w-16 md:h-full flex flex-col md:flex-row">
                SideBar
            </div> */}
            {ViewController(view)}
        </div>
    );
}
