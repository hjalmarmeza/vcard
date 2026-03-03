const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        
        // Configurar viewport como HD y que simule lo visible en web
        await page.setViewport({ width: 1440, height: 900 });
        
        const htmlPath = path.resolve('/Users/hjalmarmeza/Downloads/Antigravity/CV/index.html');
        // Usar wait until load para evitar recargas cortas y fuentes rotas
        await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });
        
        const outputPath = '/Users/hjalmarmeza/Downloads/Antigravity/CV/portada_linkedin.png';
        const outputPath2 = '/Users/hjalmarmeza/Downloads/Antigravity/CV/portada_linkedin2.png';

        // Capturar una sección específica. Primero esconder los scrolls si es que salen en mac.
        // Haremos un screenshot solo de la parte de arriba donde se define quién eres
        await page.screenshot({ 
            path: outputPath,
            clip: { x: 0, y: 0, width: 1440, height: 900 }
        });

        // Haremos otra de todo el site
        const rootHandle = await page.$('.min-h-screen');
        if (rootHandle){
             await rootHandle.screenshot({ path: outputPath2 });    
        }
        
        await browser.close();
        console.log('Capturas generadas en descargas/CV');
    } catch(err) {
        console.error("Error capturando pantalla", err);
    }
})();
