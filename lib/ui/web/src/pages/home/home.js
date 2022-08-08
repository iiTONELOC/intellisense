import { ComputedPageHeight } from '../../hooks';
import auth from '../../utils/auth';


const buttonData = [
    {
        text: 'Login',
        link: '/login'
    }
];

const handleButtonClick = (e, link) => {
    e.preventDefault();
    e.stopPropagation();
    window.location.replace(link);
};

const btnClasses = `flex justify-center py-2 px-4 border border-transparent text-md font-large rounded-md text-white
bg-indigo-700 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 text-shadow`;

export default function Home() {
    const isLoggedIn = auth.loggedIn();
    if (isLoggedIn) {
        const uData = auth.getProfile();
        window.location.replace(`/users/${uData.id}/dashboard`);
    }
    // get the height of the nav and subtract it from the height of the window
    if (!isLoggedIn) {
        return (
            <div
                className={`w-full flex flex-col justify-center items-center bg-[url('./assets/images/landing.jpg')] bg-cover p-1 overflow-hidden relative text-gray-300`}
                style={{
                    height: ComputedPageHeight()
                }}>

                <div className={`text-gray-100 w-full md:w-6/12 z-40 flex flex-col justify-center items-center text-center gap-5 overflow-hidden bg-black/40 rounded-lg `}>
                    <h1 className="mt-36 md:mt-0 font-medium text-2xl text-shadow">
                        <span className="font-medium text-4xl text-myPink">L</span>ogin to access your dashboard
                    </h1>
                    <p className="p-1 text-shadow">
                        Home Automation is a click away.
                    </p>
                    <div className="w-max p-4 gap-10 flex justify-center">
                        {buttonData.map(({ text, link }, index) => (
                            <button
                                index={index}
                                className={`${btnClasses}`}
                                onClick={e => { handleButtonClick(e, link); }}
                            >
                                {text}
                            </button>
                        ))}
                    </div>
                </div>
            </div>
        );
    } else {
        return null;
    }
}
