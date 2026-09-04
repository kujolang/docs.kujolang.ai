import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const [inputSvg, outputJpeg, sharpEntry] = process.argv.slice(2);

if (!inputSvg || !outputJpeg || !sharpEntry) {
	console.error('Usage: node scripts/rasterize-social-card.mjs INPUT_SVG OUTPUT_JPEG SHARP_ENTRY');
	process.exit(1);
}

const sharpModule = await import(pathToFileURL(path.resolve(sharpEntry)).href);
const sharp = sharpModule.default;
const svg = await readFile(inputSvg);

await sharp(svg, { density: 144 })
	.resize(1200, 630, { fit: 'fill' })
	.flatten({ background: '#ffffff' })
	.jpeg({ quality: 90, chromaSubsampling: '4:4:4', progressive: true })
	.toFile(outputJpeg);

console.log(`Rasterized ${outputJpeg}`);
