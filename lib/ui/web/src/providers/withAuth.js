import auth from '../utils/auth';
import { useState, useEffect, createContext, useContext } from 'react';

export const AuthContext = createContext({});
export const useAuthContext = () => useContext(AuthContext);

export default function WithAuthorization({ children }) {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const value = { isAuthenticated, setIsAuthenticated };
    const [isMounted, setIsMounted] = useState(false);
    const tokenName = 'alfred_token';
    const { Provider } = AuthContext;

    useEffect(() => {
        setIsMounted(true);
        return () => setIsMounted(false);
    }, []);

    function handleAuthStatus() {
        const token = localStorage.getItem(tokenName);
        const isExpired = auth.isTokenExpired(token);
        if (token && !isExpired) {
            const userData = auth.getProfile();
            const data = {
                isAuthenticated: true,
                user: userData
            };
            AuthContext.current = data;
            setIsAuthenticated(data);
        } else {
            localStorage.removeItem(tokenName);
            const data = {
                isAuthenticated: false,
                user: null
            };
            setIsAuthenticated(data);
        }
    }

    useEffect(() => {
        if (isMounted) handleAuthStatus();
        return () => handleAuthStatus();
    }, [isMounted]);

    if (!isMounted) return null;

    return (
        <Provider value={value}>
            {isAuthenticated.isAuthenticated ?
                children
                /* TODO: CREATE A REDIRECT COMPONENT */
                : <h1>Please Login</h1>}
        </Provider>
    );
}
