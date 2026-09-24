import os

BASE_DIR = r"C:\Users\ANSH\.gemini\antigravity\scratch\mahe-v2\frontend"

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def write_file(path, content):
    ensure_dir(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. main.css (500+ lines with programmatic utilities)
main_css = """
/* BASE VARIABLES & RESET */
:root {
    --bg-primary: #06060b;
    --bg-secondary: #0c0c14;
    --bg-tertiary: #161622;
    --bg-glass: rgba(12, 12, 20, 0.6);
    --bg-glass-hover: rgba(22, 22, 34, 0.8);
    
    --text-primary: #ffffff;
    --text-secondary: #a0a0b0;
    --text-muted: #6b6b7b;
    --text-inverse: #000000;
    
    --accent-cyan: #00f0ff;
    --accent-cyan-hover: #33f3ff;
    --accent-cyan-glow: rgba(0, 240, 255, 0.2);
    
    --accent-purple: #7b2ff7;
    --accent-purple-hover: #914dff;
    --accent-purple-glow: rgba(123, 47, 247, 0.2);
    
    --success: #00e676;
    --warning: #ffea00;
    --error: #ff1744;
    --info: #00b0ff;
    
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    
    --sidebar-width: 260px;
    --sidebar-width-collapsed: 80px;
    --navbar-height: 70px;
    
    --border-radius-sm: 6px;
    --border-radius-md: 12px;
    --border-radius-lg: 16px;
    --border-radius-xl: 24px;
    --border-radius-full: 9999px;
    
    --border-color: rgba(255, 255, 255, 0.1);
    --border-color-hover: rgba(255, 255, 255, 0.2);
    
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
    --shadow-lg: 0 10px 15px rgba(0,0,0,0.2);
    --shadow-glow-cyan: 0 0 20px var(--accent-cyan-glow);
    --shadow-glow-purple: 0 0 20px var(--accent-purple-glow);
    
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-normal: 250ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
    
    --z-index-dropdown: 1000;
    --z-index-sticky: 1020;
    --z-index-fixed: 1030;
    --z-index-modal-backdrop: 1040;
    --z-index-modal: 1050;
    --z-index-popover: 1060;
    --z-index-tooltip: 1070;
    --z-index-toast: 1080;
}

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    font-size: 16px;
    scroll-behavior: smooth;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

body {
    font-family: var(--font-sans);
    background-color: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    overflow-x: hidden;
    min-height: 100vh;
}

a {
    color: var(--accent-cyan);
    text-decoration: none;
    transition: color var(--transition-fast);
}

a:hover {
    color: var(--accent-cyan-hover);
}

img, picture, video, canvas, svg {
    display: block;
    max-width: 100%;
}

input, button, textarea, select {
    font: inherit;
    outline: none;
}

button {
    cursor: pointer;
    background: none;
    border: none;
}

ul, ol {
    list-style: none;
}

table {
    border-collapse: collapse;
    width: 100%;
}

/* TYPOGRAPHY */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 0.5em;
    color: var(--text-primary);
    letter-spacing: -0.02em;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.75rem; }
h4 { font-size: 1.5rem; }
h5 { font-size: 1.25rem; }
h6 { font-size: 1rem; }

p { margin-bottom: 1rem; }

.text-xs { font-size: 0.75rem; line-height: 1rem; }
.text-sm { font-size: 0.875rem; line-height: 1.25rem; }
.text-base { font-size: 1rem; line-height: 1.5rem; }
.text-lg { font-size: 1.125rem; line-height: 1.75rem; }
.text-xl { font-size: 1.25rem; line-height: 1.75rem; }
.text-2xl { font-size: 1.5rem; line-height: 2rem; }
.text-3xl { font-size: 1.875rem; line-height: 2.25rem; }

.font-light { font-weight: 300; }
.font-normal { font-weight: 400; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }

.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-justify { text-align: justify; }

.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }
.text-muted { color: var(--text-muted); }
.text-cyan { color: var(--accent-cyan); }
.text-purple { color: var(--accent-purple); }
.text-success { color: var(--success); }
.text-warning { color: var(--warning); }
.text-error { color: var(--error); }
.text-info { color: var(--info); }

.text-mono { font-family: var(--font-mono); }
.tracking-tight { letter-spacing: -0.05em; }
.tracking-normal { letter-spacing: 0; }
.tracking-wide { letter-spacing: 0.05em; }
.tracking-wider { letter-spacing: 0.1em; }
.tracking-widest { letter-spacing: 0.25em; }

.uppercase { text-transform: uppercase; }
.lowercase { text-transform: lowercase; }
.capitalize { text-transform: capitalize; }
.truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

/* LAYOUT & GRID */
.app-layout {
    display: flex;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
    position: relative;
}

.content-wrapper {
    display: flex;
    flex-direction: column;
    flex: 1;
    min-width: 0;
    height: 100%;
}

.main-content {
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 24px;
    position: relative;
    scroll-behavior: smooth;
}

.view-container {
    max-width: 1600px;
    margin: 0 auto;
    width: 100%;
    min-height: 100%;
    display: flex;
    flex-direction: column;
}

.container { width: 100%; margin-right: auto; margin-left: auto; padding-right: 1rem; padding-left: 1rem; }
@media (min-width: 640px) { .container { max-width: 640px; } }
@media (min-width: 768px) { .container { max-width: 768px; } }
@media (min-width: 1024px) { .container { max-width: 1024px; } }
@media (min-width: 1280px) { .container { max-width: 1280px; } }
@media (min-width: 1536px) { .container { max-width: 1536px; } }

.grid { display: grid; }
.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-cols-5 { grid-template-columns: repeat(5, minmax(0, 1fr)); }
.grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
.grid-cols-12 { grid-template-columns: repeat(12, minmax(0, 1fr)); }

.col-span-1 { grid-column: span 1 / span 1; }
.col-span-2 { grid-column: span 2 / span 2; }
.col-span-3 { grid-column: span 3 / span 3; }
.col-span-4 { grid-column: span 4 / span 4; }
.col-span-5 { grid-column: span 5 / span 5; }
.col-span-6 { grid-column: span 6 / span 6; }
.col-span-7 { grid-column: span 7 / span 7; }
.col-span-8 { grid-column: span 8 / span 8; }
.col-span-9 { grid-column: span 9 / span 9; }
.col-span-10 { grid-column: span 10 / span 10; }
.col-span-11 { grid-column: span 11 / span 11; }
.col-span-12 { grid-column: span 12 / span 12; }

.gap-0 { gap: 0; }
.gap-1 { gap: 0.25rem; }
.gap-2 { gap: 0.5rem; }
.gap-3 { gap: 0.75rem; }
.gap-4 { gap: 1rem; }
.gap-5 { gap: 1.25rem; }
.gap-6 { gap: 1.5rem; }
.gap-8 { gap: 2rem; }
.gap-10 { gap: 2.5rem; }
.gap-12 { gap: 3rem; }

.flex { display: flex; }
.inline-flex { display: inline-flex; }
.flex-row { flex-direction: row; }
.flex-col { flex-direction: column; }
.flex-wrap { flex-wrap: wrap; }
.flex-nowrap { flex-wrap: nowrap; }

.items-start { align-items: flex-start; }
.items-end { align-items: flex-end; }
.items-center { align-items: center; }
.items-baseline { align-items: baseline; }
.items-stretch { align-items: stretch; }

.justify-start { justify-content: flex-start; }
.justify-end { justify-content: flex-end; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }
.justify-evenly { justify-content: space-evenly; }

.flex-1 { flex: 1 1 0%; }
.flex-auto { flex: 1 1 auto; }
.flex-initial { flex: 0 1 auto; }
.flex-none { flex: none; }

/* SPACING UTILITIES (Generated via python) */
"""

# Generate spacing classes
spacing_scales = {0: '0', 1: '0.25rem', 2: '0.5rem', 3: '0.75rem', 4: '1rem', 5: '1.25rem', 6: '1.5rem', 8: '2rem', 10: '2.5rem', 12: '3rem', 16: '4rem', 20: '5rem', 24: '6rem', 32: '8rem'}
for key, val in spacing_scales.items():
    main_css += f".m-{key} {{ margin: {val}; }}\n"
    main_css += f".mt-{key} {{ margin-top: {val}; }}\n"
    main_css += f".mb-{key} {{ margin-bottom: {val}; }}\n"
    main_css += f".ml-{key} {{ margin-left: {val}; }}\n"
    main_css += f".mr-{key} {{ margin-right: {val}; }}\n"
    main_css += f".mx-{key} {{ margin-left: {val}; margin-right: {val}; }}\n"
    main_css += f".my-{key} {{ margin-top: {val}; margin-bottom: {val}; }}\n"
    main_css += f".p-{key} {{ padding: {val}; }}\n"
    main_css += f".pt-{key} {{ padding-top: {val}; }}\n"
    main_css += f".pb-{key} {{ padding-bottom: {val}; }}\n"
    main_css += f".pl-{key} {{ padding-left: {val}; }}\n"
    main_css += f".pr-{key} {{ padding-right: {val}; }}\n"
    main_css += f".px-{key} {{ padding-left: {val}; padding-right: {val}; }}\n"
    main_css += f".py-{key} {{ padding-top: {val}; padding-bottom: {val}; }}\n"

main_css += """
.m-auto { margin: auto; }
.mx-auto { margin-left: auto; margin-right: auto; }
.my-auto { margin-top: auto; margin-bottom: auto; }

/* SIZING */
.w-full { width: 100%; }
.w-screen { width: 100vw; }
.w-1\\/2 { width: 50%; }
.w-1\\/3 { width: 33.333333%; }
.w-2\\/3 { width: 66.666667%; }
.w-1\\/4 { width: 25%; }
.w-3\\/4 { width: 75%; }
.h-full { height: 100%; }
.h-screen { height: 100vh; }
.min-h-screen { min-height: 100vh; }
.min-h-full { min-height: 100%; }

/* BORDERS */
.border { border-width: 1px; }
.border-t { border-top-width: 1px; }
.border-b { border-bottom-width: 1px; }
.border-l { border-left-width: 1px; }
.border-r { border-right-width: 1px; }
.border-solid { border-style: solid; }
.border-dashed { border-style: dashed; }
.border-dotted { border-style: dotted; }
.border-transparent { border-color: transparent; }
.border-primary { border-color: var(--border-color); }
.border-accent { border-color: var(--accent-cyan); }

.rounded-none { border-radius: 0; }
.rounded-sm { border-radius: var(--border-radius-sm); }
.rounded-md { border-radius: var(--border-radius-md); }
.rounded-lg { border-radius: var(--border-radius-lg); }
.rounded-xl { border-radius: var(--border-radius-xl); }
.rounded-full { border-radius: var(--border-radius-full); }

/* BACKGROUNDS */
.bg-primary { background-color: var(--bg-primary); }
.bg-secondary { background-color: var(--bg-secondary); }
.bg-tertiary { background-color: var(--bg-tertiary); }
.bg-transparent { background-color: transparent; }

/* GLASSMORPHISM */
.glass-panel {
    background: var(--bg-glass);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-color);
    box-shadow: var(--shadow-md);
    transition: all var(--transition-normal);
}

.glass-panel:hover {
    border-color: var(--border-color-hover);
    box-shadow: var(--shadow-lg);
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: var(--bg-primary);
}
::-webkit-scrollbar-thumb {
    background: var(--bg-tertiary);
    border-radius: var(--border-radius-full);
    border: 2px solid var(--bg-primary);
}
::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted);
}
::-webkit-scrollbar-corner {
    background: var(--bg-primary);
}

/* RESPONSIVE BREAKPOINTS */
@media (max-width: 1024px) {
    .app-layout { flex-direction: column; }
    .sidebar { width: 100%; height: auto; border-right: none; border-bottom: 1px solid var(--border-color); flex-direction: row; }
    .content-wrapper { height: auto; flex: 1; }
    .grid-cols-12 { grid-template-columns: repeat(6, 1fr); }
    .col-span-6 { grid-column: span 6; }
}

@media (max-width: 768px) {
    .grid-cols-12, .grid-cols-6 { grid-template-columns: repeat(1, 1fr); }
    .col-span-12, .col-span-6, .col-span-4, .col-span-3 { grid-column: span 1; }
    .main-content { padding: 16px; }
}
"""

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MAHE V2 - Multi-Agent Hallucination Evaluator</title>
    <meta name="description" content="Advanced dashboard for evaluating LLM hallucinations using multi-agent systems.">
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- CSS -->
    <link rel="stylesheet" href="css/animations.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/dashboard.css">
</head>
<body class="dark-theme bg-primary text-primary antialiased">
    <!-- SVG Symbols for Icons -->
    <svg style="display: none;">
        <symbol id="icon-dashboard" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></symbol>
        <symbol id="icon-evaluate" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></symbol>
        <symbol id="icon-compare" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5"></path><path d="M8 3H3v5"></path><path d="M12 22v-8"></path><path d="M12 8V2"></path><path d="M3 21l6-6"></path><path d="M21 21l-6-6"></path></symbol>
        <symbol id="icon-history" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></symbol>
        <symbol id="icon-analytics" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></symbol>
        <symbol id="icon-settings" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></symbol>
        <symbol id="icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></symbol>
        <symbol id="icon-bell" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></symbol>
        <symbol id="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></symbol>
        <symbol id="icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></symbol>
        <symbol id="icon-alert" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></symbol>
    </svg>

    <div id="app-root" class="app-layout">
        <!-- Sidebar -->
        <aside id="sidebar" class="sidebar flex flex-col bg-secondary border-r border-primary transition-all duration-300">
            <!-- Sidebar populated by sidebar.js -->
        </aside>

        <!-- Main Content Wrapper -->
        <div class="content-wrapper">
            <!-- Navbar -->
            <header id="navbar" class="navbar sticky top-0 z-50 bg-glass backdrop-blur-md border-b border-primary flex items-center justify-between px-6 h-[70px]">
                <!-- Navbar populated by navbar.js -->
            </header>

            <!-- Main Scrollable Area -->
            <main id="main-content" class="main-content">
                <!-- Global Progress Bar -->
                <div id="global-progress" class="fixed top-0 left-0 w-full h-1 bg-transparent z-[1000] hidden">
                    <div class="progress-bar h-full bg-accent-cyan w-0 transition-all duration-300"></div>
                </div>

                <!-- Dynamic View Container -->
                <div id="view-container" class="view-container w-full h-full relative">
                    <!-- Views injected here by router.js -->
                </div>
            </main>
        </div>
    </div>

    <!-- Global Toast Container -->
    <div id="toast-container" class="fixed bottom-6 right-6 flex flex-col gap-3 z-[1080] pointer-events-none"></div>

    <!-- Global Modal Container -->
    <div id="modal-container" class="fixed inset-0 z-[1050] hidden flex items-center justify-center p-4">
        <div class="modal-backdrop absolute inset-0 bg-black bg-opacity-70 backdrop-blur-sm"></div>
        <div class="modal-content relative bg-secondary border border-primary rounded-xl shadow-2xl w-full max-w-2xl max-h-[90vh] flex flex-col transform scale-95 opacity-0 transition-all duration-300">
            <!-- Modal content injected here -->
        </div>
    </div>

    <!-- JavaScript Modules -->
    <script type="module" src="js/app.js"></script>
</body>
</html>
"""

# Let's execute the script building directly in python
files_to_write = {
    'frontend/index.html': index_html,
    'frontend/css/main.css': main_css,
    'frontend/js/app.js': """// app.js (Overwritten with comprehensive logic)
import Router from './router.js';
import Store from './store.js';
import { Api } from './api.js';
import { Socket } from './websocket.js';
import { initNavbar } from './components/navbar.js';
import { initSidebar } from './components/sidebar.js';
import { ToastManager } from './components/toast.js';

class App {
    constructor() {
        this.initializeStore();
        this.api = new Api();
        this.socket = new Socket('ws://localhost:8000/ws');
        this.toast = new ToastManager();
        this.router = new Router(this);
        
        // Global Error Boundary
        window.addEventListener('error', this.handleGlobalError.bind(this));
        window.addEventListener('unhandledrejection', this.handleGlobalPromiseRejection.bind(this));
        
        // Keyboard Shortcuts
        this.initKeyboardShortcuts();
    }

    initializeStore() {
        const defaultState = {
            user: { name: 'Admin', role: 'Superadmin' },
            activeView: 'dashboard',
            models: ['gpt-4-turbo', 'claude-3-opus', 'gemini-1.5-pro', 'llama-3-70b'],
            evaluations: [],
            stats: null,
            settings: {
                theme: 'dark',
                defaultTemperature: 0.7,
                autoSave: true,
                compactMode: false
            },
            isSidebarCollapsed: false,
            notifications: []
        };

        // Attempt to load from localStorage
        let savedState = {};
        try {
            const saved = localStorage.getItem('mahev2_state');
            if (saved) savedState = JSON.parse(saved);
        } catch(e) {
            console.warn('Failed to parse saved state', e);
        }

        window.store = new Store({ ...defaultState, ...savedState });

        // Subscribe to state changes for persistence
        window.store.subscribe((state) => {
            const persistState = { settings: state.settings, isSidebarCollapsed: state.isSidebarCollapsed };
            localStorage.setItem('mahev2_state', JSON.stringify(persistState));
            this.applyTheme(state.settings.theme);
        });
    }

    async init() {
        console.log('[MAHE V2] Initializing application...');
        
        // Setup UI Components
        initSidebar(this);
        initNavbar(this);
        
        // Setup Routes
        this.router.addRoute('/dashboard', () => this.loadView('dashboard'));
        this.router.addRoute('/evaluate', () => this.loadView('evaluate'));
        this.router.addRoute('/compare', () => this.loadView('compare'));
        this.router.addRoute('/history', () => this.loadView('history'));
        this.router.addRoute('/analytics', () => this.loadView('analytics'));
        this.router.addRoute('/settings', () => this.loadView('settings'));
        this.router.setDefaultRoute('/dashboard');

        // Start Router
        this.router.start();
        
        // Connect WebSocket
        this.socket.connect();
        
        // Load initial data
        await this.loadInitialData();
    }

    async loadInitialData() {
        try {
            const stats = await this.api.getStats();
            window.store.setState({ stats });
        } catch (error) {
            console.error('Failed to load initial stats', error);
            this.toast.error('Failed to load dashboard statistics');
        }
    }

    async loadView(viewName) {
        const viewContainer = document.getElementById('view-container');
        
        // Trigger transition out
        viewContainer.classList.add('opacity-0');
        
        // Show progress bar
        const progress = document.getElementById('global-progress');
        const progressBar = progress.querySelector('.progress-bar');
        progress.classList.remove('hidden');
        progressBar.style.width = '30%';
        
        try {
            // Lazy load the view module
            const module = await import(`./components/${viewName}.js`);
            progressBar.style.width = '70%';
            
            setTimeout(() => {
                const content = module.default.render();
                viewContainer.innerHTML = '';
                viewContainer.appendChild(content);
                
                if (module.default.init) {
                    module.default.init();
                }
                
                window.store.setState({ activeView: viewName });
                
                // Complete progress and fade in
                progressBar.style.width = '100%';
                setTimeout(() => {
                    progress.classList.add('hidden');
                    progressBar.style.width = '0%';
                    viewContainer.classList.remove('opacity-0');
                    viewContainer.classList.add('opacity-100');
                }, 200);
            }, 100);
        } catch (error) {
            console.error(`Error loading view: ${viewName}`, error);
            this.toast.error(`Failed to load view: ${viewName}`);
            progressBar.style.backgroundColor = 'var(--error)';
            setTimeout(() => progress.classList.add('hidden'), 1000);
            
            viewContainer.innerHTML = `
                <div class="flex flex-col items-center justify-center h-full text-center">
                    <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="var(--error)" stroke-width="2" class="mb-4"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    <h2 class="text-2xl font-bold text-error mb-2">Failed to load module</h2>
                    <p class="text-muted max-w-md">${error.message}</p>
                    <button class="btn btn-primary mt-6" onclick="window.location.reload()">Reload Application</button>
                </div>
            `;
            viewContainer.classList.remove('opacity-0');
        }
    }

    applyTheme(theme) {
        if (theme === 'light') {
            document.body.classList.remove('dark-theme');
            document.body.classList.add('light-theme');
        } else {
            document.body.classList.remove('light-theme');
            document.body.classList.add('dark-theme');
        }
    }

    handleGlobalError(event) {
        console.error('Global Error Caught:', event.error);
        this.toast.error('An unexpected error occurred. See console for details.');
    }

    handleGlobalPromiseRejection(event) {
        console.error('Unhandled Promise Rejection:', event.reason);
        this.toast.error('A background task failed unexpectedly.');
    }

    initKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Cmd/Ctrl + K for global search focus
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                const search = document.getElementById('global-search');
                if (search) search.focus();
            }
            // Cmd/Ctrl + / for quick evaluate
            if ((e.metaKey || e.ctrlKey) && e.key === '/') {
                e.preventDefault();
                this.router.navigate('/evaluate');
            }
        });
    }
}

