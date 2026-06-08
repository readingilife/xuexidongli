const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(express.json({ limit: '10mb' }));
app.use(express.static(path.join(__dirname, '..')));

app.post('/api/save-report', (req, res) => {
    try {
        const { html, filename } = req.body;
        const savePath = path.join(__dirname, '..', 'xuexili', filename);
        fs.writeFileSync(savePath, html, 'utf8');
        res.json({ success: true, path: savePath });
    } catch (error) {
        console.error('Error saving report:', error);
        res.status(500).json({ success: false, error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
    console.log(`Open CMS/report-editor.html to use the editor`);
});
