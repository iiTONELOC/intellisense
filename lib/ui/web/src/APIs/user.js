import auth from '../utils/auth';

const CONTENT_TYPE = 'application/json';

export const UserAPI = {
    loginUser: userData => {
        return fetch('/api/users/login', {
            method: 'POST',
            headers: {
                'Content-Type': CONTENT_TYPE
            },
            body: JSON.stringify(userData)
        });
    },
    createNewUser: userData => {
        return fetch('/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': CONTENT_TYPE
            },
            body: JSON.stringify(userData)
        });
    },
    remoteAccess: userData => {
        return fetch('/api/remote', {
            method: 'POST',
            headers: {
                'Content-Type': CONTENT_TYPE,
                'Authorization': `Bearer ${auth.getToken()}`
            },
            body: JSON.stringify(userData)
        });
    },
    deviceStatusAll: () => {
        return fetch('/api/deviceStatus', {
            method: 'GET',
            headers: {
                'Content-Type': CONTENT_TYPE,
                'Authorization': `Bearer ${auth.getToken()}`
            }
        });
    }
};
