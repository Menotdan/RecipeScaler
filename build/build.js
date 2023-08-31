const { execSync } = require('child_process');
var fs = require('fs')
var fse = require('fs-extra')

// Clear old directories.
fse.emptyDirSync("./built-site");

// Compile typescript and print any errors.
execSync('tsc -p ./src/tsconfig.json --outDir ./built-site', function callback(error, stdout, stderr) {
  console.log(stderr);
  console.log(stdout);
});

// Copy html files
fs.cp("./src/", "./built-site", {
    filter(src, dest) {
        return src.includes(".html") || src.includes(".css") || !src.includes(".");
    },
    recursive: true,
    force: true
}, (err) => { });

console.log("Built site successfully.");