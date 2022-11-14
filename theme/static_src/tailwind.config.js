/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        fontFamily: {
            'sans': 'IBM Plex Sans, sans-serif',
        },
        extend: {
            colors: {
                'primary': '#98EE6F',
                'primary-contrast': '#93E76C',
                'primary-hover': '#98EE6F50',
                'white': '#FFFFFF',
                'light-gray': '#D9D9D9',
                'gray': '#676767',
                'black': '#3D3D3D',
                'background-color': '#FAFAFA',
                'contrast': '#4A9E68',
                'shape': '#C1C1C1',
                'success-color': '#58AE30',
                'error-color': '#C92A2A',
                'primary-transparent-color': 'rgba(152, 238, 111, 0.08)',
                'error-transparent-color': 'rgba(201, 42, 42, 0.1)',
            },
            gridTemplateColumns: {
                'view': '0fr 1fr;',
            },
            width: {
                '60%': '60%',
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
