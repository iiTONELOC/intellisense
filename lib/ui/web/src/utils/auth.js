import decode from 'jwt-decode';

class AuthService {

    getProfile() {
        try {
            return decode(this.getToken());
        } catch (error) {
            return null;
        }
    };

    loggedIn() {
        const token = this.getToken();
        return !!token && !this.isTokenExpired(token);
    }

    isTokenExpired(token) {
        try {
            const decoded = decode(token);
            return decoded.exp < Date.now() / 1000;
        } catch (err) {
            return false;
        }
    }

    // retrieve token from localStorage
    getToken() {
        // Retrieves the user token from localStorage
        return localStorage.getItem('alfred_token');
    }

    // set token to localStorage and reload page to homepage
    async login(idToken) {
        // Saves user token to localStorage
        localStorage.setItem('alfred_token', idToken);
        setTimeout(async () => {
            const uData = await this.getProfile();
            window.location.replace(`/users/${uData.id}/dashboard`);
            return true;
        }, 250);
    }

    logout() {
        localStorage.removeItem('alfred_token');
        window.location.replace('/');
    }
}

export default new AuthService();
