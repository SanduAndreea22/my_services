(function() {
    const btn = document.getElementById('theme-toggle');
    const icon_span = document.getElementById('theme-icon');
    // Return current theme, default dark
    function getTheme() {
        if (localStorage.getItem('theme')) return localStorage.getItem('theme');
        // If no pref, match system
        return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }
    // Set data-theme attr
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        if (theme === 'light') {
            icon_span.textContent = "🌞";
        } else {
            icon_span.textContent = "🌙";
        }
    }
    // On load
    setTheme(getTheme());
    // Toggle
    btn && btn.addEventListener('click', function() {
        const newTheme = (getTheme() === 'dark') ? 'light' : 'dark';
        localStorage.setItem('theme', newTheme);
        setTheme(newTheme);
    });
})();