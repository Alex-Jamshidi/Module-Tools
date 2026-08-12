const fs = require("fs");
const { allowedNodeEnvironmentFlags } = require("process");

const args = process.argv;
const userArgs = args.slice(2);

const index = args[1].lastIndexOf("/");
const currentWorkingDirectory = args[1].slice(0, index);

const flags = userArgs
  .filter((arg) => arg.startsWith("-"))
  .map((arg) => arg.slice(1))
  .join("");

const flagHandlers = {
  1: Flag1,
  a: Flaga,
};

let printInList = false;
let showAll = false;

const fsItems = userArgs.filter((arg) => !arg.startsWith("-"));
let dirArgs;
let fileArgs;
let outputString = "";

checkArgsLength();
executeFlags();
filterFilesAndDirs();
populateOutput();
print();

function executeFlags() {
  for (const flag of flags) {
    if (flagHandlers[flag]) {
      allFilesContents = flagHandlers[flag]();
    } else {
      console.error(
        `ls: invalid option -- ${flag}\nusage: ls [-@ABCFGHILOPRSTUWXabcdefghiklmnopqrstuvwxy1%,] [--color=when] [-D format] [file ...]`,
      );
      process.exit(1);
    }
  }
}

function Flag1() {
  if (printInList) {
    outputString = outputString.replaceAll("\t", "\n");
    outputString = outputString.replaceAll("\n\n", "\n");
  } else {
    printInList = true;
  }
}

function Flaga() {
  showAll = true;
}

function checkArgsLength() {
  if (fsItems.length == 0) {
    fsItems.push(".");
  }
}

function filterFilesAndDirs() {
  dirArgs = fsItems.filter((p) => fs.statSync(currentWorkingDirectory + "/" + p).isDirectory());
  fileArgs = fsItems.filter((p) => !fs.statSync(currentWorkingDirectory + "/" + p).isDirectory());
  if (showAll == false) {
    removeDotFiles(fileArgs);
  }
}

function populateOutput() {
  if (fsItems.length == 1) {
    fileArgs.forEach((file) => {
      outputString += file + " ";
    });
    dirArgs.forEach((dir) => {
      outputString += dirOutput(dir);
    });
  } else {
    fileArgs.forEach((file) => {
      outputString += file + "\t";
    });
    dirArgs.forEach((dir) => {
      outputString += "\n\n" + dir + ":\n" + dirOutput(dir);
    });
  }
}

function dirOutput(dir) {
  let contents = fs.readdirSync(currentWorkingDirectory + "/" + dir);
  let outputStr = "";
  if (showAll) {
    outputStr += ".\t..\t";
  } else {
    for (let i = contents.length - 1; i >= 0; i--) {
      contents = removeDotFiles(contents);
    }
  }
  contents.forEach((item) => {
    outputStr += item + "\t";
  });
  return outputStr;
}

function removeDotFiles(fileList) {
  for (let i = fileList.length - 1; i >= 0; i--) {
    if (fileList[i][0] == ".") {
      fileList.splice(i, 1);
    }
  }
  return fileList;
}

function print() {
  if (printInList) {
    Flag1();
  }
  console.log(outputString.trimEnd());
}
