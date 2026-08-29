const fs = require("fs");
const { allowedNodeEnvironmentFlags } = require("process");

//
// ===== ls Procedure =====
function ls(args) {
  const userArgs = args.slice(2);

  executeFlags(getFlags(userArgs));

  const currentWorkingDirectory = getCurrentWorkingDirectory(args);
  const fsItems = checkArgsLength(getFsItems(userArgs));
  const dirArgs = getDirArgs(currentWorkingDirectory, fsItems);
  const fileArgs = getFileArgs(currentWorkingDirectory, fsItems);

  print(populateOutput(currentWorkingDirectory, fsItems, dirArgs, fileArgs));
}

//
// ===== Flag Handling =====
const flagHandlers = {
  1: Flag1,
  a: Flaga,
};

let printInList = false;
let showAll = false;

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
  console.error(
    `ls: invalid option -- ${flag}\nusage: ls [-@ABCFGHILOPRSTUWXabcdefghiklmnopqrstuvwxy1%,] [--color=when] [-D format] [file ...]`,
  );
  process.exit(1);
}

function Flag1() {
  printInList = true;
}

function makeList(outputString) {
  return outputString.replaceAll("\t", "\n").replaceAll("\n\n", "\n");
}

function Flaga() {
  showAll = true;
}

//
// ===== Extracting Data From Arguments =====
function getCurrentWorkingDirectory(args) {
  const index = args[1].lastIndexOf("/");
  return args[1].slice(0, index + 1);
}

function getFsItems(userArgs) {
  return userArgs.filter((arg) => !arg.startsWith("-"));
}

function checkArgsLength(fsItems) {
  if (fsItems.length == 0) fsItems.push(".");
  return fsItems;
}

function getDirArgs(currentWorkingDirectory, fsItems) {
  return fsItems.filter((p) => fs.statSync(currentWorkingDirectory + p).isDirectory());
}

function getFileArgs(currentWorkingDirectory, fsItems) {
  const fileArgs = fsItems.filter((p) => !fs.statSync(currentWorkingDirectory + p).isDirectory());
  if (showAll == false) removeDotFiles(fileArgs);
  return fileArgs;
}

//
// ===== Populating and Outputting Data =====
function populateOutput(currentWorkingDirectory, fsItems, dirArgs, fileArgs) {
  let outputString = "";
  if (fsItems.length == 1) {
    fileArgs.forEach((file) => {
      outputString += file + " ";
    });
    dirArgs.forEach((dir) => {
      outputString += dirOutput(dir, currentWorkingDirectory);
    });
  } else {
    fileArgs.forEach((file) => {
      outputString += file + "\t";
    });
    dirArgs.forEach((dir) => {
      outputString += "\n\n" + dir + ":\n" + dirOutput(dir, currentWorkingDirectory);
    });
  }
  return outputString;
}

function dirOutput(dir, currentWorkingDirectory) {
  let contents = fs.readdirSync(currentWorkingDirectory + dir);
  let outputStr = "";
  if (showAll) outputStr += ".\t..\t";
  else {
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
    if (fileList[i][0] == ".") fileList.splice(i, 1);
  }
  return fileList;
}

function print(outputString) {
  let output = outputString;
  if (printInList) output = makeList(output);
  console.log(output.trimEnd());
}

//
// ===== Run ls =====
ls(process.argv);