// Bootstrap
document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
    window.app.init();
});
""",
    'frontend/js/store.js': """// store.js (Expanded Reactive Store with Middleware support)
export default class Store {
    constructor(initialState = {}) {
        this.state = initialState;
        this.listeners = new Set();
        this.middlewares = [];
        this.isMutating = false;
    }

    getState() {
        // Return a shallow copy to prevent direct mutation
        return { ...this.state };
    }

    setState(partialState, actionType = 'SET_STATE') {
        if (this.isMutating) {
            console.warn('Store: setState called while already mutating. This might lead to unexpected behavior.');
        }

        this.isMutating = true;
        
        // Run middlewares before state change
        let nextState = { ...this.state, ...partialState };
        
        for (const mw of this.middlewares) {
            nextState = mw(this.state, nextState, actionType) || nextState;
        }

        const prevState = this.state;
        this.state = nextState;
        this.isMutating = false;

        this.notify(prevState, this.state, actionType);
    }

    subscribe(listener) {
        this.listeners.add(listener);
        // Immediately invoke with current state
        listener(this.state, this.state, 'SUBSCRIBE');
        
        return () => {
            this.listeners.delete(listener);
        };
    }

    notify(prevState, nextState, actionType) {
        for (const listener of this.listeners) {
            try {
                listener(nextState, prevState, actionType);
            } catch (err) {
                console.error('Store: Error in listener:', err);
            }
        }
    }

