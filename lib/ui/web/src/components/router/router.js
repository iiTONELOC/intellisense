import { Home, Login, SignUp, Dashboard } from '../../pages';
import { DeviceProvider } from '../../providers/devices';
import WithAuthorization from '../../providers/withAuth';
import { NotFound } from '../notfound';

export default function Router({ path }) {
    const pathTokens = path.split('/');
    if (pathTokens[3] === 'dashboard') {
        return (
            <WithAuthorization>
                <DeviceProvider>
                    <Dashboard />
                </DeviceProvider>
            </WithAuthorization>
        );
    } else {
        switch (path) {
            case '/':
                return <Home />;
            case '/login':
                return <Login />;
            case '/sign-up':
                return <SignUp />;
            default:
                return <NotFound />;
        };
    };
};