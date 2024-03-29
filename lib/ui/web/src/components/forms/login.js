import auth from '../../utils/auth';
import { UserAPI } from '../../APIs';
import { useState, useEffect } from 'react';
import FormContainer from './formContainer';
import { getRemembered } from './inputs/checkbox';
import { eventDefaults } from '../../utils/utils';
import { UsernameInput, PasswordInput, Checkbox } from './inputs';
import { LockClosedIcon, ExclamationCircleIcon as AlertIcon } from '@heroicons/react/solid';

const REMEMBER_TOKEN = 'alfred_remember_token';

export function isFormValidated(formState) {
    if (formState) {
        if (formState.password) {
            return formState.password.length >= 8;
        } else return false;
    } else return false;
}


export default function LoginForm() {
    const [checked, setChecked] = useState(localStorage.getItem(REMEMBER_TOKEN) ? true : false);
    const [errorMessage, setErrorMessage] = useState(null);
    const [formState, setFormState] = useState(getRemembered() === null ?
        { username: null, password: null }
        : getRemembered());

    const handleChange = e => {
        const { name, value } = e.target;
        setFormState({
            ...formState,
            [name]: value
        });
    };

    async function submitFormHandler(e) {
        eventDefaults(e);
        const user = {
            username: formState.username,
            password: formState.password
        };

        if (isFormValidated(formState)) {
            const response = await UserAPI.loginUser(user);
            const data = await response.json();
            if (response.status === 200) {
                const { token, ...rest } = data;

                // set the token in local storage
                if (checked) localStorage.setItem(REMEMBER_TOKEN, JSON.stringify(rest));
                auth.login(token);
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
        window.location.replace('/sign-up');
    }

    useEffect(() => {
        if (checked === false) localStorage.removeItem(REMEMBER_TOKEN);
    }, [checked]);
    return (
        <>
            <div className='bg-red-500 rounded-lg text-white flex flex-row justify-between drop-shadow-lg'>
                {errorMessage && <><AlertIcon className='ml-1 w-7 h-7 self-center' /><span className='p-2 ml-1 content-center'>{errorMessage.message}</span></>}
            </div>
            <FormContainer>
                <h2 className='text-center text-xl text-gray-300 -mt-8'>Login</h2>
                <div className="rounded-md shadow-sm -space-y-px">
                    <UsernameInput onChange={handleChange} defaultValue={formState.email} />
                    <PasswordInput onChange={handleChange} />
                </div>
                <div className="flex items-center justify-between">
                    <Checkbox checked={checked} setChecked={setChecked} />
                    <span
                        tabIndex={-1}
                        onClick={clickHandler}
                        className="bg-slate-900 hover:bg-indigo-800 text-white py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                        Create account instead
                    </span>
                </div>
                <div>
                    <button
                        onClick={submitFormHandler}
                        className={`group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm 
                        font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500`}
                    >
                        <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                            <LockClosedIcon className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" aria-hidden="true" />
                        </span>
                        Sign in
                    </button>
                </div>
            </FormContainer>
        </>
    );
}