    addMiddleware(middleware) {
        if (typeof middleware === 'function') {
            this.middlewares.push(middleware);
        }
    }

    // Selectors for derived state
    select(selectorFn) {
        return selectorFn(this.state);
    }
}
""",
    'frontend/js/router.js': """// router.js (Expanded client-side hash router)
export default class Router {
    constructor(appInstance) {
        this.app = appInstance;
        this.routes = new Map();
        this.defaultRoute = '/';
        this.currentRoute = null;
        this.history = [];
        
        // Bind event listeners
        window.addEventListener('hashchange', this.handleRoute.bind(this));
    }

    addRoute(path, callback, guards = []) {
        // Convert path to regex if it has parameters (e.g. /evaluations/:id)
        const paramNames = [];
        const regexPath = path.replace(/\\/:([^\\/]+)/g, (match, paramName) => {
            paramNames.push(paramName);
            return '([^\\/]+)';
        });
        
        this.routes.set(path, {
            regex: new RegExp(`^${regexPath}$`),
            paramNames,
            callback,
            guards
        });
    }

    setDefaultRoute(path) {
        this.defaultRoute = path;
    }

    start() {
        if (!window.location.hash) {
            window.location.hash = this.defaultRoute;
        } else {
            this.handleRoute();
        }
    }

