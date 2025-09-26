# FleTodo - Standalone Single Page Application

A simple and elegant todo list application built with pure HTML, CSS, and JavaScript.

## Features

✅ **Add Todos**: Create new todo items with a simple text input  
✅ **Mark Complete**: Check off completed tasks  
✅ **Delete Todos**: Remove tasks you no longer need  
✅ **Persistent Storage**: Data is saved in browser's localStorage  
✅ **Responsive Design**: Works on desktop and mobile devices  
✅ **Progressive Web App**: Can be installed on devices  
✅ **Offline Support**: Works without internet connection  

## Quick Start

1. **Open the app**: Simply open `index.html` in any modern web browser
2. **Add a todo**: Type in the input field and click "Add Todo" or press Enter
3. **Mark complete**: Click the checkbox next to any todo item
4. **Delete**: Click the 🗑️ button to remove a todo
5. **Data persistence**: Your todos are automatically saved and will be there when you return

## Deployment Options

### Static Web Hosting
Upload all files to any static hosting service:
- GitHub Pages
- Netlify  
- Vercel
- Amazon S3 + CloudFront
- Any web server

### Local Testing
Use Python's built-in server:
```bash
python3 -m http.server 8080
```
Then open http://localhost:8080

### Web Server
Configure any web server (Apache, Nginx) to serve the files.

## File Structure

```
release/
├── index.html          # Main application file
├── styles.css          # Application styles
├── app.js             # Application logic
├── manifest.json      # PWA manifest
├── sw.js             # Service worker for offline support
└── README.md         # This documentation
```

## Browser Compatibility

Works in all modern browsers including:
- Chrome (65+)
- Firefox (60+)
- Safari (12+)
- Edge (79+)

## Technical Details

- **No external dependencies**: Everything runs locally
- **LocalStorage**: Data persists between sessions
- **Service Worker**: Enables offline functionality
- **Responsive CSS**: Mobile-first design
- **Vanilla JavaScript**: No frameworks required
- **Progressive Enhancement**: Works with JavaScript disabled (basic functionality)

## Data Privacy

- All data is stored locally in your browser
- No data is sent to external servers
- No tracking or analytics
- Complete privacy and control over your todos

## Customization

You can easily customize the app by editing:
- `styles.css` - Change colors, fonts, layout
- `app.js` - Modify functionality or add features
- `index.html` - Update structure or content

## License

MIT License - Feel free to use, modify, and distribute.

---

Built with ❤️ using pure web technologies.