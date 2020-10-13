#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%

^0:: Dispatch("a 0")
^1:: Dispatch("a 1")
^2:: Dispatch("a 2")
^3:: Dispatch("a 3")
^4:: Dispatch("a 4")
^5:: Dispatch("a 5")
^6:: Dispatch("a 6")
^7:: Dispatch("a 7")
^8:: Dispatch("a 8")
^9:: Dispatch("a 9")

^!0:: Dispatch("s 0")
^!1:: Dispatch("s 1")
^!2:: Dispatch("s 2")
^!3:: Dispatch("s 3")
^!4:: Dispatch("s 4")
^!5:: Dispatch("s 5")
^!6:: Dispatch("s 6")
^!7:: Dispatch("s 7")
^!8:: Dispatch("s 8")
^!9:: Dispatch("s 9")

Dispatch(Message) {
	FileName := "data/test"
	file := FileOpen(FileName, "w")
	if !IsObject(file) {
		MsgBox Can't open "%FileName%" for writing.
		return
	}

	file.Write(Message)
	file.Close()
}