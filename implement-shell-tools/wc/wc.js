const fs = require("fs");
const { allowedNodeEnvironmentFlags } = require("process");

const metrics = ["lineCount", "wordCount", "byteSize"];
const displayedMetrics = [];

//
// ===== wc Procedure =====
function wc(args) {
  const userArgs = args.slice(2);

  executeFlags(getFlags(userArgs));

  const currentWorkingDirectory = getCurrentWorkingDirectory(args);
  const fileNames = getFileNames(userArgs);

  const allFilesData = addTotals(extractFilesData(fileNames, currentWorkingDirectory));
  printOutput(allFilesData);
}

//
// ===== Flag Handling =====
const flagHandlers = {
  l: lFlag,
  w: wFlag,
  c: cFlag,
};

function getFlags(userArgs) {
  return userArgs
    .filter((arg) => arg.startsWith("-"))
    .map((arg) => arg.slice(1))
    .join("");
}

function executeFlags(flags) {
  for (const flag of flags) {
    if (flagHandlers[flag]) flagHandlers[flag]();
    else invalidFlagError();
  }
}

function invalidFlagError() {
  console.error(`wc: illegal option -- ${flag}\nusage: wc [-Lclmw] [file ...]`);
  process.exit(1);
}

function lFlag() {
  displayedMetrics.push("lineCount");
}

function wFlag() {
  displayedMetrics.push("wordCount");
}

function cFlag() {
  displayedMetrics.push("byteSize");
}

//
// ===== Extracting Data From Arguments =====
function getCurrentWorkingDirectory(args) {
  const index = args[1].lastIndexOf("/");
  return args[1].slice(0, index + 1);
}

function getFileNames(userArgs) {
  return userArgs.filter((argument) => !argument.startsWith("-"));
}

//
// ===== Extracting Files Data =====
function extractFilesData(fileNames, currentWorkingDirectory) {
  const allFilesData = [];

  fileNames.forEach((fileName) => {
    const fileData = {};
    fileData.name = fileName;
    fileData.text = readFile(fileName, currentWorkingDirectory);
    fileData.lineCount = calculateLineCount(fileData.text);
    fileData.wordCount = calculateWordCount(fileData.text);
    fileData.byteSize = readByteSize(fileName, currentWorkingDirectory);

    allFilesData.push(fileData);
  });
  return allFilesData;
}

function readFile(fileName, currentWorkingDirectory) {
  const filePath = currentWorkingDirectory + fileName;
  return fs.readFileSync(filePath, "utf8").trimEnd();
}

function calculateLineCount(text) {
  return text.split("\n").length;
}

function calculateWordCount(text) {
  return text.split(/\s+/).length;
}

function readByteSize(fileName, currentWorkingDirectory) {
  return fs.statSync(currentWorkingDirectory + fileName).size;
}

function addTotals(allFilesData) {
  if (allFilesData.length == 1) return allFilesData;

  const totalsData = { name: "total" };
  metrics.forEach((metric) => {
    let sum = 0;
    allFilesData.forEach((file) => {
      sum += file[metric];
    });
    totalsData[metric] = sum;
  });
  allFilesData.push(totalsData);
  return allFilesData;
}

//
// ===== Outputting Data =====
function printOutput(outputData) {
  outputData.forEach((file) => {
    let outputString = "";
    metrics.forEach((metric) => {
      if (displayedMetrics.length === 0 || displayedMetrics.includes(metric)) {
        outputString += String(file[metric]).padStart(8, " ");
      }
    });

    outputString += ` ${file.name}`;
    console.log(outputString);
  });
}

//
// ===== Run wc =====
wc(process.argv);
