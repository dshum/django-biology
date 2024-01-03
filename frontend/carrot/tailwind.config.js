/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/flowbite/**/*.js',
  ],
  darkMode: 'class',
  theme: {
    container: {
      center: true,
      padding: '1rem',
    },
    fontFamily: {
      'logo': ['"Rubik Moonrocks"'],
      'sans': ['Montserrat', 'ui-sans-serif', 'system-ui']
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}