    async handleRoute() {
        let path = window.location.hash.slice(1) || '/';
        if (path !== '/' && !path.startsWith('/')) {
            path = '/' + path;
        }

        let routeMatched = false;

        for (const [routePath, routeDef] of this.routes.entries()) {
            const match = path.match(routeDef.regex);
            
            if (match) {
                routeMatched = true;
                
                // Execute guards
                let canProceed = true;
                for (const guard of routeDef.guards) {
                    if (!(await guard(this.app))) {
                        canProceed = false;
                        break;
                    }
                }
                
                if (!canProceed) return;

                // Extract params
                const params = {};
                routeDef.paramNames.forEach((name, index) => {
                    params[name] = match[index + 1];
                });

                // Update history
                this.history.push(path);
                if (this.history.length > 20) this.history.shift();
                
                this.currentRoute = path;
                
                // Execute route callback
                try {
                    await routeDef.callback(params);
                } catch(e) {
                    console.error('Route callback failed', e);
                }
                break;
            }
        }

        if (!routeMatched) {
            console.warn(`Route not found: ${path}`);
            window.location.hash = this.defaultRoute;
        }
    }

    navigate(path) {
        if (!path.startsWith('#')) {
            path = '#' + path;
        }
        window.location.hash = path;
    }
    
    goBack() {
        if (this.history.length > 1) {
            this.history.pop(); // remove current
            const prev = this.history.pop(); // get prev
            this.navigate(prev);
        } else {
            this.navigate(this.defaultRoute);
        }
    }
}
""",
    'frontend/js/components/toast.js': """// toast.js (Expanded toast notification manager)
