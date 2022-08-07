import { useEffect, useState } from "react";
import { CloseButton } from "../../buttons/closeButton";

const navData = [
    { room: 'Living Room', icon: '', },
    { room: 'Kitchen', icon: '', },
    { room: 'Master Bedroom', icon: '', },
];

function RoomIcon({ className }) {
    if (!className) className = "h-8 w-8 text-gray-400 hover:text-gray-500";
    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className={className}
            viewBox="0 0 20 20"
            fill="currentColor"
        >
            <path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z" />
        </svg>
    );
};

export function RoomNavBar({ room, setRoom, user }) {
    const [isMounted, setIsMounted] = useState(false);
    const [time, setTime] = useState(Date.now());
    const [open, setOpen] = useState(false);
    const timerUpdater = () => {
        setTime(Date.now());
    };
    useEffect(() => { setIsMounted(true) }, []);
    useEffect(() => {
        if (isMounted) {
            setTime(Date.now())
            setInterval(timerUpdater, 10000);
        };
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [isMounted]);
    return (
        <nav navdata='room-navbar' className="w-full flex flex-col justify-end items-center text-gray-200 min-h-16 static mt:1 md:mt-2">
            <header className='w-full flex-col justify-between items-center'>
                {/* INFO HEADER */}
                <div className="w-full flex flex-col md:flex-row justify-between mb-2">
                    <h1 className="ml-3 text-shadow">
                        Welcome, {user?.username || ''}!
                    </h1>
                    <span className="w-full md:w-1/2 flex flex-col md:flex-row justify-between">
                        <p className="ml-3 md:m-0 text-shadow">Today is  {`${new Intl.DateTimeFormat('en-US', { dateStyle: 'full' })
                            .format(Date.now())}`}
                        </p>
                        <p className="ml-3 md:mr-3 text-shadow">
                            {`${new Intl.DateTimeFormat('en-US',
                                { timeStyle: 'short' })
                                .format(time)}`}
                        </p>
                    </span>
                </div>
                {/* POP-UP MENU BUTTON */}
                <h1
                    onClick={() => setOpen(!open)}
                    className="mr-3 text-myLightBlue font-medium text-xl sm:text-2xl lg:text-3xl text-right underline underline-offset-8"
                >
                    <span className="flex flex-wrap gap-5 items-center justify-end">
                        <RoomIcon />
                        {room}
                    </span>

                </h1>
            </header>
            {/* POP UP MENU */}
            {open && <ul className="top-60 md:top-40 right-3 flex flex-col gap-4 p-2 mx-3 absolute bg-zinc-800 rounded-lg drop-shadow-md">
                <CloseButton onClick={() => setOpen(false)} />
                {navData.map((navItem, index) => {
                    return (
                        <li
                            className={`rounded-lg align-middle text-start ${room === navItem.room ? 'border-b-2 border-b-myLightBlue' : ''}`}
                            key={'Nav: ' + navItem?.room || `${index}`}>
                            <p
                                onClick={setRoom}
                                className="ml-1 lg:text-xl hover:text-myLightBlue"
                            >
                                {navItem.room}
                            </p>
                        </li>
                    )
                })}
            </ul>
            }
        </nav>
    );
};