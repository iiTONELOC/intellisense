import { useState } from 'react';
import auth from '../../utils/auth';
import { isFormValidated } from './login';
import { UserAPI } from '../../APIs/user';
import FormContainer from './formContainer';
import { eventDefaults } from '../../utils/utils';
import { getRemembered } from './inputs/checkbox';
import { PasswordInput, UsernameInput } from './inputs';
import { PlusCircleIcon, ExclamationCircleIcon as AlertIcon } from '@heroicons/react/solid';


export default function SignUpForm() {
    const [errorMessage, setErrorMessage] = useState(null);
    const [formState, setFormState] = useState(getRemembered() !== !null ?
        { email: null, username: null, password: null }
        : { email: getRemembered().email, username: null, password: null });

    const handleChange = e => {
        const { name, value } = e.target;
        setFormState({
            ...formState,
            [name]: value
        });
    };
    async function submitFormHandler(e) {
        eventDefaults(e);
        const newUser = {
            username: formState.username,
            password: formState.password
        };
        if (isFormValidated(formState)) {
            const response = await UserAPI.createNewUser(newUser);
            const data = await response.json();
            const { token } = data;
            if (response.status === 200) {
                return auth.login(token);
            } else {
                const { error } = data;
                if (error) {
                    setErrorMessage(error);
                    setTimeout(() => setErrorMessage(null), 3500);
                }
            }
        }
    }

    function clickHandler(e) {
        eventDefaults(e);
        window.location.replace('/login');
    }

    return (
        <>
            <div className='bg-red-500 rounded-lg text-white flex flex-row justify-between drop-shadow-lg'>
                {errorMessage && <><AlertIcon className='ml-1 w-7 h-7 self-center' /><span className='p-2 ml-1 content-center'>{errorMessage.message}</span></>}
            </div>
            <FormContainer>
                <h2 className='text-center text-xl text-gray-300 -mt-8'>Sign Up</h2>
                <div className="rounded-md shadow-sm -space-y-px">
                    <UsernameInput onChange={handleChange} defaultValue={formState.username} />
                    <PasswordInput onChange={handleChange} />
                </div>
                <div className="flex items-center justify-between">
                    <span
                        tabIndex={-1}
                        onClick={clickHandler}
                        className="bg-slate-900 hover:bg-indigo-800 text-white py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                        Login instead
                    </span>
                </div>
                <div>
                    <button
                        onClick={submitFormHandler}
                        className={`group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white
                        bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500`}
                    >
                        <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                            <PlusCircleIcon className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" aria-hidden="true" />
                        </span>
                        Create account
                    </button>
                </div>
            </FormContainer>
        </>
    );
};