export class ToastManager {
    constructor() {
        this.container = document.getElementById('toast-container');
        this.toasts = new Map();
        this.toastCount = 0;
    }

    show(message, type = 'info', options = {}) {
        const duration = options.duration || 4000;
        const id = `toast_${++this.toastCount}`;
        
        const toast = document.createElement('div');
        toast.id = id;
        toast.className = `toast toast-${type} glass-panel pointer-events-auto flex items-start p-4 rounded-lg min-w-[300px] max-w-md transform transition-all duration-300 translate-x-full opacity-0`;
        
        // Icons
        const icons = {
            success: `<svg class="w-5 h-5 text-success flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>`,
            error: `<svg class="w-5 h-5 text-error flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>`,
            warning: `<svg class="w-5 h-5 text-warning flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>`,
            info: `<svg class="w-5 h-5 text-info flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`
        };

        toast.innerHTML = `
            <div class="mr-3 mt-0.5">${icons[type] || icons.info}</div>
            <div class="flex-1 mr-2">
                ${options.title ? `<h4 class="text-sm font-semibold mb-1">${options.title}</h4>` : ''}
                <p class="text-sm text-secondary">${message}</p>
            </div>
            <button class="text-muted hover:text-primary transition-colors focus:outline-none" onclick="window.app.toast.dismiss('${id}')">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
            <div class="absolute bottom-0 left-0 h-1 bg-${type} opacity-50 transition-all duration-linear" style="width: 100%;"></div>
        `;

        this.container.appendChild(toast);
        this.toasts.set(id, toast);

        // Animate in
        requestAnimationFrame(() => {
            toast.classList.remove('translate-x-full', 'opacity-0');
        });

        // Setup auto-dismiss progress bar
        const progressBar = toast.querySelector('.absolute.bottom-0');
        if (progressBar && duration > 0) {
            progressBar.style.transitionDuration = `${duration}ms`;
            requestAnimationFrame(() => {
                progressBar.style.width = '0%';
            });
        }

        if (duration > 0) {
            const timeoutId = setTimeout(() => {
                this.dismiss(id);
            }, duration);
            toast.dataset.timeoutId = timeoutId;
        }
    }

    success(message, options) { this.show(message, 'success', options); }
    error(message, options) { this.show(message, 'error', options); }
    warning(message, options) { this.show(message, 'warning', options); }
    info(message, options) { this.show(message, 'info', options); }

    dismiss(id) {
        const toast = this.toasts.get(id);
        if (toast) {
            if (toast.dataset.timeoutId) clearTimeout(parseInt(toast.dataset.timeoutId));
            
            toast.classList.add('translate-x-full', 'opacity-0');
            setTimeout(() => {
                toast.remove();
                this.toasts.delete(id);
            }, 300); // Wait for transition
        }
    }
}
"""
}

for path, content in files_to_write.items():
    write_file(path, content)

print("Batch 1 extension completed.")
