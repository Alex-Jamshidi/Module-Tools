const fs = require("fs");

const arguments = process.argv;
const userArguments = arguments.slice(2);

const index = arguments[1].lastIndexOf("/");
const currentWorkingDirectory = arguments[1].slice(0, index + 1);

const flags = userArguments
  .filter((argument) => argument.startsWith("-"))
  .map((argument) => argument.slice(1))
  .join("");

const flagHandlers = {
  b: bFlag,
  n: nFlag,
};

const fileNames = userArguments.filter((argument) => !argument.startsWith("-"));
let allFilesContents = [];

readFiles();
executeFlags();
printLines();

function readFiles() {
  fileNames.forEach((fileName) => {
    fileContent = readFile(fileName);
    allFilesContents.push(fileContent.split("\n"));
  });
}

function readFile(fileName) {
  const filePath = currentWorkingDirectory + fileName;
  return fs.readFileSync(filePath, "utf8").trimEnd();
}

function executeFlags() {
  for (const flag of flags) {
    if (flagHandlers[flag]) {
      allFilesContents = flagHandlers[flag]();
    } else {
      console.error(`cat: illegal option -- ${flag}\nusage: cat [-belnstuv] [file ...]`);
      process.exit(1);
    }
  }
}

function bFlag() {
  const resultFiles = [];

  for (const fileContent of allFilesContents) {
    const formattedLines = [];
    let lineNumber = 1;

    for (const line of fileContent) {
      if (line === "") {
        formattedLines.push(line);
      } else {
        const formattedLine = `${String(lineNumber++).padStart(6, " ")} ${line}`;
        formattedLines.push(formattedLine);
      }
    }

    resultFiles.push(formattedLines);
  }

  return resultFiles;
}

function nFlag() {
  return allFilesContents.map((fileContent) => {
    return fileContent.map((line, index) => `${String(index + 1).padStart(6, " ")} ${line}`);
  });
}

function printLines() {
  allFilesContents.forEach((fileContent) => {
    fileContent.forEach((line) => {
      console.log(line);
    });
  });
}
