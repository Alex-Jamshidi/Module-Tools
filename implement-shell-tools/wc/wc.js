const fs = require("fs");
const { allowedNodeEnvironmentFlags } = require("process");

const arguments = process.argv;
const userArguments = arguments.slice(2);

const index = arguments[1].lastIndexOf("/");
const currentWorkingDirectory = arguments[1].slice(0, index + 1);

const flags = userArguments
  .filter((argument) => argument.startsWith("-"))
  .map((argument) => argument.slice(1))
  .join("");

const flagHandlers = {
  l: lFlag,
  w: wFlag,
  c: cFlag,
};

const metrics = ["lineCount", "wordCount", "byteSize"];
const fileNames = userArguments.filter((argument) => !argument.startsWith("-"));
const allFilesData = [];

extractFilesData();
addTotals();
const outputData = structuredClone(allFilesData);

let deleted = false;
executeFlags();
printOutput();

function extractFilesData() {
  fileNames.forEach((fileName) => {
    const fileData = {};
    fileData.name = fileName;
    fileData.text = readFile(fileName);
    fileData.lineCount = calculateLineCount(fileData.text);
    fileData.wordCount = calculateWordCount(fileData.text);
    fileData.byteSize = readByteSize(fileName);

    allFilesData.push(fileData);
  });
}

function addTotals() {
  if (allFilesData.length == 1) {
    return;
  }
  const totalsData = { name: "total" };
  metrics.forEach((metric) => {
    let sum = 0;
    allFilesData.forEach((file) => {
      sum += file[metric];
    });
    totalsData[metric] = sum;
  });
  allFilesData.push(totalsData);
}

function readFile(fileName) {
  const filePath = currentWorkingDirectory + fileName;
  return fs.readFileSync(filePath, "utf8").trimEnd();
}

function calculateLineCount(text) {
  return text.split("\n").length;
}

function calculateWordCount(text) {
  return text.split(/\s+/).length;
}

function readByteSize(fileName) {
  return fs.statSync(currentWorkingDirectory + fileName).size;
}

function executeFlags() {
  for (const flag of flags) {
    if (flagHandlers[flag]) {
      allFilesContents = flagHandlers[flag]();
    } else {
      console.error(`wc: illegal option -- ${flag}\nusage: wc [-Lclmw] [file ...]`);
      process.exit(1);
    }
  }
}

function lFlag() {
  deleteOutputs();
  allFilesData.forEach((sourceFile) => {
    const targetFile = outputData.find((file) => file.name === sourceFile.name);
    targetFile.lineCount = getIfTrue(sourceFile, "lineCount");
  });
}

function wFlag() {
  deleteOutputs();
  allFilesData.forEach((sourceFile) => {
    const targetFile = outputData.find((file) => file.name === sourceFile.name);
    targetFile.wordCount = getIfTrue(sourceFile, "wordCount");
  });
}

function cFlag() {
  deleteOutputs();
  allFilesData.forEach((sourceFile) => {
    const targetFile = outputData.find((file) => file.name === sourceFile.name);
    targetFile.byteSize = getIfTrue(sourceFile, "byteSize");
  });
}

function deleteOutputs() {
  if (!deleted) {
    outputData.forEach((file) => {
      metrics.forEach((metric) => {
        delete file[metric];
      });
    });
  }
  deleted = true;
}

function printOutput() {
  outputs = [];
  outputData.forEach((file) => {
    let outputString = "";
    metrics.forEach((metric) => {
      outputString += getIfTrue(file, metric);
    });
    outputString += ` ${file.name}`;
    console.log(outputString);
  });
}

function getIfTrue(file, metric) {
  if (file[metric]) {
    return String(file[metric]).padStart(8, " ");
  }
  return "";
}
