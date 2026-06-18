import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const outputPath = resolve(__dirname, '../src/environments/environment.generated.ts');
const apiBaseUrl = process.env.BACKEND_URL || '/api';

mkdirSync(dirname(outputPath), { recursive: true });

writeFileSync(
  outputPath,
  `export const environment = {\n  apiBaseUrl: ${JSON.stringify(apiBaseUrl)},\n};\n`,
);

console.log(`Using BACKEND_URL=${apiBaseUrl}`);
