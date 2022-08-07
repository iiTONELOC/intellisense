import decode from 'jwt-decode';

class AuthService {

    getProfile() {
        try {
            return decode(this.getToken());
        } catch (error) {
            return null
        };
    };

    loggedIn() {
        const token = this.getToken();
        return !!token && !this.isTokenExpired(token);
    };

    isTokenExpired(token) {
        try {
            const decoded = decode(token);
            if (decoded.exp < Date.now() / 1000) {
                return true;
            } else {
                return false;
            }
        } catch (err) {
            return false;
        };
    };

    // retrieve token from localStorage
    getToken() {
        // Retrieves the user token from localStorage
        return localStorage.getItem('jarvis_token');
    }

    // set token to localStorage and reload page to homepage
    async login(idToken) {
        // Saves user token to localStorage
        localStorage.setItem('jarvis_token', idToken);
        setTimeout(async () => {
            const uData = await this.getProfile();
            window.location.replace(`/users/${uData.id}/dashboard`);
            return true
        }, 250);
    };

    logout() {
        localStorage.removeItem('jarvis_token');
        window.location.replace('/');
    };
};

export default new AuthService();