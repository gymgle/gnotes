/*
Custom file name of IMG, VID, PANO as:
    Raw file name: IMG_20161201_071251.jpg
    to
    New file name: 2016-12-01 07.12.51.jpg

    Raw file name: VID_20161201_071251_1.mp4
    to
    New file name: 2016-12-01 07.12.51_1.mp4

author: Gymgle
date: 2016-12-19
*/

package main

import (
	"io/ioutil"
	"log"
	"os"
	"strings"
)

func main() {
	logName := "rename.log"
	logFile, err := os.Create(logName)
	defer logFile.Close()
	if err != nil {
		log.Fatalf("Can not create %s\n", logName)
	}
	logger := log.New(logFile, "", log.Ldate|log.Ltime)

	dir := "./"
	files, err := ioutil.ReadDir(dir)
	if err != nil {
		logger.Fatalln("Read directory error!")
	}
	for _, f := range files {
		if f.IsDir() {
			continue
		}
		fileName := f.Name()
		if (HasPrefix(fileName, "IMG_") && HasSuffix(fileName, ".jpg")) ||
			(HasPrefix(fileName, "VID_") && HasSuffix(fileName, ".mp4")) ||
			(HasPrefix(fileName, "PANO_") && HasSuffix(fileName, ".jpg")) {
			newName := customName(fileName)
			err := os.Rename(fileName, newName)
			if err != nil {
				logger.Fatalf("Rename error: %s -> %s\n", fileName, newName)
				continue
			}
			logger.Println(fileName + " -> " + newName)
		}
	}
}

// customName : 自定义文件名
func customName(fileName string) string {
	name := strings.SplitN(fileName, "_", 3)
	nameDate := name[1]
	nameTime := name[2]
	newName := nameDate[0:4] + "-" +
		nameDate[4:6] + "-" +
		nameDate[6:8] + " " +
		nameTime[0:2] + "." +
		nameTime[2:4] + "." +
		nameTime[4:]
	return newName
}

// HasPrefix : 检查 s 是否以 prefix 开始
func HasPrefix(s, prefix string) bool {
	return len(s) >= len(prefix) && s[0:len(prefix)] == prefix
}

// HasSuffix : 检查 s 是否以 suffix 结尾
func HasSuffix(s, suffix string) bool {
	return len(s) >= len(suffix) && s[len(s)-len(suffix):] == suffix
}
