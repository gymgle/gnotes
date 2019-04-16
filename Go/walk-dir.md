# walk-dir

用 go 实现遍历目录

## 方法一、使用 go 的 path/filepath 包

```go
package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	var dir string
	flag.StringVar(&dir, "d",".", "the dir to travel")
	flag.Parse()

	err := filepath.Walk(dir, walkFunc)
	if err != nil {
		fmt.Println(err)
	}
}

func walkFunc(path string, info os.FileInfo, err error) error {
	fmt.Println(path)
	return nil
}
```

## 方法二、深度优先递归实现

```go
package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	var dir string
	var level int
	flag.StringVar(&dir, "d", ".", "the dir to travel")
	flag.IntVar(&level, "l", 10, "the level depth to travel")
	flag.Parse()

	err := walkDir(dir, level)
	if err != nil {
		fmt.Println(err)
	}
}

func walkDir(path string, depth int) error {
	if depth <= 0 {
		return nil
	}

	files, err := ioutil.ReadDir(path)
	if err != nil {
		return err
	}

	for _, file := range files {
		if file.IsDir() {
			fmt.Println(path + string(os.PathSeparator) + file.Name())
			err = walkDir(path+string(os.PathSeparator)+file.Name(), depth-1)
			if err != nil {
				return err
			}
		} else {
			fmt.Println(path + string(os.PathSeparator) + file.Name())
		}
	}

	return nil
}

```

## 方法三、广度优先实现

需要借助一个队列去实现。使用 slice 模拟队列，把发现的目录放到 slice 中。

```go
package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	var dir string
	flag.StringVar(&dir, "d", ".", "the dir to travel")
	flag.Parse()

	if err := walkDir(dir); err != nil {
		fmt.Println(err)
	}
}

func walkDir(path string) error {
	dirs := make([]string, 0)
	dirs = append(dirs, path)
	for 0 < len(dirs) {
		files, err := ioutil.ReadDir(dirs[0])
		if err != nil {
			return err
		}

		for _, file := range files {
			filePath := dirs[0] + string(os.PathSeparator) + file.Name()
			fmt.Println(filePath)

			if file.IsDir() {
				dirs = append(dirs, filePath)
			}
		}
		dirs = dirs[1:]
	}

	return nil
}
```