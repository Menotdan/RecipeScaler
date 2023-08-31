const { execSync } = require('child_process');
var fs = require('fs')

// Clear old directories.
fs.rmSync("built-site", { recursive: true, force: true });

// Compile typescript and print any errors.
execSync('tsc -p ./src/tsconfig.json --outDir ./built-site', function callback(error, stdout, stderr) {
  console.log(stderr);
  console.log(stdout);
});

// Copy html files
fs.cp("./src/", "./built-site", {
    filter(src, dest) {
        return src.includes(".html") || !src.includes(".");
    },
    recursive: true,
    force: true
}, (err) => { });

console.log("Built site successfully.");