const fs = require("fs");

//
// ===== cat Procedure =====
function cat(args) {
  const userArgs = args.slice(2);
  const currentWorkingDirectory = getCurrentWorkingDirectory(args);
  const fileNames = getFileNames(userArgs, currentWorkingDirectory);

  const allFilesContents = readFiles(fileNames, currentWorkingDirectory);
  executeFlags(getFlags(userArgs), allFilesContents);
  printLines(allFilesContents);
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

function readFiles(fileNames, currentWorkingDirectory) {
  const allFilesContents = [];
  fileNames.forEach((fileName) => {
    fileContent = readFile(fileName, currentWorkingDirectory);
    allFilesContents.push(fileContent.split("\n"));
  });
  return allFilesContents;
}

function readFile(fileName, currentWorkingDirectory) {
  const filePath = currentWorkingDirectory + fileName;
  return fs.readFileSync(filePath, "utf8").trimEnd();
}

//
// ===== Flag Handling =====
const flagHandlers = {
  b: bFlag,
  n: nFlag,
};

function getFlags(userArgs) {
  return userArgs
    .filter((arg) => arg.startsWith("-"))
    .map((arg) => arg.slice(1))
    .join("");
}

function executeFlags(flags, allFilesContents) {
  for (const flag of flags) {
    if (flagHandlers[flag]) flagHandlers[flag](allFilesContents, flags);
    else invalidFlagError();
  }
}

function invalidFlagError() {
  console.error(`cat: illegal option -- ${flag}\nusage: cat [-belnstuv] [file ...]`);
  process.exit(1);
}

function bFlag(allFilesContents) {
  let linenumber = 1;
  allFilesContents.forEach((fileContent) => {
    fileContent.forEach((line, index) => {
      if (line !== "") {
        fileContent[index] = `${String(linenumber).padStart(6, " ")} ${line}`;
        linenumber += 1;
      }
    });
  });
}

function nFlag(allFilesContents, flags) {
  if (!flags.includes("b")) {
    allFilesContents.forEach((fileContent) => {
      fileContent.forEach((line, index) => (fileContent[index] = `${String(index + 1).padStart(6, " ")} ${line}`));
    });
  }
}

//
// ==== Print Output =====
function printLines(allFilesContents) {
  allFilesContents.forEach((fileContent) => {
    fileContent.forEach((line) => {
      console.log(line);
    });
  });
}

//
// ===== Run cat =====
cat(process.argv);
