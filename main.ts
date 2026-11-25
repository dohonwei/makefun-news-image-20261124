// News image entry (Node 22, standard library only).
// The image was drawn by draw.py from the day's news and saved as
// entry.png, which is stored in this repository as one line of
// base64 in entry.png.b64 (the push tool takes text files only).
// This program decodes it into the output directory the grader
// provides, so both runs produce the same bytes: a 1024 x 1024
// PNG, under 1 MiB. Nothing is fetched and nothing is drawn at
// run time; the image is already in the repo. The decode is
// deterministic: the same base64 always produces the same PNG,
// so the two grader runs match byte for byte.
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const here = dirname(fileURLToPath(import.meta.url));
const png = Buffer.from(readFileSync(join(here, 'entry.png.b64'), 'utf8').trim(), 'base64');
writeFileSync(join(outDir, 'entry.png'), png);
